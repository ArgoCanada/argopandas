
"""
These wrappers define a few ways to load a NetCDF file from a
:class:`argodata.mirror.Mirror` and define which tables can
be extracted from them. These objects are used under the hood
to power extraction of tables from the indexes; however, you
may use them directly if you have local NetCDF files that
conform to the Argo standards.
"""


from typing import Iterable, Union
import os
import io
import shutil
import urllib.request
import reprlib

from netCDF4 import Dataset, Variable, chartostring
from pandas import DataFrame, MultiIndex
import numpy as np

from .path import info as path_info


def _is_string_dim(x):
    return x.startswith('STRING') or x == 'DATE_TIME'


def _is_string_var(x):
    dims = x.dimensions
    return len(dims) > 0 and _is_string_dim(dims[-1])


def _dims_along_match(dims, target_dims):
    return dims == target_dims or \
        (len(dims) > 0 and _is_string_dim(dims[-1]) and dims[:-1] == target_dims)


class NetCDFWrapper:
    """
    The base class for an Argo NetCDF file. These objects
    are usually constructed using :func:`argopandas.nc` .
    """

    def __init__(self, src):
        """
        :param src: A filename, URL, raw bytes, or existing
            ``netCDF4.Dataset`` object.
        """
        if not isinstance(src, (Dataset, bytes, str)):
            raise TypeError('`src` must be a filename, url, bytes, or netCDF4.Dataset object')
        self._src = src
        self._dataset = None

    def __enter__(self):
        return self

    def __exit__(self, *execinfo):
        if self._dataset is not None and not isinstance(self._src, Dataset):
            self._dataset.close()
            self._dataset = None

    def __repr__(self):
        return f"{type(self).__name__}({reprlib.repr(self._src)})"

    def __getitem__(self, k) -> Variable:
        return self.dataset[k]

    @property
    def variables(self):
        return self.dataset.variables

    @property
    def info(self):
        """
        Returns a one-row ``DataFrame`` containing
        all dimensionless variables in the NetCDF.
        """
        return self.info_()
    
    def info_(self, vars: Union[None, str, Iterable[str]]=None):
        """
        Returns a one-row ``DataFrame`` containing
        all dimensionless variables in the NetCDF, selecting
        specific variables.
        """
        return self._data_frame_along([], vars=vars)

    @property
    def dataset(self) -> Dataset:
        """
        Return the underlying ``netCDF4.Dataset`` .
        """
        if self._dataset is None:
            self._load_dataset()
        return self._dataset

    def _data_frame_along(self, target_dims, vars=None):
        dataset = self.dataset

        if isinstance(vars, str):
            vars = [vars]

        var_names = self._var_names_along(target_dims, vars=vars)
        if not var_names:
            return DataFrame()

        if target_dims:
            dim_lengths = [len(dataset.dimensions[dim_name]) for dim_name in target_dims]
            index = MultiIndex.from_product(
                [range(size) for size in dim_lengths],
                names=target_dims
            )
            n = len(index)
        else:
            index = None
            n = 1

        values = {}
        for var_name in var_names:
            values[var_name] = self._ndarray(var_name, dataset).reshape((n, ))

        return DataFrame(values, index=index)

    def _var_names_along(self, target_dims, vars=None):
        dataset = self.dataset
        if vars is None:
            vars = dataset.variables
        target_dims = tuple(target_dims)

        target_vars = []
        for v in vars:
            dims = dataset[v].dimensions
            if _dims_along_match(dims, target_dims):
                target_vars.append(v)

        return target_vars

    def _ndarray(self, var_name, dataset=None):
        if dataset is None:
            dataset = self.dataset
        var = dataset[var_name]
        if _is_string_var(var):
            return chartostring(var[:], encoding='utf-8')
        else:
            return var[:]

    def _load_dataset(self):
        if isinstance(self._src, Dataset):
            self._dataset = self._src
        elif isinstance(self._src, str) and os.path.exists(self._src):
            self._dataset = Dataset(self._src)
        elif isinstance(self._src, bytes):
            self._dataset = Dataset('in-mem-file', mode='r', memory=self._src)
        elif self._src.startswith('http://') or self._src.startswith('https://') or self._src.startswith('ftp://'):
            buf = io.BytesIO()
            with urllib.request.urlopen(self._src) as f:
                shutil.copyfileobj(f, buf)
            self._dataset = Dataset('in-mem-file', mode='r', memory=buf.getvalue())
        else:
            raise ValueError(f"Don't know how to open '{self._src}'\n.Is it a valid file or URL?")


class ProfNetCDF(NetCDFWrapper):
    """
    Subclass representing a profile NetCDF file.
    """

    def __init__(self, src):
        super().__init__(src)

    @property
    def levels(self) -> DataFrame:
        """Extract variables along N_PROF, N_LEVELS"""
        return self.levels_()
    
    def levels_(self, vars: Union[None, str, Iterable[str]]=None) -> DataFrame:
        """Extract variables along N_PROF, N_LEVELS selecting specific variables"""
        return self._data_frame_along(('N_PROF', 'N_LEVELS'), vars=vars)

    @property
    def prof(self) -> DataFrame:
        """Extract variables along N_PROF"""
        return self.prof_()
    
    def prof_(self, vars: Union[None, str, Iterable[str]]=None) -> DataFrame:
        """Extract variables along N_PROF selecting specific variables"""
        return self._data_frame_along(('N_PROF', ), vars=vars)

    @property
    def calib(self) -> DataFrame:
        """Extract variables along N_PROF, N_CALIB, N_PARAM"""
        return self._data_frame_along(('N_PROF', 'N_CALIB', 'N_PARAM'))

    @property
    def param(self) -> DataFrame:
        """Extract variables along N_PROF, N_PARAM"""
        return self._data_frame_along(('N_PROF', 'N_PARAM'))

    @property
    def history(self) -> DataFrame:
        """Extract variables along N_HISTORY, N_PROF"""
        return self._data_frame_along(('N_HISTORY', 'N_PROF'))


