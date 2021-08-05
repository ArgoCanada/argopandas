
import gzip
import io
import urllib.request
import pyarrow
import pyarrow.csv as csv
from . import index
from .mirror import NullMirror

# using pyarrow for date parsing because this takes
# minutes using pandas
# hard-coding the 8-line header here
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

    df = table.to_pandas()
    if nrows is None:
        return df
    else:
        return df.head(nrows)


class GlobalIndex:

    def __init__(self, path: str):
        self._path = path
        self._mirror = NullMirror()

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

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.DataFrameIndex(df)

    def head(self, n=6):
        if self._cached_index is None:
            return self._load_index(n)
        else:
            return self._index().head(n)

    def __getitem__(self, k):
        return self._index()[k]

    @property
    def loc(self):
        return self._index().loc

    @property
    def iloc(self):
        return self._index().iloc

    def __repr__(self):
        return f"{type(self).__name__}({repr(self._path)}, mirror={repr(self._mirror)})"


class GlobalMeta(GlobalIndex):
    def __init__(self):
        super().__init__('ar_index_global_meta.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.MetaIndex(df, _mirror=self._mirror)


class GlobalTech(GlobalIndex):
    def __init__(self):
        super().__init__('ar_index_global_tech.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.TechIndex(df, _mirror=self._mirror)


class GlobalTraj(GlobalIndex):
    def __init__(self):
        super().__init__('ar_index_global_traj.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.TrajIndex(df, _mirror=self._mirror)


class GlobalProf(GlobalIndex):
    def __init__(self):
        super().__init__('ar_index_global_prof.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.ProfIndex(df, _mirror=self._mirror)


class GlobalBioTraj(GlobalIndex):
    def __init__(self):
        super().__init__('argo_bio-traj_index.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.TrajIndex(df, _mirror=self._mirror)


class GlobalBioProf(GlobalIndex):
    def __init__(self):
        super().__init__('argo_bio-profile_index.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.ProfIndex(df, _mirror=self._mirror)


class GlobalSyntheticProf(GlobalIndex):
    def __init__(self):
        super().__init__('argo_synthetic-profile_index.txt.gz')

    def _make_index(self, file, nrows=None):
        df = _read_index_csv(file, nrows=nrows)
        return index.ProfIndex(df, _mirror=self._mirror)
