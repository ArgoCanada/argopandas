
import unittest
import os
import argodata as argo
from argodata.mirror import FileMirror

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
    
    def test_filename(self):
        actual_file = 'ar_index_global_meta.txt.gz'
        with argo.file(actual_file) as f:
            self.assertIsInstance(f.read(6), bytes)
        
        with argo.file(actual_file) as f:
            first_bytes = f.read(6)
            for fiter in argo.file([actual_file]):
                self.assertEqual(fiter.read(6), first_bytes)


if __name__ == '__main__':
    unittest.main()