class TrajNetCDF(NetCDFWrapper):
    """Subclass representing a trajectory NetCDF."""

    def __init__(self, src):
        super().__init__(src)

    @property
    def measurement(self) -> DataFrame:
        """Extract variables along N_MEASUREMENT"""
        return self.measurement_()
    
    def measurement_(self, vars: Union[None, str, Iterable[str]]=None) -> DataFrame:
        """Extract variables along N_MEASUREMENT selecting specific variables"""
        return self._data_frame_along(('N_MEASUREMENT', ), vars=vars)

    @property
    def cycle(self) -> DataFrame:
        """Extract variables along N_CYCLE"""
        return self.cycle_()
    
    def cycle_(self,  vars: Union[None, str, Iterable[str]]=None) -> DataFrame:
        """Extract variables along N_CYCLE selecting specific variables"""
        return self._data_frame_along(('N_CYCLE', ), vars=vars)

    @property
    def param(self) -> DataFrame:
        """Extract variables along N_PARAM"""
        return self._data_frame_along(('N_PARAM', ))

    @property
    def history(self):
        """Extract variables along N_HISTORY"""
        return self._data_frame_along(('N_HISTORY', ))


class TechNetCDF(NetCDFWrapper):
    """Subclass representing a tech NetCDF file"""

    def __init__(self, src):
        super().__init__(src)

    @property
    def tech_param(self) -> DataFrame:
        """Extract variables along N_TECH_PARAM"""
        return self._data_frame_along(('N_TECH_PARAM', ))


class MetaNetCDF(NetCDFWrapper):
    """
    Subclass representing a meta NetCDF file.
    """

    def __init__(self, src):
        super().__init__(src)

    @property
    def config_param(self) -> DataFrame:
        """
        Extract variables along N_CONFIG_PARAM and combine
        them with variables along N_MISSIONS and N_CONFIG_PARAM.
        """

        # non-standard for these functions, however,
        # each of these data frames is useless without the other
        params = self._data_frame_along(('N_CONFIG_PARAM', ))
        values = self._data_frame_along(('N_MISSIONS', 'N_CONFIG_PARAM'))
        n_params = len(params.index)
        n_values = len(values.index)
        if n_params == 0 or n_values == 0:
            return DataFrame()

        n_missions = int(n_values / n_params)
        params_rep = params.iloc[np.tile(range(n_params), n_missions)]
        for col in params_rep.keys():
            values[col] = params_rep[col].values

        return values

    @property
    def missions(self) -> DataFrame:
        """Extract variables along N_MISSIONS"""
        return self._data_frame_along(('N_MISSIONS', ))

    @property
    def trans_system(self) -> DataFrame:
        """Extract variables along N_TRANS_SYSTEM"""
        return self._data_frame_along(('N_TRANS_SYSTEM', ))

    @property
    def positioning_system(self) -> DataFrame:
        """Extract variables along N_POSITIONING_SYSTEM"""
        return self._data_frame_along(('N_POSITIONING_SYSTEM', ))

    @property
    def launch_config_param(self) -> DataFrame:
        """Extract variables along N_LAUNCH_CONFIG_PARAM"""
        return self._data_frame_along(('N_LAUNCH_CONFIG_PARAM', ))

    @property
    def sensor(self) -> DataFrame:
        """Extract variables along N_SENSOR"""
        return self._data_frame_along(('N_SENSOR', ))

    @property
    def param(self) -> DataFrame:
        """Extract variables along N_PARAM"""
        return self._data_frame_along(('N_PARAM', ))


def _guess_class_from_name(name):
    file_type = path_info(name)['type']

    if file_type == 'meta':
        return MetaNetCDF
    elif file_type == 'prof':
        return ProfNetCDF
    elif file_type == 'tech':
        return TechNetCDF
    elif file_type == 'traj':
        return TrajNetCDF
    else:
        return None


def _guess_class_from_wrapper(nc):
    try:
        file_type = nc.info['DATA_TYPE'][0].strip()
        if file_type == 'Argo meta-data':
            return MetaNetCDF
        elif file_type == 'Argo profile':
            return ProfNetCDF
        elif file_type == 'Argo technical data':
            return TechNetCDF
        elif file_type == 'Argo trajectory':
            return TrajNetCDF
        else:
            return NetCDFWrapper
    except:
        return NetCDFWrapper


def load_netcdf(src):
    if isinstance(src, str):
        nc_class = _guess_class_from_name(src)
        if nc_class:
            return nc_class(src)

    nc = None
    try:
        nc = NetCDFWrapper(src)
        return _guess_class_from_wrapper(nc)(src)
    finally:
        if nc and not isinstance(src, Dataset):
            nc.dataset.close()
