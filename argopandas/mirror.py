
"""
The Mirror API is responsible for mapping file requests to a
URL, local filename, file-like object, or something that can
construct a NetCDF ``Dataset``. These are usually constructred
using :func:`argopandas.url_mirror` and/or
:func:`argopandas.file_mirror`.
"""


from argopandas.downloader import download_async
import os
import urllib.request
import tempfile
from typing import BinaryIO


class PathsDoNotExistError(Exception):
    """
    The exception thrown when one or more requested path
    does not exist locally and could not be downloaded.
    """

    def __init__(self, bad_paths, errors=None):
        self.bad_paths = bad_paths
        self.errors = errors
        path_summary = "\n".join("'" + path + "'" for path in bad_paths[:20])
        if len(bad_paths) > 20:
            path_summary = path_summary + f'\n...and {len(bad_paths) - 20} more'
        super().__init__(path_summary)


class Mirror:
    """
    The ``Mirror`` class is the abstract base class for
    other mirror types. You can define your own subclass
    and use it in the main API if you have a non-standard
    mapping of files and would like to use features of the
    package-level API.

    :param path: A path to a file on the GDAC (e.g.,
      /dac/csio/1234/1234_meta.nc)
    """

    def __init__(self):
        # used to cache objects generated from the mirror like global indexes
        self.cache = {}
    
    def reset(self):
        self.cache = {}

    def open(self, path) -> BinaryIO:
        """Get a file-like object for this ``path``."""
        raise NotImplementedError()

    def filename(self, path) -> str:
        """
        Get a filename for this path. The filename is not
        guaranteed to exist unless :meth:`prepare` is called
        first.
        """
        raise NotImplementedError()

    def prepare(self, path_iter):
        """
        Prepare the mirror for loading all the paths in
        ``path_iter`` (e.g., by downloading them).

        :param path_iter: An iterable of ``path`` s.
        """
        raise NotImplementedError()

    def url(self, path):
        """
        Return the URL to ``path`` without checking
        if it exists.
        """
        raise NotImplementedError()

    def netcdf_dataset_src(self, path):
        """
        Return the best available input to
        :class:`argopandas.netcdf.NetCDFWrapper`.
        """
        raise NotImplementedError()


class FileMirror(Mirror):
    """
    The ``FileMirror`` maps a root directory on a filesystem.
    This is useful if you have a local copy of Argo downloaded
    via ``rsync`` or via a stable DOI version of the GDAC. This
    can also be a partial copy if you have a few files you
    need to access frequently.
    """

    def __init__(self, root):
        """
        :param root: The root directory containing the files.
        """
        super().__init__()
        if not os.path.isdir(root):
            raise ValueError(f"'{root}' is not a directory")
        self._root = root

    def __repr__(self) -> str:
        return f"argo.FileMirror({repr(self._root)})"

    def open(self, path) -> BinaryIO:
        return open(os.path.join(self._root, path), mode='rb')

    def filename(self, path) -> str:
        return os.path.join(self._root, path)

    def url(self, path) -> str:
        abspath = os.path.abspath(self.filename(path))
        return 'file://' + abspath.replace('\\', '/')

    def prepare(self, path_iter):
        bad_paths = []
        for path in path_iter:
            abs_path = os.path.join(self._root, path)
            if not os.path.isfile(abs_path):
                bad_paths.append(path)

        if bad_paths:
            raise PathsDoNotExistError(bad_paths)

        return self

    def netcdf_dataset_src(self, path):
        return self.filename(path)


class UrlMirror(Mirror):
    """
    The ``UrlMirror`` is a cache-less mirror that only uses
    URL connections. You probably want the :class:`CachedUrlMirror`
    unless you are doing real-time work that might be affected
    by an out-of-date cache. Note that :meth:`filename` is not
    supported by the ``UrlMirror`` (use :meth:`open` instead).
    """

    def __init__(self, root):
        """
        :param root: The URL of the base directory. This can
            be anything supported by ``urllib.request.urlopen``.
        """
        super().__init__()
        if root.endswith('/'):
            root = root[:-1]
        self._root = root

    def __repr__(self) -> str:
        return f"argo.UrlMirror({repr(self._root)})"

    def open(self, path) -> BinaryIO:
        return urllib.request.urlopen(self.url(path))

    def filename(self, path) -> str:
        raise NotImplementedError()

    def url(self, path) -> str:
        if path.startswith('/'):
            path = path[1:]
        return '/'.join((self._root, path))

    def prepare(self, path_iter):
        return self

    def netcdf_dataset_src(self, path):
        return self.url(path)


class CachedUrlMirror(UrlMirror):
    """
    This is the most common mirror, which uses a cache
    to avoid unnecessarily downloading the same file
    more than once. By default the cache will reset
    when the session is restarted; however, you can set
    a persistent cache using ``cache_dir``.
    """

    def __init__(self, root, cache_dir=None):
        """
        :param root: The URL of the base directory. This can
            be anything supported by ``urllib.request.urlopen``.
        :param cache_dir: The path to the local persistent cache
            or ``None`` to use a temporary directory.
        """
        super().__init__(root)
        self._temp_dir = None

        if cache_dir is None:
            self._temp_dir = tempfile.TemporaryDirectory()
            self._cache_dir = self._temp_dir.name
        else:
            if not os.path.isdir(cache_dir):
                raise ValueError(f"'{cache_dir}' is not a directory")
            self._cache_dir = cache_dir

    def __del__(self):
        if self._temp_dir is not None:
            self._temp_dir.cleanup()
    
    def reset(self):
        super().reset()
        # only delete the cache directory if it's a tempdir
        if self._temp_dir is not None:
            self._temp_dir.cleanup()
            self._temp_dir = tempfile.TemporaryDirectory()
            self._cache_dir = self._temp_dir.name

    def __repr__(self) -> str:
        if self._temp_dir is None:
            return f"argo.CachedUrlMirror({repr(self._root)}, {repr(self._cache_dir)})"
        else:
            return f"argo.CachedUrlMirror({repr(self._root)})"

    def open(self, path) -> BinaryIO:
        return open(self.filename(path), 'rb')

    def filename(self, path) -> str:
        return os.path.join(self._cache_dir, path)

    def prepare(self, path_iter):
        paths = list(path_iter)
        files = zip(
            paths,
            [self.url(path) for path in paths],
            [self.filename(path) for path in paths]
        )
        downloads = [(path, url, dest) for path, url, dest in files if not os.path.exists(dest)]
        download_files = [(item[1], item[2]) for item in downloads]
        
        errors = download_async(download_files, quiet=False, max_errors=50)
        if errors:
            path_index, errors = zip(*errors)
            bad_paths = [download_files[i][0] for i in path_index]
            raise PathsDoNotExistError(bad_paths, errors)

        return self

    def netcdf_dataset_src(self, path):
        return self.filename(path)
