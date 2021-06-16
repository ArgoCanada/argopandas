
import os
from typing import BinaryIO

class PathsDoNotExistError(Exception):

    def __init__(self, bad_paths):
        self.bad_paths = bad_paths
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
