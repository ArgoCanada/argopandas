
try:
    from netCDF4 import Dataset
except ImportError as e:
    raise ImportError(
        "Package 'netCDF4' must be installed to import this module"
    ) from e


class NetCDFFile:

    def __init__(self, data=None, mirror=None):
        self._data = {} if data is None else dict(data)
        self._mirror
