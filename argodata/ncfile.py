
import os
import io
import shutil
import urllib.request

from .mirror import default_mirror


try:
    from netCDF4 import Dataset
except ImportError as e:
    class Dataset:  # pragma: no cover
        def __init__(self, *args, **kwargs):  # pragma: no cover
            raise ImportError(  # pragma: no cover
                "Package 'netCDF4' must be installed to read NetCDF files"  # pragma: no cover
            )  # pragma: no cover


class NetCDFFile:

    def __init__(self, src, data=None, mirror=None):
        self._src = src
        self._data = {} if data is None else data
        self._mirror = default_mirror if mirror is None else mirror
        self._dataset = None

    def __getitem__(self, k):
        return self._data[k]

    def dataset(self):
        if self._dataset is None:
            self._load_dataset()
        return self._dataset

    def _load_dataset(self):
        if os.path.isabs(self._src):
            self._dataset = Dataset(self._src)
        elif isinstance(self._src, bytes):
            self._dataset = Dataset('in-mem-file', mode='r', memory=self._src)
        elif self._src.startswith('http://') or self._src.startswith('https://') or self._src.startswith('ftp://'):
            buf = io.BytesIO()
            with urllib.request.urlopen(self._src) as f:
                shutil.copyfileobj(f, buf)
            self._dataset = Dataset('in-mem-file', mode='r', memory=buf.getvalue())
        elif self._mirror is None:
            self._dataset = Dataset(self._src)
        else:
            try:
                self._mirror.prepare([self._src])
                self._dataset = Dataset(self._mirror.filename(self._src))
                return
            except NotImplementedError:
                pass

            buf = io.BytesIO()
            with urllib.request.urlopen(self._mirror.url(self._src)) as f:
                shutil.copyfileobj(f, buf)
            self._dataset = Dataset('in-mem-file', mode='r', memory=buf.getvalue())
