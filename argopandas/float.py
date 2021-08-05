
from . import path
from . import index


class Float:

    def __init__(self, float_id, globals):
        self._float_id = float_id
        self._globals = globals

    def exists(self):
        return self.meta.shape[0] > 0

    def _filtered(self, name):
        root = self._globals[name]
        return root[path.is_float(root['file'], self._float_id)]

    @property
    def prof(self) -> index.ProfIndex:
        return self._filtered('prof')

    @property
    def traj(self) -> index.TrajIndex:
        return self._filtered('traj')

    @property
    def tech(self) -> index.TechIndex:
        return self._filtered('tech')

    @property
    def meta(self) -> index.MetaIndex:
        return self._filtered('meta')

    @property
    def bio_prof(self) -> index.ProfIndex:
        return self._filtered('bio_prof')

    @property
    def synthetic_prof(self) -> index.ProfIndex:
        return self._filtered('synthetic_prof')

    @property
    def bio_traj(self) -> index.TrajIndex:
        return self._filtered('bio_traj')
