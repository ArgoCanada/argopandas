"""
The root package contains the interface for
argopandas.

Global indexes
--------------

``argopandas.meta``

    The :class:`argopandas.global_index.GlobalMeta` for the current :func:`default_mirror`.

``argopandas.tech``

    The :class:`argopandas.global_index.GlobalTech` for the current :func:`default_mirror`.

``argopandas.prof``

    The :class:`argopandas.global_index.GlobalProf` for the current :func:`default_mirror`.

``argopandas.traj``

    The :class:`argopandas.global_index.GlobalTraj` for the current :func:`default_mirror`.

``argopandas.bio_traj``

    The :class:`argopandas.global_index.GlobalBioTraj` for the current :func:`default_mirror`.

``argopandas.bio_prof``

    The :class:`argopandas.global_index.GlobalBioProf` for the current :func:`default_mirror`.

``argopandas.synthetic_prof``

    The :class:`argopandas.global_index.GlobalSyntheticProf` for the current :func:`default_mirror`.

>>> import argopandas as argo
>>> argo.meta.head(1)
                       file  profiler_type institution               date_update
0  aoml/13857/13857_meta.nc            845          AO 2018-10-11 20:00:14+00:00
>>> argo.tech.head(1)
                       file institution               date_update
0  aoml/13857/13857_tech.nc          AO 2021-04-28 20:03:35+00:00
>>> argo.prof.head(1)
                                file                      date  latitude  longitude ocean  profiler_type institution               date_update
0  aoml/13857/profiles/R13857_001.nc 1997-07-29 20:03:00+00:00     0.267    -16.032     A            845          AO 2018-10-11 18:05:20+00:00
>>> argo.bio_prof.head(1)
                                     file                      date  latitude  ...                       parameters parameter_data_mode               date_update
0  aoml/1900722/profiles/BD1900722_001.nc 2006-10-22 02:16:24+00:00   -40.316  ...  PRES TEMP_DOXY BPHASE_DOXY DOXY                RRRD 2020-03-12 15:32:30+00:00
[1 rows x 10 columns]
>>> argo.synthetic_prof.head(1)
                                     file                      date  latitude  longitude  ... institution           parameters parameter_data_mode               date_update
0  aoml/1900722/profiles/SD1900722_001.nc 2006-10-22 02:16:24+00:00   -40.316     73.389  ...          AO  PRES TEMP PSAL DOXY                DDDD 2020-10-30 13:30:05+00:00
[1 rows x 10 columns]
>>> argo.bio_traj.head(1)
                             file latitude_max latitude_min  ... institution                                         parameters               date_update
0  bodc/3901496/3901496_BRtraj.nc         None         None  ...          BO  PRES C1PHASE_DOXY C2PHASE_DOXY TEMP_DOXY DOXY ... 2021-07-22 15:44:18+00:00
[1 rows x 9 columns]

"""

from contextlib import AbstractContextManager
from typing import Union, Iterator, BinaryIO
import os

from .mirror import CachedUrlMirror, FileMirror, Mirror, UrlMirror
from . import global_index
from . import path
from .float import Float
from .netcdf import load_netcdf, NetCDFWrapper

# --- global index interface ----

_index_all = global_index.make_globals()

meta: global_index.GlobalMeta = _index_all['meta']  #: The :class:`argopandas.global_index.GlobalMeta` for the current :func:`default_mirror`.
tech: global_index.GlobalTech = _index_all['tech']
traj: global_index.GlobalTraj = _index_all['traj']
prof: global_index.GlobalProf = _index_all['prof']
bio_traj: global_index.GlobalBioTraj = _index_all['bio_traj']
bio_prof: global_index.GlobalBioProf = _index_all['bio_prof']
synthetic_prof: global_index.GlobalSyntheticProf = _index_all['synthetic_prof']


# --- global mirror preference ----

_default_mirror = None


def set_default_mirror(mirror: Mirror) -> Mirror:
    """
    Set the default mirror.

    :param mirror: One of :func:`url_mirror` or :func:`file_mirror`.
    """
    global _default_mirror
    previous = _default_mirror
    _default_mirror = mirror

    # update mirror for globals
    for index in _index_all.values():
        index._set_mirror(mirror)

    return previous


