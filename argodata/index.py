
import gzip
import itertools
import sqlite3
from contextlib import AbstractContextManager
from collections import deque
from typing import Iterable


# needed to support Python 3.6 (contextlib.nullcontext was added in 3.7)
class nullcontext(AbstractContextManager):
    def __init__(self, enter_result=None):
        self.enter_result = enter_result

    def __enter__(self):
        return self.enter_result

    def __exit__(self, *excinfo):
        pass


class Index:

    def __iter__(self) -> Iterable[dict]:
        raise NotImplementedError()


class SQLiteIndex:

    def __init__(self, src=':memory:'):
        self._con = sqlite3.connect(src)

    def __del__(self):
        self._con.close()


class FileIndex(Index):

    def __init__(self, src, filters=None):
        self._src = src
        self._filters = [] if filters is None else list(filters)
        self._cached_len = None
        self._fresh = True
        self._validate()

    def filter(self, *args) -> Index:
        new_filters = list(self._filters) + list(args)
        return FileIndex(self._src, new_filters)

    def _validate(self) -> None:
        for i, f in enumerate(self._filters):
            if not callable(f):
                raise ValueError(f"filter {i} is not callable")

        try:
            with self._open() as f:
                pass
        except Exception as e:
            raise ValueError(f"Failed to open {repr(self._src)}': {str(e)}")

    def __len__(self):
        if self._cached_len is None:
            counter = itertools.count()
            deque(zip(self, counter), maxlen=0)
            self._cached_len = next(counter)
        return self._cached_len

    def __iter__(self):
        with self._open() as f:
            if not self._fresh:
                f.seek(0)
            self._fresh = False

            names = None
            for line in f:
                if not line or line.startswith(b'#'):
                    continue
                elif names is None and line.startswith(b'file,'):
                    names = line[:-1].decode('UTF-8').split(',')
                    continue

                item = {k: v for k, v in zip(names, line[:-1].decode('UTF-8').split(','))}
                if any(not f(item) for f in self._filters):
                    continue

                yield item


    def _open(self):
        if isinstance(self._src, str) and self._src.endswith('.gz'):
            return gzip.open(self._src)
        elif isinstance(self._src, str):
            return open(self._src, 'rb')
        elif hasattr(self._src, 'readline') and callable(self._src.readline):
            return nullcontext(self._src)
        else:
            raise ValueError("src must be a filename or file-like object")

    def __repr__(self) -> str:
        filter_repr = repr(self._filters)
        return f"Index({repr(self._src)}, {filter_repr})"

    def __str__(self) -> str:
        return repr(self)
