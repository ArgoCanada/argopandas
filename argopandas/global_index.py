"""
This module implements the logic to lazily load index files as
necessary. The classes in this module represent the indexes
provided by the main package API (e.g., :attr:`argopandas.prof`).
"""

import gzip
import io
from typing import Iterable, Union
import urllib.request
import numpy as np
import pandas as pd
import pyarrow
import pyarrow.csv as csv
from . import index
from .mirror import Mirror

# Using pyarrow for date parsing because this takes
# minutes using pandas. Hard-coding the 8-line header here
def _read_index_csv(file_obj, nrows=None):
    # pyarrow doesn't have a concept of 'nrows' but it's really important
    # for partial downloading of the giant prof index
    if nrows is not None:
        buf = io.BytesIO()
        n = 0
        for line in file_obj:
            n += 1
            buf.write(line)
            if n >= (nrows + 8 + 1):
                break

        buf.seek(0)
        return _read_index_csv(buf, nrows=None)

    table = pyarrow.csv.read_csv(
        file_obj,
        read_options=csv.ReadOptions(skip_rows=8),
        convert_options=csv.ConvertOptions(
            column_types={
                'date': pyarrow.timestamp('s', tz='utc'),
                'date_update': pyarrow.timestamp('s', tz='utc')
            },
            timestamp_parsers=['%Y%m%d%H%M%S']
        )
    )

    return table.to_pandas()


class GlobalIndex:
    """
    Abstract base class for global indexes implementing the logic to
    make these lazy and data frame-like (without unnecessarily downloading
    the index until requested).
    """

    def __init__(self, path: str):
        self._path = path
        self._mirror = Mirror()
        self._cached_index = None
    
    def reset(self):
        self._cached_index = None

    def is_downloaded(self):
        return self._cached_index is not None

    def short_repr(self):
        if self.is_downloaded():
            return f"{type(self).__name__}"
        else:
            return f"Lazy {type(self).__name__}"

    def _index(self):
        if self._cached_index is None:
            self._load_index()
        return self._cached_index

    def _set_mirror(self, mirror):
        if mirror is not self._mirror:
            self._mirror = mirror
            self._cached_index = None

    def _load_index(self, nrows=None):
        if nrows is None:
            self._mirror.prepare([self._path])
            with self._mirror.open(self._path) as fg:
                with gzip.open(fg) as f:
                    self._cached_index = self._make_index(f, nrows=nrows)
                    return self._cached_index
        else:
            # we want to try to download/load as little as possible
            # here so that we can get a preview of the index
            # we want a URL connection for this if there's no cached
            # file (otherwise we want the cached file for consistency)
            try:
                filename = self._mirror.filename(self._path)
                with open(filename, 'rb') as fg:
                    with gzip.open(fg) as f:
                        return self._make_index(f, nrows=nrows)
            except (FileNotFoundError, NotImplementedError):
                url = self._mirror.url(self._path)
                with urllib.request.urlopen(url) as fg:
                    with gzip.open(fg) as f:
                        return self._make_index(f, nrows=nrows)

    def _make_index(self, file, nrows=None) -> index.DataFrameIndex:
        raise NotImplementedError()  # pragma: no cover

    def head(self, n=6):
        """
        Get the first ``n`` rows of this index without downloading it.
        """
        if self._cached_index is None:
            return self._load_index(n)
        else:
            return self._index().head(n)

    def __getitem__(self, k) -> Union[index.DataFrameIndex, pd.Series]:
        return self._index()[k]

    @property
    def loc(self) -> index.DataFrameIndex:
        return self._index().loc

    @property
    def iloc(self) -> index.DataFrameIndex:
        return self._index().iloc

    def subset_data_mode(self, data_mode: str) -> index.DataFrameIndex:
        """
        Return the subset of this index corresponding to the specified
        ``data_mode``.
        See :meth:`argopandas.index.DataFrameIndex.subset_data_mode`.

        :param data_mode: One of 'R', 'D', 'realtime' or 'delayed'
        """
        return self._index().subset_data_mode(data_mode)
    
    def subset_float(self, floats: Union[str, int, Iterable[Union[str, int]]]) -> index.DataFrameIndex:
        """
        Return the subset of this index corresponding to the specified
        ``floats``.
        See :meth:`argopandas.index.DataFrameIndex.subset_float`.

        :param floats: An integer, string, or iterable of those
            representing the float identifier(s).
        """
        return self._index().subset_float(floats)
    
    def subset_direction(self, direction: str) -> index.DataFrameIndex:
        """
        Return the subset of this index corresponding to the specified
        ``direction``.
        See :meth:`argopandas.index.DataFrameIndex.subset_direction`.

        :param direction: 'ascending', 'descending', 'asc', or 'desc'
        """
        return self._index().subset_direction(direction)
    
    def subset_parameter(self, parameters: Union[None, str, Iterable[str]]) -> index.DataFrameIndex:
        """
        Return the subset of this index corresponding containing
        one or more of the parameters specified.
        See :meth:`argopandas.index.DataFrameIndex.subset_parameter`.

        :param parameters: A string or iterable of strings containing
            the parameters of interest.
        """
        return self._index().subset_parameter(parameters)

    def subset_date(self, date_start=None, date_end=None) -> index.DataFrameIndex:
        """
        Return the subset of this index representing profiles collected between
        ``date_start`` and ``date_end``.
        See :meth:`argopandas.index.DataFrameIndex.subset_date`.

        :param date_start: The first date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        :param date_end: The laste date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        """
        return self._index().subset_date(date_start, date_end)

    def subset_updated(self, date_start=None, date_end=None) -> index.DataFrameIndex:
        """
        Return the subset of this index representing profiles updated between
        ``date_start`` and ``date_end``.
        See :meth:`argopandas.index.DataFrameIndex.subset_updated`.

        :param date_start: The first date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        :param date_end: The laste date to include in the subset. Can be a
            pandas-style date abbreviation like '2021' or '2021-09' or a
            datetime object.
        """
        return self._index().subset_updated(date_start, date_end)

    def subset_radius(self, latitude, longitude, radius_km) -> index.DataFrameIndex:
        """
        Return the subset of this index representing profiles collected 
        within ``radius_km`` of the position given by
        ``latitude``/``longitude``.
        See :meth:`argopandas.index.DataFrameIndex.subset_radius`.

        :param latitude: The latitude of the target position.
        :param longitude: The longitude of the target position.
        :param radius_km: The number of kilometres within which profiles should
            be included.
        """
        return self._index().subset_radius(latitude, longitude, radius_km)
    
    def subset_rect(self, latitude_min=-np.Inf, longitude_min=-np.Inf,
                    latitude_max=np.Inf, longitude_max=np.Inf) -> index.DataFrameIndex:
        """
        Return the subset of this index representing profiles or trajectories 
        within the bounding box. You can specify bounding boxes that wrap around
        the international date line by specifying ``lat_min > lat_max``.
        See :meth:`argopandas.index.DataFrameIndex.subset_rect`.

        :param latitude_min: The minimum latitude to include
        :param longitude_min: The minimum longitude to include
        :param latitude_max: The maximum latitude to include
        :param longitude_min: The maximum longitude to include
        """
        return self._index().subset_rect(latitude_min, longitude_min, latitude_max, longitude_max)

    def _repr_html_(self):
        if self.is_downloaded():
            rep = f"{self.short_repr()} (downloaded)"
            html = self._index()._repr_html_()
        else:
            rep = f"{self.short_repr()} (preview)"
            html = self.head()._repr_html_()

        return f"<p>{rep}</p>\n{html}"

    def __repr__(self):
        if self.is_downloaded():
            return f"{self.short_repr()}\n{repr(self._index())}"
        else:
            return f"{self.short_repr()} (preview)\n{repr(self.head())}"


