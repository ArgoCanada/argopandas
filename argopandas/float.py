
from . import path
from . import index


class Float:
    """
    A representation of an Argo float based on one or more
    indexes. These objects are normally created using
    :func:`argopandas.float`.
    """

    def __init__(self, float_id, globals):
        """
        :param float_id: The float identifier as an integer
            or string.
        :param globals: A dictionary of global indexes on which
            this float is based.
        """
        self._float_id = float_id
        self._globals = globals

    def float_id(self) -> str:
        """Returns the float identifier for this float."""
        return str(self._float_id)

    def exists(self):
        """
        Returns ``True`` if this float object likely represents
        an actual float (i.e., the ``float_id`` is valid).
        """
        return self.meta.shape[0] > 0

    def _filtered(self, name):
        root = self._globals[name]
        return root[path.is_float(root['file'], self._float_id)]

    @property
    def prof(self) -> index.ProfIndex:
        """The profile index for this float."""
        return self._filtered('prof')

    @property
    def traj(self) -> index.TrajIndex:
        """The trajectory index for this float."""
        return self._filtered('traj')

    @property
    def tech(self) -> index.TechIndex:
        """The technical parameter index for this float."""
        return self._filtered('tech')

    @property
    def meta(self) -> index.MetaIndex:
        """The meta index for this float."""
        return self._filtered('meta')

    @property
    def bio_prof(self) -> index.ProfIndex:
        """The BGC profile index for this float."""
        return self._filtered('bio_prof')

    @property
    def synthetic_prof(self) -> index.ProfIndex:
        """The synthetic index for this float."""
        return self._filtered('synthetic_prof')

    @property
    def bio_traj(self) -> index.TrajIndex:
        """The BGC trajectory index for this float."""
        return self._filtered('bio_traj')