def default_mirror() -> Mirror:
    """
    Get the default mirror (e.g., used to populate
    the global indexes).

    >>> import argopandas as argo
    >>> argo.default_mirror()
    argo.CachedUrlMirror('https://data-argo.ifremer.fr')
    """
    return _default_mirror


set_default_mirror(CachedUrlMirror('https://data-argo.ifremer.fr'))


# ---- mirror wrappers that support the get/set default mirror ----

class MirrorContext(AbstractContextManager, Mirror):

    def __init__(self, mirror: Mirror):
        self._mirror = mirror
        self._prev_mirror = None

    def __enter__(self) -> Mirror:
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
    """
    Returns a mirror with an optional cache directory.

    :param root: A URL that contains a dac/ directory and
        a listing of .txt.gz index files.
    :param cache_dir: Use ``None`` to use a temporary file
        or sepcify an existing cache directory.
    :param cached: Use ``False`` to skip the cache step
        completely and operate on data sets in memory.
    """

    if cached:
        return MirrorContext(CachedUrlMirror(root, cache_dir))
    else:
        return MirrorContext(UrlMirror(root))


def file_mirror(root) -> MirrorContext:
    """
    Returns a mirror from a local file system.

    :param root: A directory that contains a dac/ directory and
        a listing of .txt.gz index files.
    """
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


def _nc_path_prepare(path, mirror):
    mirror_paths = []
    for p in path:
        is_file = os.path.isfile(p)
        is_url = p.startswith('https://') or p.startswith('http://') or p.startswith('ftp://')
        if not is_file and not is_url:
            mirror_paths.append(p)
    mirror.prepare(mirror_paths)

def _nc_load_one(path, mirror):
    is_file = os.path.isfile(path)
    is_url = path.startswith('https://') or path.startswith('http://') or path.startswith('ftp://')
    if is_file or is_url:
        return load_netcdf(path)
    else:
        return load_netcdf(mirror.netcdf_dataset_src(path))


def _nc_iter(path, mirror):
    _nc_path_prepare(path, mirror)
    for p in path:
        yield _nc_load_one(p, mirror)


def _float_iter(float, globals):
    for f in float:
        yield Float(f, globals=globals)


def open(path: Union[str, Iterator[str]]) -> Union[str, Iterator[BinaryIO]]:
    """
    Open a file or iterate over open files on the default mirror.

    :param path: One or more paths relative to the root directory.
    """
    mirror = default_mirror()
    if isinstance(path, str):
        return mirror.prepare([path]).open(path)
    else:
        return _open_iter(path, mirror)


def filename(path: Union[str, Iterator[str]]) -> Union[str, Iterator[str]]:
    """
    Download a one or more files and return the filename.
    """
    mirror = default_mirror()

    if isinstance(path, str):
        return mirror.prepare([path]).filename(path)
    else:
        return _filename_iter(path, mirror)


def url(path: Union[str, Iterator[str]]) -> Union[str, Iterator[str]]:
    """
    Return the URL to one or more files. If :func:`default_mirror`
    is a :func:`file_mirror`, this will be a ``file://`` URL.
    """
    mirror = default_mirror()
    if isinstance(path, str):
        return mirror.url(path)
    else:
        return _url_iter(path, mirror)


def nc(path: Union[str, Iterator[str]]) -> Union[str, Iterator[NetCDFWrapper]]:
    """
    Get a ``netCDF4.Dataset`` or iterate over multiple data sets.
    """
    mirror = default_mirror()
    if isinstance(path, str):
        _nc_path_prepare([path], mirror)
        return _nc_load_one(path, mirror)
    else:
        return _nc_iter(path, mirror)


def float(float_id: Union[str, int, Iterator[Union[str, int]]]) -> Union[Float, Iterator[Float]]:
    """
    Subset all the global indexes for a given float.

    :param float_id: A string or int float identifier or iterable
    """
    if isinstance(float_id, int) or isinstance(float_id, str):
        return Float(float_id, globals=_index_all)
    else:
        return _float_iter(float_id, globals=_index_all)


# don't include 'open' in * because it shadows the builtin open()
__all__ = (
    'filename', 'url', 'default_mirror', 'set_default_mirror',
    'meta', 'tech', 'traj', 'prof', 'bio_traj', 'bio_prof', 'nc',
    'synthetic_prof', 'path', 'float'
)
