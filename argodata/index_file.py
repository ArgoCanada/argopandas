
import gzip
import itertools
from contextlib import AbstractContextManager
from collections import deque

# needed to support Python 3.6 (contextlib.nullcontext was added in 3.7)
class nullcontext(AbstractContextManager):
    def __init__(self, enter_result=None):
        self.enter_result = enter_result

    def __enter__(self):
        return self.enter_result

    def __exit__(self, *excinfo):
        pass

class IndexFile:

    def __init__(self, src, filters=None, skip=0, limit=None):
        self._src = src
        self._filters = [] if filters is None else list(filters)
        self._skip = int(skip)
        self._limit = limit
        self._cached_len = None
        self._fresh = True

    def filter(self, *args):
        new_filters = list(self._filters) + list(args)
        return IndexFile(self._src, new_filters, self._skip, self._limit)

    def is_valid(self):
        try:
            self.validate()
            return True
        except ValueError:
            return False

    def validate(self) -> None:
        for i, f in enumerate(self._filters):
            if not callable(f):
                raise ValueError(f"filter {i} is not callable")

        try:
            with self._open() as f:
                pass
        except Exception as e:
            raise ValueError(f"Failed to open '{ self._src }': { str(e) }")

    def __getitem__(self, k):
        if isinstance(k, slice):
            k_start = k.start
            k_stop = k.stop
            if k.step is not None:
                raise ValueError("Can't subset Index with stepped slice")

            if k_start is None and k_stop is None:
                return self

            if k_start is None:
                k_start = 0

            # a common case where we can avoid calculating the length
            if k_stop is None and self._limit is None and k_start >= 0:
                return IndexFile(self._src, filters=self._filters, skip=self._skip + k_start)

            if k_start < 0 or k_stop is None or k_stop < 0:
                this_len = len(self)
                k_stop = this_len if k_stop is None else k_stop
                k_start = this_len + k_start if k_start < 0 else k_start
                k_stop = this_len + k_stop if k_stop < 0 else k_stop

            new_skip = self._skip + k_start
            new_limit = k_stop - k_start
            return IndexFile(self._src, filters=self._filters, skip=new_skip, limit=new_limit)

        elif isinstance(k, int):
            if k < 0:
                k = len(self) + k

            n = 0
            for item in self:
                if n == k:
                    return item
                n += 1

            # take this opportunity to cache the length
            if self._cached_len is None:
                self._cached_len = n

            raise IndexError(f"Can't extract item {k} from Index of length {n}")
        else:
            raise ValueError(f"Can't subset Index with object of type '{type(k).__name__}'")

    def __len__(self):
        if self._cached_len is None:
            counter = itertools.count()
            deque(zip(self, counter), maxlen=0)
            self._cached_len = next(counter)
        return self._cached_len

    def __iter__(self):
        if self._limit is not None and self._limit <= 0:
            return

        with self._open() as f:
            if not self._fresh:
                f.seek(0)
            self._fresh = False

            names = None
            length = -1
            size = 0
            for line in f:
                if not line or line.startswith(b'#'):
                    continue
                elif names is None and line.startswith(b'file,'):
                    names = line[:-1].decode('UTF-8').split(',')
                    continue

                item = {k: v for k, v in zip(names, line[:-1].decode('UTF-8').split(','))}
                if any(not f(item) for f in self._filters):
                    continue

                length += 1
                if length < self._skip:
                    continue
                yield item

                size += 1
                if size == self._limit:
                    break

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
        return f"Index({repr(self._src)}, {filter_repr}, {self._skip}, {self._limit})"

    def __str__(self) -> str:
        return repr(self)
