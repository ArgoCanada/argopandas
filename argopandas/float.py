
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
        self._cached_tables = {}

    def __repr__(self):
        constructor = f"argo.float({repr(self._float_id)})"
        tbls = [
            'prof', 'traj', 'tech', 'meta',
            'bio_prof', 'synthetic_prof', 'bio_traj'
        ]
        items = '\n'.join(f"  .{tbl} <{self.__repr_item(tbl)}>" for tbl in tbls)
        return f"{constructor}\n{items}"

    def __repr_item(self, name):
        if name in self._cached_tables:
            tbl = self._cached_tables[name]
            shape = f"[{tbl.shape[0]} x {tbl.shape[1]}]"
            return f"{type(tbl).__name__} {shape}"
        else:
            root = f"argo.{name}"
            return f"{root}[argo.path.is_float({root}['file'], {repr(self._float_id)})]"

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
        if name not in self._cached_tables:
            root = self._globals[name]
            tbl = root[path.is_float(root['file'], self._float_id)]
            self._cached_tables[name] = tbl
        return self._cached_tables[name]

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
