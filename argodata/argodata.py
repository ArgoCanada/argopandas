
from typing import Union, Iterator, BinaryIO
from .mirror import CachedUrlMirror, Mirror

_default_mirror_if_none = CachedUrlMirror('https://data-argo.ifremer.fr')
_default_mirror = None


def set_default_mirror(mirror: Mirror) -> Mirror:
    global _default_mirror
    if _default_mirror is None:
        _default_mirror = _default_mirror_if_none
    previous = _default_mirror
    _default_mirror = mirror
    return previous


def get_default_mirror():
    if _default_mirror is None:
        set_default_mirror(_default_mirror_if_none)
    return _default_mirror


def _file_iter(path, mirror):
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


def file(path: Union[str, Iterator[str]]) -> Union[str, Iterator[BinaryIO]]:
    mirror = get_default_mirror()
    if isinstance(path, str):
        return mirror.prepare([path]).open(path)
    else:
        return _file_iter(path, mirror)


def filename(path: Union[str, Iterator[str]]) -> Union[str, Iterator[str]]:
    mirror = get_default_mirror()

    if isinstance(path, str):
        return mirror.prepare([path]).filename(path)
    else:
        return _filename_iter(path, mirror)


def url(path: Union[str, Iterator[str]]) -> Union[str, Iterator[str]]:
    mirror = get_default_mirror()
    if isinstance(path, str):
        return mirror.url(path)
    else:
        return _url_iter(path, mirror)


__all__ = ('file', 'filename', 'url', 'get_default_mirror', 'set_default_mirror')
