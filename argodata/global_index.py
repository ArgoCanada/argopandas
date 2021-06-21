
from typing import Iterable, Union
import gzip
import reprlib

from .index import FileIndex, Index, ListIndex
from .mirror import Mirror


class GlobalIndex(ListIndex):

    def __init__(self, src, filters=None, names=None):
        if filters is not None:
            src = list(ListIndex(src, filters, names))
        super().__init__(src, filters=filters, names=names)

    def _make_item(self, item):
        return item

    def __iter__(self):
        constructor = self._make_item
        for item in self._src:
            yield constructor(item)

    def __repr__(self):
        # reprlib abbreviates lists so that these are readable in
        # interactive output
        return f"GlobalIndex({reprlib.repr(self._src)})"


class GlobalIndexRoot(Index):

    def __init__(self,
                 path: str,
                 names: Iterable[str],
                 mirror=None):
        super().__init__(None, None)
        self._path = path
        self._mirror = Mirror() if mirror is None else mirror
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
                self._cached_index = GlobalIndex(FileIndex(f), names=self._names)

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
