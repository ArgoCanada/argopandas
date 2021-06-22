
import os
import io
import shutil
import urllib.request


try:
    from netCDF4 import Dataset, Variable
except ImportError as e:  # pragma: no cover
    class Dataset:
        def __init__(self, *args, **kwargs):
            raise ImportError(
                "Package 'netCDF4' must be installed to read NetCDF files"
            )

    class Variable:
        pass


class NetCDFFile:

    def __init__(self, src):
        if not isinstance(src, (Dataset, bytes, str)):
            raise TypeError('`src` must be a filename, url, bytes, or netCDF4.Dataset object')
        self._src = src
        self._dataset = None

    def __getitem__(self, k) -> Variable:
        return self.dataset()[k]

    def dataset(self) -> Dataset:
        if self._dataset is None:
            self._load_dataset()
        return self._dataset

    def _load_dataset(self):
        if isinstance(self._src, Dataset):
            self._dataset = self._src
        elif os.path.exists(self._src):
            # netCDF4 needs forward slashes here
            self._dataset = Dataset(self._src)
        elif isinstance(self._src, bytes):
            self._dataset = Dataset('in-mem-file', mode='r', memory=self._src)
        elif self._src.startswith('http://') or self._src.startswith('https://') or self._src.startswith('ftp://'):
            buf = io.BytesIO()
            with urllib.request.urlopen(self._src) as f:
                shutil.copyfileobj(f, buf)
            self._dataset = Dataset('in-mem-file', mode='r', memory=buf.getvalue())
        else:
            raise ValueError(f"Don't know how to open '{self._src}'\n.Is it a valid file or URL?")
