
import os
import urllib.request
from urllib.error import URLError
from http.client import InvalidURL
import shutil
import tempfile
from typing import BinaryIO

class PathsDoNotExistError(Exception):

    def __init__(self, bad_paths, errors=None):
        self.bad_paths = bad_paths
        self.errors = errors
        path_summary = "\n".join("'" + path + "'" for path in bad_paths[:20])
        if len(bad_paths) > 20:
            path_summary = path_summary + f'\n...and {len(bad_paths) - 20} more'
        super().__init__(path_summary)

class Mirror:

    def open(self, path) -> BinaryIO:
        raise NotImplementedError()
    
    def filename(self, path) -> str:
        raise NotImplementedError()
    
    def prepare(self, path_iter):
        raise NotImplementedError()


class FileMirror(Mirror):

    def __init__(self, root):
        if not os.path.isdir(root):
            raise ValueError(f"'{root}' is not a directory")
        self._root = root
    
    def __repr__(self) -> str:
        return f"argo.FileMirror({repr(self._root)})"

    def open(self, path) -> BinaryIO:
        return open(os.path.join(self._root, path), mode='rb')
    
    def filename(self, path) -> str:
        return os.path.join(self._root, path)

    def prepare(self, path_iter):
        bad_paths = []
        for path in path_iter:
            abs_path = os.path.join(self._root, path)
            if not os.path.isfile(abs_path):
                bad_paths.append(path)
        
        if bad_paths:
            raise PathsDoNotExistError(bad_paths)

        return self

class UrlMirror(Mirror):

    def __init__(self, root):
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

class CachedUrlMirror(UrlMirror):

    def __init__(self, root, cache_dir=None):
        super().__init__(root)

        if cache_dir is None:
            self._temp_dir = tempfile.TemporaryDirectory()
            self._cache_dir = self._temp_dir.name
        else:
            if not os.path.isdir(cache_dir):
                raise ValueError(f"'{cache_dir}' is not a directory")
            self._cache_dir = cache_dir
            self._temp_dir = None
    
    def __del__(self):
        if self._temp_dir is not None:
            self._temp_dir.cleanup()

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
        # download all the files! in the future, do the parallel thing
        bad_paths = []
        errors = []
        for path in path_iter:
            try:
                dest_file = self.filename(path)
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                with super().open(path) as src:
                    with open(dest_file, 'wb') as dst:
                        shutil.copyfileobj(src, dst)
            except (URLError, InvalidURL) as e:
                bad_paths.append(path)
                errors.append(str(e))
        
        if bad_paths:
            raise PathsDoNotExistError(bad_paths, errors)
        
        return self
