
from typing import Iterable, Union
from .index import FileIndex
from .mirror import Mirror

class GlobalIndex:

    def __init__(self,
                 path: str,
                 names: Iterable[str],
                 mirror: Union[Mirror, None]=None):
        self._path = path
        self._names = tuple(names)
        self._mirror = Mirror() if mirror is None else mirror
        self._index = None

    def index(self):
        if self._index is None:
            self._load_index()
        return self._index

    def _set_mirror(self, mirror):
        if mirror is not self._mirror:
            self._mirror = mirror
            self._index = None

    def _load_index(self):
        self._mirror.prepare([self._path])
        self._index = FileIndex(self._mirror.filename(self._path))

    def __iter__(self) -> Iterable[dict]:
        return iter(self.index())


class GlobalMeta(GlobalIndex):
    def __init__(self):
        super().__init__(
            'ar_index_global_meta.txt.gz',
            ('file', 'profiler_type', 'institution', 'date_update')
        )


class GlobalTech(GlobalIndex):
    def __init__(self):
        super().__init__(
            'ar_index_global_tech.txt.gz',
            ('file', 'institution', 'date_update')
        )


class GlobalTraj(GlobalIndex):
    def __init__(self):
        super().__init__(
            'ar_index_global_traj.txt.gz',
            ('file', 'latitude_max', 'latitude_min',
             'longitude_max', 'longitude_min', 'profiler_type'
             'institution', 'date_update')
        )


class GlobalProf(GlobalIndex):
    def __init__(self):
        super().__init__(
            'ar_index_global_prof.txt.gz',
            ('file', 'date', 'longitude', 'latitude', 'ocean',
             'profiler_type', 'institution', 'date_update')
        )


class GlobalBioTraj(GlobalIndex):
    def __init__(self):
        super().__init__(
            'argo_bio-traj_index.txt.gz',
            ('file', 'latitude_max', 'latitude_min',
             'longitude_max', 'longitude_min', 'profiler_type'
             'parameters', 'institution', 'date_update')
        )


class GlobalBioProf(GlobalIndex):
    def __init__(self):
        super().__init__(
            'argo_bio-profile_index.txt.gz',
            ('file', 'date', 'longitude', 'latitude', 'ocean',
             'profiler_type', 'institution', 'parameters',
             'parameter_data_mode' 'date_update')
        )


class GlobalSyntheticProf(GlobalIndex):
    def __init__(self):
        super().__init__(
            'argo_synthetic-profile_index.txt.gz',
            ('file', 'date', 'longitude', 'latitude', 'ocean',
             'profiler_type', 'institution', 'parameters',
             'parameter_data_mode' 'date_update')
        )
