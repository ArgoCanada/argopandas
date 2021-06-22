
from contextlib import AbstractContextManager
from typing import Union, Iterator, BinaryIO
from .mirror import CachedUrlMirror, FileMirror, NullMirror, UrlMirror
from . import global_index

# --- global index interface ----

meta = global_index.GlobalMeta()
tech = global_index.GlobalTech()
traj = global_index.GlobalTraj()
prof = global_index.GlobalProf()
bio_traj = global_index.GlobalBioTraj()
bio_prof = global_index.GlobalBioProf()
synthetic_prof = global_index.GlobalSyntheticProf()

_index_all = (meta, tech, traj, prof, bio_traj, bio_prof, synthetic_prof)

# --- global mirror preference ----

_default_mirror = None


def set_default_mirror(mirror: NullMirror) -> NullMirror:
    global _default_mirror
    previous = _default_mirror
    _default_mirror = mirror

    # update mirror for globals
    for index in _index_all:
        index._set_mirror(mirror)

    return previous


def default_mirror() -> NullMirror:
    return _default_mirror


set_default_mirror(CachedUrlMirror('https://data-argo.ifremer.fr'))


# ---- mirror wrappers that support the get/set default mirror ----

class MirrorContext(AbstractContextManager, NullMirror):

    def __init__(self, mirror: NullMirror):
        self._mirror = mirror
        self._prev_mirror = None

    def __enter__(self) -> NullMirror:
        self._prev_mirror = set_default_mirror(self._mirror)
        return self._mirror

    def __exit__(self, *excinfo):
        set_default_mirror(self._prev_mirror)

    def open(self, path) -> BinaryIO:
        return self._mirror.open(path)

    def filename(self, path) -> str:
        return self._mirror.filename(path)

    def prepare(self, path_iter):
        self._mirror.prepare(path_iter)
        return self

    def url(self, path):
        return self._mirror.url(path)


def url_mirror(root, cache_dir=None, cached=True) -> MirrorContext:
    if cached:
        return MirrorContext(CachedUrlMirror(root, cache_dir))
    else:
        return MirrorContext(UrlMirror(root))


def file_mirror(root) -> MirrorContext:
    return MirrorContext(FileMirror(root))

# ---- global mirror shortcuts ----


def _open_iter(path, mirror):
    mirror.prepare(path)
    for p in path:
        with mirror.open(p) as f:
            yield f


def _filename_iter(path, mirror):
    mirror.prepare(path)
    for p in path:
        yield mirror.filename(p)


def _url_iter(path, mirror):
    for p in path:
        yield mirror.url(p)


def open(path: Union[str, Iterator[str]]) -> Union[str, Iterator[BinaryIO]]:
    mirror = default_mirror()
    if isinstance(path, str):
        return mirror.prepare([path]).open(path)
    else:
        return _open_iter(path, mirror)


def filename(path: Union[str, Iterator[str]]) -> Union[str, Iterator[str]]:
    mirror = default_mirror()

    if isinstance(path, str):
        return mirror.prepare([path]).filename(path)
    else:
        return _filename_iter(path, mirror)


def url(path: Union[str, Iterator[str]]) -> Union[str, Iterator[str]]:
    mirror = default_mirror()
    if isinstance(path, str):
        return mirror.url(path)
    else:
        return _url_iter(path, mirror)


# don't include 'open' in * because it shadows the builtin open()
__all__ = (
    'filename', 'url', 'default_mirror', 'set_default_mirror',
    'meta', 'tech', 'traj', 'prof', 'bio_traj', 'bio_prof',
    'synthetic_prof'
)
