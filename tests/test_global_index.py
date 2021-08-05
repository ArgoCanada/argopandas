
import os
import unittest
import pandas as pd
import argopandas.global_index as global_index
import argopandas.index as index
from argopandas.mirror import FileMirror


class TestGlobalIndex(unittest.TestCase):

    def setUp(self) -> None:
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        self.mirror = FileMirror(os.path.join(this_file, mirror_dir))

    def test_global(self):
        root = global_index.GlobalMeta()
        root._set_mirror(self.mirror)

        # make sure head() gets called without resolving the whole file
        self.assertEqual(root.head().shape[0], 2)
        self.assertIsNone(root._cached_index)

        # make sure the whole file can get resolved
        self.assertEqual(root[:].shape[0], 2)
        self.assertIsInstance(root._cached_index, pd.DataFrame)

        # ...and that calling head() again works the same
        self.assertEqual(root.head().shape[0], 2)

        # check loc and iloc
        self.assertEqual(root.iloc[0, 0], root[:].iloc[0, 0])
        self.assertEqual(root.loc[0, 'file'], root[:].loc[0, 'file'])

        # repr
        self.assertRegex(repr(root), r'^GlobalMeta')

    def test_prof(self):
        root = global_index.GlobalProf()
        root._set_mirror(self.mirror)
        self.assertIsInstance(root[:], index.ProfIndex)

    def test_bio_prof(self):
        root = global_index.GlobalBioProf()
        root._set_mirror(self.mirror)
        self.assertIsInstance(root[:], index.ProfIndex)

    def test_synethetic_prof(self):
        root = global_index.GlobalSyntheticProf()
        root._set_mirror(self.mirror)
        self.assertIsInstance(root[:], index.ProfIndex)

    def test_traj(self):
        root = global_index.GlobalTraj()
        root._set_mirror(self.mirror)
        self.assertIsInstance(root[:], index.TrajIndex)

    def test_bio_traj(self):
        root = global_index.GlobalBioTraj()
        root._set_mirror(self.mirror)
        self.assertIsInstance(root[:], index.TrajIndex)

    def test_tech(self):
        root = global_index.GlobalTech()
        root._set_mirror(self.mirror)
        self.assertIsInstance(root[:], index.TechIndex)

    def test_meta(self):
        root = global_index.GlobalMeta()
        root._set_mirror(self.mirror)
        self.assertIsInstance(root[:], index.MetaIndex)


if __name__ == '__main__':
    unittest.main()
