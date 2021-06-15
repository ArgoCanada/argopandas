
class ArgoIndex:

    def __init__(self, src, filters=None, start=0, limit=-1):
        self._src = str(src)
        self._filters = [] if filters is None else list(filters)
        self._start = int(start)
        self._limit = int(limit)
    
    def is_valid(self):
        try:
            self.validate()
            return True
        except ValueError:
            return False
    
    def validate(self):
        for i, f in enumerate(self._filters):
            if not callable(f):
                raise ValueError(f"filter {i} is not callable")

        try:
            with self._open() as f:
                pass
        except Exception as e:
            raise ValueError(f"Failed to open '{ self._src }': { str(e) }")

    def __repr__(self) -> str:
        filter_repr = repr(self._filters)
        return f"ArgoIndex({repr(self._src)}, {filter_repr}, {self._start}, {self._limit})"

    def __str__(self) -> str:
        return repr(self)
    
    def _open(self):
        return open(self._src, 'r')
