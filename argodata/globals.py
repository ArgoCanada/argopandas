
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
