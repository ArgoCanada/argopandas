
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


class GlobalTech:
    pass


class GlobalTraj:
    pass


class GlobalProf:
    pass


class GlobalBioTraj(GlobalTraj):
    pass


class GlobalBioProf(GlobalProf):
    pass


class GlobalSyntheticProf(GlobalBioProf):
    pass
