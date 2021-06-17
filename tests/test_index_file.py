
import unittest
import os

from argodata.index_file import IndexFile

class TestIndexFile(unittest.TestCase):

    def setUp(self):
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        index_file = "ar_index_global_meta.txt.gz"
        self.index_file = os.path.join(this_file, mirror_dir, index_file)

    def test_repr(self):
        self.assertEqual(repr(IndexFile('src', None, 0, 1)), """Index('src', [], 0, 1)""")
        self.assertEqual(repr(IndexFile('src')), """Index('src', [], 0, None)""")

    def test_str(self):
        self.assertEqual(str(IndexFile('src', None, 0, 1)), """Index('src', [], 0, 1)""")
        self.assertEqual(str(IndexFile('src')), """Index('src', [], 0, None)""")

    def test_valid(self):
        self.assertFalse(IndexFile("not a file").is_valid())
        self.assertTrue(IndexFile(self.index_file).is_valid())
        self.assertFalse(IndexFile(self.index_file, [None, ]).is_valid())
        self.assertTrue(IndexFile(self.index_file, [lambda x: True, ]).is_valid())

    def test_existing_file_object(self):
        import gzip
        with gzip.open(self.index_file, 'rb') as f:
            ind = IndexFile(f)
            self.assertTrue(ind.is_valid())
            # check twice because the file object needs to be reset for each iterator
            self.assertEqual(list(ind), list(ind))

    def test_length(self):
        self.assertEqual(len(IndexFile(self.index_file)), 2)

    def test_iter(self):
        for item in IndexFile(self.index_file):
            self.assertIn('file', item.keys())
            self.assertRegex(item['file'], '_meta.nc$')

        count = 0
        for item in IndexFile(self.index_file, limit=0):
            count += 1
        self.assertEqual(count, 0)

    def test_filter(self):
        filter_true = lambda x: True
        filter_false = lambda x: False
        self.assertEqual(len(IndexFile(self.index_file).filter(filter_false)), 0)
        self.assertEqual(
            list(IndexFile(self.index_file)),
            list(IndexFile(self.index_file).filter(filter_true))
        )

    def test_getitem(self):
        with self.assertRaises(ValueError):
            IndexFile("dummy")[list()]

    def test_slice(self):
        ind = IndexFile(self.index_file)
        self.assertIs(ind[:], ind)
        self.assertEqual(len(ind[:1]), 1)
        self.assertEqual(len(ind[1:]), 1)
        self.assertEqual(len(ind[0:-1]), 1)
        self.assertEqual(len(ind[-2:-1]), 1)
        self.assertEqual(len(ind[-1:]), 1)
        with self.assertRaises(ValueError):
            ind[1:2:3]

    def test_slice_filtered(self):
        filter_true = lambda x: True
        filter_false = lambda x: False

        ind = IndexFile(self.index_file, [filter_true, ])
        self.assertEqual(len(ind), 2)
        self.assertIs(ind[:], ind)
        self.assertEqual(len(ind[:1]), 1)
        self.assertEqual(len(ind[1:]), 1)
        self.assertEqual(len(ind[0:-1]), 1)
        self.assertEqual(len(ind[-2:-1]), 1)
        self.assertEqual(len(ind[-1:]), 1)

        ind = IndexFile(self.index_file, [filter_false, ])
        self.assertEqual(len(ind), 0)
        self.assertIs(ind[:], ind)
        self.assertEqual(len(ind[:1]), 0)
        self.assertEqual(len(ind[1:]), 0)
        self.assertEqual(len(ind[0:-1]), 0)
        self.assertEqual(len(ind[-2:-1]), 0)
        self.assertEqual(len(ind[-1:]), 0)

    def test_extract(self):
        ind = IndexFile(self.index_file)
        with self.assertRaises(IndexError):
            ind[2]
        self.assertEqual(ind[0]["file"], "csio/2900313/2900313_meta.nc")
        self.assertEqual(ind[1]["file"], "csio/2902746/2902746_meta.nc")
        self.assertEqual(ind[-1], ind[1])
        self.assertEqual(ind[-2], ind[0])

if __name__ == '__main__':
    unittest.main()
