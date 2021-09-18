"""
This module contains an interface to the index files provided
by the GDAC. It is related to the :module:`argopandas.netcdf`
module in that there is an index subclass for each
:class:`argopandas.netcdf.NetCDFWrapper` subclass. Indexes
are ``pandas.DataFrame`` subclasses with a few accessors
that load data from each.
"""

import os
from typing import Union, Iterable
import numpy as np
import pandas as pd
from .netcdf import MetaNetCDF, NetCDFWrapper, ProfNetCDF, TechNetCDF, TrajNetCDF
from .progress import guess_progressor
from . import path
from . import _geo


class DataFrameIndex(pd.DataFrame):
    """
    A representation of a ``pandas.DataFrame`` whose ``file`` column
    represents a path to a NetCDF file on the GDAC. These objects
    are created by subsetting the global indexes (e.g., ``argopandas.prof``).
    """

    # needed to get the mirror passed on to subsets
    # https://pandas.pydata.org/pandas-docs/stable/development/extending.html#subclassing-pandas-data-structures
    _metadata = pd.DataFrame._metadata + ['_mirror']

    def __init__(self, *args, _mirror=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._mirror = _mirror

    @property
    def _constructor(self):
        return type(self)

    def _netcdf_wrapper(self, src):
        return NetCDFWrapper(src)

    def _data_frame_along(self, attr, vars=None):
        file = self['file']

        if len(file) == 0:
            return self[['file']].iloc[[]]

        # prepare the mirror
        self._mirror.prepare(['dac/' + item for item in file])

        # collect the keys and the individual data frames
        objs = []
        keys = []

        message = f"Reading {len(file)} {'files' if len(file) != 1 else 'file'}"
        pb = guess_progressor(len(file), init_message=message)

        # slightly different pattern if we need to pass 'vars' along:
        # call object.attr_(vars=vars) instead of object.attr
        with pb:
            for item in file:
                pb.bump(message=os.path.basename(item))
                nc = self._netcdf_wrapper(self._mirror.netcdf_dataset_src('dac/' + item))
                val = getattr(nc, attr) if vars is None else getattr(nc, attr + '_')(vars=vars)
                objs.append(val)
                keys.append(item)

        # combine them, adding a `file` index as a level in the multi-index
        return pd.concat(objs, keys=keys, names=["file"])

    @property
    def info(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.NetCDFWrapper.info` table for
        the files in this index.
        """
        return self.info_()
    
    def info_(self, vars: Union[None, str, Iterable[str]]=None) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.NetCDFWrapper.info` table for
        the files in this index, selecting specific variables.

        :param vars: A variable, an interable of variables, or ``None``
            to select all possible variables.
        """
        return self._data_frame_along('info', vars=vars)

    def __assert_columns(self, *cols):
        missing_cols = [col for col in cols if col not in self]
        if missing_cols:
            missing_cols_lab = ', '.join(f"'{col}'" for col in missing_cols)
            raise ValueError(f"Index is missing required columns: {missing_cols_lab}")
    
    def subset_data_mode(self, data_mode) -> pd.DataFrame:
        """
        Return the subset of this index corresponding to the specified
        ``data_mode``.

        :param data_mode: One of 'R', 'D', 'realtime' or 'delayed'
        """
        self.__assert_columns('file')
        return self[path.is_data_mode(self['file'], data_mode)]
    
    def subset_float(self, floats) -> pd.DataFrame:
        """
        Return the subset of this index corresponding to the specified
        ``floats``.

        :param floats: An integer, string, or iterable of those
            representing the float identifier(s).
        """
        self.__assert_columns('file')
        return self[path.is_float(self['file'], floats)]
    
    def subset_direction(self, direction) -> pd.DataFrame:
        """
        Return the subset of this index corresponding to the specified
        ``direction``.

        :param direction: 'ascending', 'descending', 'asc', or 'desc'
        """
        self.__assert_columns('file')
        direction = direction.lower()
        if direction in ('ascending', 'asc'):
            return self[~path.is_descending(self['file'])]
        elif direction in ('descending', 'desc'):
            return self[path.is_descending(self['file'])]
        else:
            raise ValueError("`direction` must be one of '(asc)ending' or '(desc)ending'")
    
    def subset_parameter(self, parameters) -> pd.DataFrame:
        """
        Return the subset of this index corresponding containing
        one or more of the parameters specified.

        :param parameters: A string or iterable of strings containing
            the parameters of interest.
        """
        self.__assert_columns('parameters')

        if isinstance(parameters, str):
            parameters = r'\b' + parameters.upper() + r'\b'
        else:
            parameters = r'\b)|(\b'.join(p.upper() for p in parameters)
            parameters = r'(\b' + parameters + r'\b)'

        if parameters == r'(\b\b)':
            return self.iloc[[]]
        else:
            return self[self['parameters'].str.contains(parameters)]

    def subset_date(self, date_start=None, date_end=None) -> pd.DataFrame:
        """
        Return the subset of this index representing profiles collected between
        ``date_start`` and ``date_end``.

        :param date_start: The first date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        :param date_end: The laste date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        """
        self.__assert_columns('date')

        if date_start is None and date_end is None:
            return self
        elif date_start is None and date_end is not None:
            return self[self['date'] <= date_end]
        elif date_start is not None and date_end is None:
            return self[self['date'] >= date_start]
        else:
            return self[(self['date'] >= date_start) & (self['date'] <= date_end)]

    def subset_updated(self, date_start=None, date_end=None) -> pd.DataFrame:
        """
        Return the subset of this index representing profiles updated between
        ``date_start`` and ``date_end``.

        :param date_start: The first date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        :param date_end: The laste date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        """
        self.__assert_columns('date_update')

        if date_start is None and date_end is None:
            return self
        elif date_start is None and date_end is not None:
            return self[self['date_update'] <= date_end]
        elif date_start is not None and date_end is None:
            return self[self['date_update'] >= date_start]
        else:
            return self[(self['date_update'] >= date_start) & (self['date_update'] <= date_end)]

    def subset_radius(self, latitude, longitude, radius_km) -> pd.DataFrame:
        """
        Return the subset of this index representing profiles collected 
        within ``radius_km`` of the position given by
        ``latitude``/``longitude``.

        :param latitude: The latitude of the target position.
        :param longitude: The longitude of the target position.
        :param radius_km: The number of kilometres within which profiles should
            be included.
        """
        self.__assert_columns('latitude', 'longitude')
        xy_target = {
            'x': _geo.normalize_lng(longitude),
            'y': _geo.normalize_lat(latitude)
        }
        xy = {
            'x': _geo.normalize_lng(self['longitude']),
            'y': _geo.normalize_lat(self['latitude'])
        }
        return self[_geo.geodist_lnglat(xy, xy_target) <= radius_km]
    
    def subset_rect(self, latitude_min=-np.Inf, longitude_min=-np.Inf,
                    latitude_max=np.Inf, longitude_max=np.Inf) -> pd.DataFrame:
        """
        Return the subset of this index representing profiles or trajectories 
        within the bounding box. You can specify bounding boxes that wrap around
        the international date line by specifying ``lat_min > lat_max``.

        :param latitude_min: The minimum latitude to include
        :param longitude_min: The minimum longitude to include
        :param latitude_max: The maximum latitude to include
        :param longitude_min: The maximum longitude to include
        """
        r_target = {
            'xmin': _geo.normalize_lng(longitude_min),
            'ymin': _geo.normalize_lat(latitude_min),
            'xmax': _geo.normalize_lng(longitude_max),
            'ymax': _geo.normalize_lat(latitude_max)
        }
        r_target_west, r_target_east = _geo.rect_split_dateline(r_target)

        try:
            self.__assert_columns('latitude', 'longitude')
            xy = {
                'x': _geo.normalize_lng(self['longitude']),
                'y': _geo.normalize_lat(self['latitude'])
            }

            contains = _geo.rect_contains(r_target_west, xy) | \
                _geo.rect_contains(r_target_east, xy)

            return self[contains]
        except ValueError:
            pass
            
        try:
            self.__assert_columns('latitude_max', 'longitude_max', 'latitude_min', 'longitude_min')
            r = {
                'xmin': _geo.normalize_lng(self['longitude_min']),
                'ymin': _geo.normalize_lat(self['latitude_min']),
                'xmax': _geo.normalize_lng(self['longitude_max']),
                'ymax': _geo.normalize_lat(self['latitude_max'])
            }

            # split across the dateline and check for all combinations for possible intersection
            r_west, r_east = _geo.rect_split_dateline(r)

            contains = _geo.rect_intersects(r_west, r_target_west) | \
                _geo.rect_intersects(r_west, r_target_east) | \
                _geo.rect_intersects(r_east, r_target_west) | \
                _geo.rect_intersects(r_east, r_target_east)

            return self[contains]
        except ValueError:
            pass
        
        raise ValueError("Index must have columns 'latitude' and 'longitude' or 'latitude+longitude_min+max'")


class ProfIndex(DataFrameIndex):
    """
    A subclass for an index of profile NetCDF files.
    """

    def _netcdf_wrapper(self, src):
        return ProfNetCDF(src)

    @property
    def levels(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.ProfNetCDF.levels` table for
        the files in this index.
        """
        return self.levels_()
    
    def levels_(self, vars: Union[None, str, Iterable[str]]=None) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.ProfNetCDF.levels` table for
        the files in this index, selecting specific variables.

        :param vars: A variable, an interable of variables, or ``None``
            to select all possible variables.
        """
        return self._data_frame_along('levels', vars=vars)

    @property
    def prof(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.ProfNetCDF.prof` table for
        the files in this index.
        """
        return self.prof_()
    
    def prof_(self, vars: Union[None, str, Iterable[str]]=None) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.ProfNetCDF.prof` table for
        the files in this index, selecting specific variables.

        :param vars: A variable, an interable of variables, or ``None``
            to select all possible variables.
        """
        return self._data_frame_along('prof', vars=vars)

    @property
    def calib(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.ProfNetCDF.calib` table for
        the files in this index.
        """
        return self._data_frame_along('calib')

    @property
    def param(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.ProfNetCDF.param` table for
        the files in this index.
        """
        return self._data_frame_along('param')

    @property
    def history(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.ProfNetCDF.history` table for
        the files in this index.
        """
        return self._data_frame_along('history')


class TrajIndex(DataFrameIndex):
    """
    A subclass for an index of trajectory NetCDF files.
    """

    def _netcdf_wrapper(self, src):
        return TrajNetCDF(src)

    @property
    def measurement(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.TrajNetCDF.measurement` table for
        the files in this index.
        """
        return self.measurement_()
    
    def measurement_(self, vars: Union[None, str, Iterable[str]]=None) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.TrajNetCDF.measurement` table for
        the files in this index, selecting specific variables.

        :param vars: A variable, an interable of variables, or ``None``
            to select all possible variables.
        """
        return self._data_frame_along('measurement', vars=vars)

    @property
    def cycle(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.TrajNetCDF.cycle` table for
        the files in this index.
        """
        return self.cycle_()
    
    def cycle_(self, vars: Union[None, str, Iterable[str]]=None) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.TrajNetCDF.cycle` table for
        the files in this index, selecting specific variables.

        :param vars: A variable, an interable of variables, or ``None``
            to select all possible variables.
        """
        return self._data_frame_along('cycle', vars=vars)

    @property
    def param(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.TrajNetCDF.param` table for
        the files in this index.
        """
        return self._data_frame_along('param')

    @property
    def history(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.TrajNetCDF.history` table for
        the files in this index.
        """
        return self._data_frame_along('history')


class TechIndex(DataFrameIndex):
    """
    A subclass for an index of tech NetCDF files.
    """

    def _netcdf_wrapper(self, src):
        return TechNetCDF(src)

    @property
    def tech_param(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.TechNetCDF.tech_param` table for
        the files in this index.
        """
        return self._data_frame_along('tech_param')


class MetaIndex(DataFrameIndex):
    """
    A subclass for an index of meta NetCDF files.
    """

    def _netcdf_wrapper(self, src):
        return MetaNetCDF(src)

    @property
    def config_param(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.MetaNetCDF.cycle` table for
        the files in this index.
        """
        return self._data_frame_along('config_param')

    @property
    def missions(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.MetaNetCDF.missions` table for
        the files in this index.
        """
        return self._data_frame_along('missions')

    @property
    def trans_system(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.MetaNetCDF.trans_system` table for
        the files in this index.
        """
        return self._data_frame_along('trans_system')

    @property
    def positioning_system(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.MetaNetCDF.positioning_system` table for
        the files in this index.
        """
        return self._data_frame_along('positioning_system')

    @property
    def launch_config_param(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.MetaNetCDF.launch_config_param` table for
        the files in this index.
        """
        return self._data_frame_along('launch_config_param')

    @property
    def sensor(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.MetaNetCDF.sensor` table for
        the files in this index.
        """
        return self._data_frame_along('sensor')

    @property
    def param(self) -> pd.DataFrame:
        """
        Combine the :attr:`argopandas.netcdf.MetaNetCDF.param` table for
        the files in this index.
        """
        return self._data_frame_along('param')
