
import tempfile
import unittest
import os
import argopandas as argo
from argopandas.mirror import FileMirror, UrlMirror
import argopandas.global_index as global_index
from argopandas.netcdf import NetCDFWrapper, ProfNetCDF


class TestGlobalIndexInterface(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "argo-test-mirror")
        self.mirror = FileMirror(self.test_dir)
        self.previous_mirror = argo.set_default_mirror(self.mirror)

    def tearDown(self):
        argo.set_default_mirror(self.previous_mirror)

    def test_global(self):
        self.assertIsInstance(argo.prof, global_index.GlobalProf)
        self.assertIs(argo.prof._mirror, self.mirror)

        self.assertIsInstance(argo.traj, global_index.GlobalTraj)
        self.assertIs(argo.traj._mirror, self.mirror)

        self.assertIsInstance(argo.tech, global_index.GlobalTech)
        self.assertIs(argo.tech._mirror, self.mirror)

        self.assertIsInstance(argo.meta, global_index.GlobalMeta)
        self.assertIs(argo.meta._mirror, self.mirror)

        self.assertIsInstance(argo.bio_prof, global_index.GlobalBioProf)
        self.assertIs(argo.bio_prof._mirror, self.mirror)

        self.assertIsInstance(argo.synthetic_prof, global_index.GlobalSyntheticProf)
        self.assertIs(argo.meta._mirror, self.mirror)

        self.assertIsInstance(argo.bio_traj, global_index.GlobalBioTraj)
        self.assertIs(argo.meta._mirror, self.mirror)
    
    def test_reset(self):
        old_vals = [
            argo.meta, argo.tech, argo.prof, argo.traj,
            argo.bio_prof, argo.synthetic_prof, argo.bio_traj
        ]
        # force resolving the index for all indexes
        for val in old_vals:
            val[:]

        old_mirror = argo.default_mirror()

        # reset
        argo.reset()

        self.assertTrue(argo.default_mirror(), old_mirror)

        new_vals = [
            argo.meta, argo.tech, argo.prof, argo.traj,
            argo.bio_prof, argo.synthetic_prof, argo.bio_traj
        ]
        for old, new in zip(old_vals, new_vals):
            self.assertFalse(old is new)
            self.assertIsNone(new._cached_index)
            self.assertIsNotNone(old._cached_index)


class TestGlobalMirrors(unittest.TestCase):

    def test_global_mirror(self):
        mirror = UrlMirror('something')
        prev_mirror = argo.set_default_mirror(mirror)
        self.assertIs(argo.default_mirror(), mirror)
        self.assertIs(argo.set_default_mirror(prev_mirror), mirror)
        self.assertIs(argo.default_mirror(), prev_mirror)


class TestMirrorContext(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "argo-test-mirror")
        self.mirror = FileMirror(self.test_dir)

    def test_mirror_context(self):
        from argopandas._interactive import MirrorContext
        # test use without the with: syntax
        m = MirrorContext(self.mirror)
        self.assertTrue(os.path.exists(m.filename('ar_index_global_meta.txt.gz')))
        with m.open('ar_index_global_meta.txt.gz') as f:
            self.assertTrue(hasattr(f, 'read'))
        self.assertRegex(m.url('ar_index_global_meta.txt.gz'), r'^file://')
        self.assertIs(m.prepare([]), m)

        prev_mirror = argo.default_mirror()
        with MirrorContext(self.mirror) as m:
            self.assertIs(argo.default_mirror(), m)
            self.assertTrue(os.path.exists(m.filename('ar_index_global_meta.txt.gz')))
            with m.open('ar_index_global_meta.txt.gz') as f:
                self.assertTrue(hasattr(f, 'read'))
            self.assertRegex(m.url('ar_index_global_meta.txt.gz'), r'^file://')
            self.assertIs(m.prepare([]), m)

        self.assertIs(argo.default_mirror(), prev_mirror)

    def test_url_mirror(self):
        with argo.url_mirror('some_root') as m:
            self.assertEqual(m.url('something'), 'some_root/something')
            self.assertIs(argo.default_mirror(), m)
        with argo.url_mirror('some_root', cached=False) as m:
            self.assertEqual(m.url('something'), 'some_root/something')
            self.assertIs(argo.default_mirror(), m)

    def test_file_mirror(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with argo.file_mirror(temp_dir) as m:
                self.assertEqual(
                    m.filename('something'),
                    os.path.join(temp_dir, 'something')
                )
                self.assertIs(argo.default_mirror(), m)


class TestGlobalMirrorInterface(unittest.TestCase):

    def setUp(self):
        test_dir = os.path.join(os.path.dirname(__file__), "argo-test-mirror")
        self.previous_mirror = argo.set_default_mirror(FileMirror(test_dir))

    def tearDown(self):
        argo.set_default_mirror(self.previous_mirror)

    def test_url(self):
        self.assertRegex(argo.url('some_value'), r'some_value$')
        self.assertTrue(
            list(argo.url(['some_value'])) == [argo.url('some_value')]
        )

    def test_filename(self):
        actual_file = 'ar_index_global_meta.txt.gz'
        self.assertRegex(argo.filename(actual_file), f'{actual_file}$')
        self.assertTrue(
            list(argo.filename([actual_file])) == [argo.filename(actual_file)]
        )

    def test_file(self):
        actual_file = 'ar_index_global_meta.txt.gz'
        with argo.open(actual_file) as f:
            self.assertIsInstance(f.read(6), bytes)

        with argo.open(actual_file) as f:
            first_bytes = f.read(6)
            for fiter in argo.open([actual_file]):
                self.assertEqual(fiter.read(6), first_bytes)

    def test_nc(self):
        actual_file = 'dac/csio/2900313/profiles/D2900313_002.nc'

        # as a path
        self.assertIsInstance(argo.nc(actual_file), ProfNetCDF)
        for fiter in argo.nc([actual_file]):
            self.assertIsInstance(fiter, ProfNetCDF)

        # as a filename
        self.assertIsInstance(argo.nc(argo.filename(actual_file)), ProfNetCDF)
        for fiter in argo.nc(argo.filename([actual_file])):
            self.assertIsInstance(fiter, ProfNetCDF)

    def test_float(self):
        self.assertTrue(argo.float(2900313).exists())
        self.assertTrue(argo.float('2900313').exists())
        for float in argo.float([2900313]):
            self.assertTrue(float.exists())



if __name__ == '__main__':
    unittest.main()
