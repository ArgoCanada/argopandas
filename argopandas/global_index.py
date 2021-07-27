
from argopandas.nc import NetCDFWrapper, ProfNetCDF
from typing import Iterable
import gzip
import reprlib

import pandas as pd

from .index import FileIndex, Index, ListIndex
from .mirror import NullMirror


class GlobalIndexItem(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nc = NetCDFWrapper(b"")


class GlobalIndex(ListIndex):

    def __init__(self, src, filters=None, names=None, mirror=None):
        self._mirror = mirror
        if filters is not None:
            src = list(ListIndex(src, filters, names))
        super().__init__(src, filters=filters, names=names)

    def filter(self, *args):
        result = super().filter(*args)
        result._mirror = self._mirror
        return result

    def __getitem__(self, k) -> GlobalIndexItem:
        if isinstance(k, slice):
            return type(self)(self._src[k], names=self._names, mirror=self._mirror)
        else:
            return self._make_item(self._src[k])

    def _make_item(self, item) -> GlobalIndexItem:
        return GlobalIndexItem(item)

    def __repr__(self):
        # reprlib abbreviates lists so that these are readable in
        # interactive output
        return f"{type(self).__name__}({reprlib.repr(self._src)}, mirror={reprlib.repr(self._mirror)})"


class ProfIndex(GlobalIndex):

    def __init__(self, src, filters=None, names=None, mirror=None):
        super().__init__(src, filters=filters, names=names, mirror=mirror)

    def _make_item(self, item):
        item = GlobalIndexItem(item)
        item.nc = ProfNetCDF(self._mirror.url('dac/' + item['file']))
        return item

    @property
    def levels(self) -> pd.DataFrame:
        objs = []
        keys = []
        for item in self._src:
            objs.append(self._make_item(item).nc.levels)
            keys.append(item['file'])

        return pd.concat(objs, keys=keys, names=["file"])

    @property
    def prof(self):
        pass

    @property
    def calib(self):
        pass

    @property
    def param(self):
        pass

    @property
    def history(self):
        pass


class GlobalIndexRoot(Index):

    def __init__(self,
                 path: str,
                 names: Iterable[str],
                 mirror=None):
        super().__init__(None, None)
        self._path = path
        self._mirror = NullMirror() if mirror is None else mirror
        self._names = tuple(names)

    def _index(self):
        if self._cached_index is None:
            self._load_index()
        return self._cached_index

    def _set_mirror(self, mirror):
        if mirror is not self._mirror:
            self._mirror = mirror
            self._cached_index = None

    def _load_index(self):
        self._mirror.prepare([self._path])
        with self._mirror.open(self._path) as fg:
            with gzip.open(fg) as f:
                self._cached_index = self._make_index(FileIndex(f))

    def _make_index(self, file_index):
        return GlobalIndex(file_index, names=self._names, mirror=self._mirror)

    def filter(self, *args) -> GlobalIndex:
        return self._index().filter(*args)

    def names(self):
        return self._names

    def __iter__(self):
        return iter(self._index())

    def __len__(self):
        return len(self._index())

    def __repr__(self):
        return f"GlobalIndexRoot({repr(self._path)}, {repr(self._names)}, {repr(self._mirror)})"


class GlobalMeta(GlobalIndexRoot):
    def __init__(self):
        super().__init__(
            'ar_index_global_meta.txt.gz',
            ('file', 'profiler_type', 'institution', 'date_update')
        )


class GlobalTech(GlobalIndexRoot):
    def __init__(self):
        super().__init__(
            'ar_index_global_tech.txt.gz',
            ('file', 'institution', 'date_update')
        )


class GlobalTraj(GlobalIndexRoot):
    def __init__(self):
        super().__init__(
            'ar_index_global_traj.txt.gz',
            ('file', 'latitude_max', 'latitude_min',
             'longitude_max', 'longitude_min', 'profiler_type'
             'institution', 'date_update')
        )


class GlobalProf(GlobalIndexRoot):
    def __init__(self):
        super().__init__(
            'ar_index_global_prof.txt.gz',
            ('file', 'date', 'longitude', 'latitude', 'ocean',
             'profiler_type', 'institution', 'date_update')
        )

    def _make_index(self, file_index):
        return ProfIndex(file_index, names=self._names, mirror=self._mirror)


class GlobalBioTraj(GlobalIndexRoot):
    def __init__(self):
        super().__init__(
            'argo_bio-traj_index.txt.gz',
            ('file', 'latitude_max', 'latitude_min',
             'longitude_max', 'longitude_min', 'profiler_type'
             'parameters', 'institution', 'date_update')
        )


class GlobalBioProf(GlobalIndexRoot):
    def __init__(self):
        super().__init__(
            'argo_bio-profile_index.txt.gz',
            ('file', 'date', 'longitude', 'latitude', 'ocean',
             'profiler_type', 'institution', 'parameters',
             'parameter_data_mode', 'date_update')
        )


class GlobalSyntheticProf(GlobalIndexRoot):
    def __init__(self):
        super().__init__(
            'argo_synthetic-profile_index.txt.gz',
            ('file', 'date', 'longitude', 'latitude', 'ocean',
             'profiler_type', 'institution', 'parameters',
             'parameter_data_mode', 'date_update')
        )