class GlobalMeta(GlobalIndex):
    """
    The global meta index (i.e., 'ar_index_global_meta.txt.gz'). Subsets
    of the global meta index are :class:`argopandas.index.MetaIndex` objects.
    This object is available as the :attr:`argopandas.meta` object.
    """

    def __init__(self):
        super().__init__('ar_index_global_meta.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.MetaIndex(df, _mirror=self._mirror)


class GlobalTech(GlobalIndex):
    """
    The global tech index (i.e., 'ar_index_global_tech.txt.gz'). Subsets
    of the global meta index are :class:`argopandas.index.TechIndex` objects.
    This object is available as the :attr:`argopandas.tech` object.
    """

    def __init__(self):
        super().__init__('ar_index_global_tech.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.TechIndex(df, _mirror=self._mirror)


class GlobalTraj(GlobalIndex):
    """
    The global trajectory index (i.e., 'ar_index_global_traj.txt.gz'). Subsets
    of the global meta index are :class:`argopandas.index.TrajIndex` objects.
    This object is available as the :attr:`argopandas.traj` object.
    """

    def __init__(self):
        super().__init__('ar_index_global_traj.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.TrajIndex(df, _mirror=self._mirror)


class GlobalProf(GlobalIndex):
    """
    The global profile index (i.e., 'ar_index_global_prof.txt.gz'). Subsets
    of the global meta index are :class:`argopandas.index.ProfIndex` objects.
    This object is available as the :attr:`argopandas.prof` object.
    """

    def __init__(self):
        super().__init__('ar_index_global_prof.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.ProfIndex(df, _mirror=self._mirror)


class GlobalBioTraj(GlobalIndex):
    """
    The global BGC trajectory index (i.e., 'argo_bio-traj_index.txt.gz').
    Subsets are :class:`argopandas.index.TrajIndex` objects.
    This object is available as the :attr:`argopandas.bio_traj` object.
    """

    def __init__(self):
        super().__init__('argo_bio-traj_index.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.TrajIndex(df, _mirror=self._mirror)


class GlobalBioProf(GlobalIndex):
    """
    The global BGC profile index (i.e., 'argo_bio-profile_index.txt.gz').
    Subsets are :class:`argopandas.index.ProfIndex` objects.
    This object is available as the :attr:`argopandas.bio_prof` object.
    """

    def __init__(self):
        super().__init__('argo_bio-profile_index.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.ProfIndex(df, _mirror=self._mirror)


class GlobalSyntheticProf(GlobalIndex):
    """
    The global BGC synthetic profile index (i.e., 'argo_synthetic-profile_index.txt.gz').
    Subsets are :class:`argopandas.index.ProfIndex` objects. This object is
    avilable as the :attr:`argopandas.synthetic_prof` object.
    """

    def __init__(self):
        super().__init__('argo_synthetic-profile_index.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.ProfIndex(df, _mirror=self._mirror)


def make_globals(mirror=None):
    globals = {
        'prof': GlobalProf(),
        'traj': GlobalTraj(),
        'tech': GlobalTech(),
        'meta': GlobalMeta(),
        'bio_traj': GlobalBioTraj(),
        'bio_prof': GlobalBioProf(),
        'synthetic_prof': GlobalSyntheticProf()
    }

    if mirror is not None:
        for v in globals.values():
            v._set_mirror(mirror)

    return globals
