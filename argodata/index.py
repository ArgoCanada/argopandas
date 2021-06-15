
import gzip
import itertools
from collections import deque

class ArgoIndex:

    def __init__(self, src, filters=None, start=0, limit=-1):
        self._src = str(src)
        self._filters = [] if filters is None else list(filters)
        self._start = int(start)
        self._limit = int(limit)
    
    def _open(self):
        return gzip.open(self._src)
    
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

    def __iter__(self):
        with self._open() as f:
            names = None
            length = -1
            size = 0
            for line in f:
                if not line or line.startswith(b'#'):
                    continue
                elif names is None and line.startswith(b'file,'):
                    names = line[:-1].decode('UTF-8').split(',')
                    continue

                length += 1
                if length < self._start:
                    continue

                item = {k: v for k, v in zip(names, line[:-1].decode('UTF-8').split(','))}
                if all(f(item) for f in self._filters):
                    yield item
                
                size += 1
                if size == self._limit:
                    break

    def __repr__(self) -> str:
        filter_repr = repr(self._filters)
        return f"ArgoIndex({repr(self._src)}, {filter_repr}, {self._start}, {self._limit})"

    def __str__(self) -> str:
        return repr(self)

    def __len__(self):
        counter = itertools.count()
        deque(zip(self, counter), maxlen=0)
        return next(counter)
