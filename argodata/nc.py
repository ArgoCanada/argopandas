
import os
import io
import shutil
import urllib.request

from netCDF4 import Dataset, Variable, chartostring
from pandas import DataFrame, MultiIndex


def _is_string_dim(x):
    return x.startswith('STRING') or x == 'DATE_TIME'


def _is_string_var(x):
    dims = x.dimensions
    return len(dims) > 0 and _is_string_dim(dims[-1])


def _dims_along_match(dims, target_dims):
    return dims == target_dims or \
        (len(dims) > 0 and _is_string_dim(dims[-1]) and dims[:-1] == target_dims)


class NetCDFWrapper:

    def __init__(self, src):
        if not isinstance(src, (Dataset, bytes, str)):
            raise TypeError('`src` must be a filename, url, bytes, or netCDF4.Dataset object')
        self._src = src
        self._dataset = None

    def __getitem__(self, k) -> Variable:
        return self.dataset()[k]

    def dataset(self) -> Dataset:
        if self._dataset is None:
            self._load_dataset()
        return self._dataset

    def _data_frame_along(self, target_dims, vars=None):
        dataset = self.dataset()

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
        dataset = self.dataset()
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
            dataset = self.dataset()
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



