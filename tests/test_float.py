
import unittest
import os
from argopandas.float import Float
from argopandas.mirror import FileMirror
from argopandas import global_index


class TestFloat(unittest.TestCase):

    def setUp(self) -> None:
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        self.mirror = FileMirror(os.path.join(this_file, mirror_dir))

    def test_float(self):
        globals = global_index.make_globals(self.mirror)
        f = Float(2900313, globals)
        self.assertTrue(f.exists())
        self.assertEqual(f.meta.shape[0], 1)
        self.assertEqual(f.tech.shape[0], 1)
        self.assertEqual(f.traj.shape[0], 1)
        self.assertEqual(f.prof.shape[0], 8)
        self.assertEqual(f.bio_prof.shape[0], 0)
        self.assertEqual(f.synthetic_prof.shape[0], 0)
        self.assertEqual(f.bio_traj.shape[0], 0)


if __name__ == '__main__':
    unittest.main()
