
import pandas as pd

from .netcdf import MetaNetCDF, NetCDFWrapper, ProfNetCDF, TechNetCDF, TrajNetCDF


class DataFrameIndex(pd.DataFrame):

    # needed to get the mirror passed on to subsets
    # https://pandas.pydata.org/pandas-docs/stable/development/extending.html#subclassing-pandas-data-structures
    _metadata = pd.DataFrame._metadata + ['_mirror']

    def __init__(self, *args, _mirror=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._mirror = _mirror

    @property
    def _constructor(self):
        return type(self)

    def _netcdf_wrapper(self, src):
        return NetCDFWrapper(src)

    def _data_frame_along(self, attr):
        file = self['file']

        # prepare the mirror
        self._mirror.prepare(['dac/' + item for item in file])

        # collect the keys and the individual data frames
        objs = []
        keys = []
        for item in file:
            nc = self._netcdf_wrapper(self._mirror.netcdf_dataset_src('dac/' + item))
            objs.append(getattr(nc, attr))
            keys.append(item)

        # combine them, adding a `file` index as a level in the multi-index
        return pd.concat(objs, keys=keys, names=["file"])

    @property
    def info(self):
        return self._data_frame_along('info')


class ProfIndex(DataFrameIndex):

    def _netcdf_wrapper(self, src):
        return ProfNetCDF(src)

    @property
    def levels(self):
        return self._data_frame_along('levels')

    @property
    def prof(self):
        return self._data_frame_along('prof')

    @property
    def calib(self):
        return self._data_frame_along('calib')

    @property
    def param(self):
        return self._data_frame_along('param')

    @property
    def history(self):
        return self._data_frame_along('history')


class TrajIndex(DataFrameIndex):

    def _netcdf_wrapper(self, src):
        return TrajNetCDF(src)

    @property
    def measurement(self):
        return self._data_frame_along('measurement')

    @property
    def cycle(self):
        return self._data_frame_along('cycle')

    @property
    def param(self):
        return self._data_frame_along('param')

    @property
    def history(self):
        return self._data_frame_along('history')


class TechIndex(DataFrameIndex):

    def _netcdf_wrapper(self, src):
        return TechNetCDF(src)

    @property
    def tech_param(self):
        return self._data_frame_along('tech_param')


class MetaIndex(DataFrameIndex):

    def _netcdf_wrapper(self, src):
        return MetaNetCDF(src)

    @property
    def config_param(self):
        return self._data_frame_along('config_param')

    @property
    def missions(self):
        return self._data_frame_along('missions')

    @property
    def trans_system(self):
        return self._data_frame_along('trans_system')

    @property
    def positioning_system(self):
        return self._data_frame_along('positioning_system')

    @property
    def launch_config_param(self):
        return self._data_frame_along('launch_config_param')

    @property
    def sensor(self):
        return self._data_frame_along('sensor')

    @property
    def param(self):
        return self._data_frame_along('param')
