
import gzip
import itertools
from contextlib import AbstractContextManager
from collections import deque
from typing import Iterable, Tuple


# needed to support Python 3.6 (contextlib.nullcontext was added in 3.7)
class nullcontext(AbstractContextManager):
    def __init__(self, enter_result=None):
        self.enter_result = enter_result

    def __enter__(self):
        return self.enter_result

    def __exit__(self, *excinfo):
        pass


class Index:

    def __init__(self, src, filters=None):
        self._src = src
        self._filters = () if filters is None else tuple(filters)

    def filter(self, *args):
        new_filters = self._filters + tuple(args)
        return type(self)(self._src, new_filters)

    def __repr__(self) -> str:
        filter_repr = repr(self._filters)
        return f"{type(self).__name__}({repr(self._src)}, {filter_repr})"

    def __str__(self) -> str:
        return repr(self)

    def names(self) -> Tuple[str]:
        raise NotImplementedError()  # pragma: no cover

    def __iter__(self) -> Iterable[dict]:
        raise NotImplementedError()  # pragma: no cover

    def __len__(self):
        raise NotImplementedError()  # pragma: no cover


class ListIndex(Index):

    def __init__(self, src: Iterable[dict], filters=None, names=None):
        super().__init__(list(src), filters)
        if names is None and self._src:
            self._names = tuple(self._src[0].keys())
        elif names is None:
            self._names = ()
        else:
            self._names = names

    def filter(self, *args):
        new_filters = self._filters + tuple(args)
        return type(self)(self._src, new_filters, self._names)

    def names(self):
        return self._names

    def __iter__(self):
        for item in self._src:
            if any(not f(item) for f in self._filters):
                continue
            yield item

    def __len__(self):
        return len(self._src)

    def __repr__(self):
        return f"ListIndex({repr(self._src)}, {repr(self._filters)}, {repr(self._names)})"


class FileIndex(Index):

    def __init__(self, src, filters=None):
        super().__init__(src, filters)
        self._cached_len = None
        self._fresh = True
        self._names = None
        self._validate()

    def _validate(self) -> None:
        for i, f in enumerate(self._filters):
            if not callable(f):
                raise ValueError(f"filter {i} is not callable")

        try:
            with self._open() as f:
                pass
        except Exception as e:
            raise ValueError(f"Failed to open {repr(self._src)}': {str(e)}")

    def names(self):
        if self._names is None:
            for item in self:
                break
        return self._names

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
                    self._names = tuple(names)
                    continue

                item = {k: v for k, v in zip(names, line[:-1].decode('UTF-8').split(','))}
                if any(not f(item) for f in self._filters):
                    continue

                yield item

            if names is None:
                raise ValueError('Header line not found. Is this a valid index file?')

    def _open(self):
        if isinstance(self._src, str) and self._src.endswith('.gz'):
            return gzip.open(self._src)
        elif isinstance(self._src, str):
            return open(self._src, 'rb')
        elif hasattr(self._src, 'readline') and callable(self._src.readline):
            return nullcontext(self._src)
        else:
            raise ValueError("src must be a filename or file-like object")
