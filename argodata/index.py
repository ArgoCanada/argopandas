
import gzip
import itertools
from collections import deque

class ArgoIndex:

    def __init__(self, src, filters=None, start=0, limit=None):
        self._src = str(src)
        self._filters = [] if filters is None else list(filters)
        self._start = int(start)
        self._limit = limit
        self._cached_len = None
    
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
                raise ValueError("Can't subset ArgoIndex with stepped slice")

            if k_start is None and k_stop is None:
                return self

            if k_start is None:
                k_start = 0

            # a common case where we can avoid calculating the length
            if k_stop is None and self._limit is None and k_start >= 0:
                return ArgoIndex(self._src, filters=self._filters, start=self._start + k_start)

            if k_stop is None:
                k_stop = -1

            if k_start < 0 or k_stop < 0:
                this_len = len(self)
                k_start = this_len + k_start + 1 if k_start < 0 else k_start
                k_stop = this_len + k_stop + 1 if k_stop < 0 else k_stop

            new_start = self._start + k_start
            new_limit = k_stop - k_start
            return ArgoIndex(self._src, filters=self._filters, start=new_start, limit=new_limit)

        elif isinstance(k, int):
            if k < 0:
                k = len(self) - k

            n = 0
            for item in self:
                if n == k:
                    return item
                n += 1

            # take this opportunity to cache the length
            if self._cached_len is None:
                self._cached_len = n
            
            raise IndexError(f"Can't extract item {k} from ArgoIndex of length {n}")
        else:
            raise ValueError(f"Can't subset ArgoIndex with object of type '{type(k)}'")

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
    
    def _open(self):
        return gzip.open(self._src)

    def __repr__(self) -> str:
        filter_repr = repr(self._filters)
        return f"ArgoIndex({repr(self._src)}, {filter_repr}, {self._start}, {self._limit})"

    def __str__(self) -> str:
        return repr(self)

if __name__ == '__main__':
    ind = ArgoIndex("../argodata/cache-dev/ar_index_global_meta.txt.gz")
    print(repr(ind))
    print(len(ind))
    print(repr(ind[-2:-1]))
