
from argopandas.nc import NetCDFWrapper
import tempfile
from argopandas.interactive import MirrorContext, file_mirror, url_mirror
from argopandas.index import FileIndex
from argopandas.global_index import GlobalIndex
import unittest
import os
import argopandas.interactive as argo
from argopandas.mirror import FileMirror, UrlMirror


class TestGlobalIndexInterface(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "argo-test-mirror")
        self.previous_mirror = argo.set_default_mirror(FileMirror(self.test_dir))

    def tearDown(self):
        argo.set_default_mirror(self.previous_mirror)

    def test_global_meta(self):
        self.assertEqual(len(argo.meta), 2)
        self.assertEqual(
            list(argo.meta),
            list(FileIndex(os.path.join(self.test_dir, 'ar_index_global_meta.txt.gz')))
        )
        self.assertIsInstance(argo.meta.filter(), GlobalIndex)
        self.assertRegex(repr(argo.meta), 'ar_index')
        self.assertIn('date_update', argo.meta.names())

    def test_global_tech(self):
        self.assertEqual(len(argo.tech), 2)
        self.assertEqual(
            list(argo.tech),
            list(FileIndex(os.path.join(self.test_dir, 'ar_index_global_tech.txt.gz')))
        )
        self.assertIsInstance(argo.tech.filter(), GlobalIndex)
        self.assertRegex(repr(argo.tech), 'ar_index')
        self.assertIn('date_update', argo.tech.names())

    def test_global_traj(self):
        self.assertEqual(len(argo.traj), 2)
        self.assertEqual(
            list(argo.traj),
            list(FileIndex(os.path.join(self.test_dir, 'ar_index_global_traj.txt.gz')))
        )
        self.assertIsInstance(argo.traj.filter(), GlobalIndex)
        self.assertRegex(repr(argo.traj), 'ar_index')
        self.assertIn('date_update', argo.traj.names())

    def test_global_prof(self):
        self.assertEqual(len(argo.prof), 11)
        self.assertEqual(
            list(argo.prof),
            list(FileIndex(os.path.join(self.test_dir, 'ar_index_global_prof.txt.gz')))
        )
        self.assertIsInstance(argo.prof.filter(), GlobalIndex)
        self.assertRegex(repr(argo.prof), 'ar_index')
        self.assertIn('date_update', argo.prof.names())

    def test_global_bio_traj(self):
        self.assertEqual(len(argo.bio_traj), 1)
        self.assertEqual(
            list(argo.bio_traj),
            list(FileIndex(os.path.join(self.test_dir, 'argo_bio-traj_index.txt.gz')))
        )
        self.assertIsInstance(argo.bio_traj.filter(), GlobalIndex)
        self.assertRegex(repr(argo.bio_traj), '_index')
        self.assertIn('date_update', argo.bio_traj.names())

    def test_global_bio_prof(self):
        self.assertEqual(len(argo.bio_prof), 5)
        self.assertEqual(
            list(argo.bio_prof),
            list(FileIndex(os.path.join(self.test_dir, 'argo_bio-profile_index.txt.gz')))
        )
        self.assertIsInstance(argo.bio_prof.filter(), GlobalIndex)
        self.assertRegex(repr(argo.bio_prof), '_index')
        self.assertIn('date_update', argo.bio_prof.names())

    def test_global_synthetic_prof(self):
        self.assertEqual(len(argo.synthetic_prof), 5)
        self.assertEqual(
            list(argo.synthetic_prof),
            list(FileIndex(os.path.join(self.test_dir, 'argo_synthetic-profile_index.txt.gz')))
        )
        self.assertIsInstance(argo.synthetic_prof.filter(), GlobalIndex)
        self.assertRegex(repr(argo.synthetic_prof), '_index')
        self.assertIn('date_update', argo.synthetic_prof.names())


class TestGlobalMirrors(unittest.TestCase):

    def test_global_mirror(self):
        import argopandas.interactive as argopandas_mod
        mirror = UrlMirror('something')
        prev_mirror = argopandas_mod.set_default_mirror(mirror)
        self.assertIs(argopandas_mod.default_mirror(), mirror)
        self.assertIs(argopandas_mod.set_default_mirror(prev_mirror), mirror)
        self.assertIs(argopandas_mod.default_mirror(), prev_mirror)


class TestMirrorContext(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "argo-test-mirror")
        self.mirror = FileMirror(self.test_dir)

    def test_mirror_context(self):
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
        with url_mirror('some_root') as m:
            self.assertEqual(m.url('something'), 'some_root/something')
            self.assertIs(argo.default_mirror(), m)
        with url_mirror('some_root', cached=False) as m:
            self.assertEqual(m.url('something'), 'some_root/something')
            self.assertIs(argo.default_mirror(), m)

    def test_file_mirror(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with file_mirror(temp_dir) as m:
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
        self.assertIsInstance(argo.nc(actual_file), NetCDFWrapper)
        for fiter in argo.nc([actual_file]):
            self.assertIsInstance(fiter, NetCDFWrapper)


if __name__ == '__main__':
    unittest.main()
