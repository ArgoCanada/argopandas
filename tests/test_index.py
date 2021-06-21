
import unittest
import os

from argodata.index import FileIndex


def filter_true(x):
    return True


def filter_false(x):
    return False


class TestFileIndex(unittest.TestCase):

    def setUp(self):
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        index_file = "ar_index_global_meta.txt.gz"
        self.index_file = os.path.join(this_file, mirror_dir, index_file)

    def test_repr(self):
        self.assertRegex(str(FileIndex(self.index_file)), r"Index\('.*?', \(\)\)")

    def test_str(self):
        self.assertRegex(str(FileIndex(self.index_file)), r"Index\('.*?', \(\)\)")

    def test_names(self):
        self.assertEqual(
            FileIndex(self.index_file).names(),
            ('file', 'profiler_type', 'institution', 'date_update')
        )

    def test_invalid(self):
        with self.assertRaises(ValueError):
            FileIndex("not a file")
        with self.assertRaises(ValueError):
            FileIndex(self.index_file, [None, ])

    def test_existing_file_object(self):
        import gzip
        with gzip.open(self.index_file, 'rb') as f:
            ind = FileIndex(f)
            # check twice because the file object needs to be reset for each iterator
            self.assertEqual(list(ind), list(ind))

    def test_length(self):
        self.assertEqual(len(FileIndex(self.index_file)), 2)

    def test_iter(self):
        for item in FileIndex(self.index_file):
            self.assertIn('file', item.keys())
            self.assertRegex(item['file'], '_meta.nc$')

    def test_filter(self):
        self.assertEqual(len(FileIndex(self.index_file).filter(filter_false)), 0)
        self.assertEqual(
            list(FileIndex(self.index_file)),
            list(FileIndex(self.index_file).filter(filter_true))
        )


if __name__ == '__main__':
    unittest.main()
