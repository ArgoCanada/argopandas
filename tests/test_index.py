
import unittest
import os

from argodata.index import ArgoIndex

class TestArgoIndex(unittest.TestCase):

    def setUp(self):
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        index_file = "ar_index_global_meta.txt.gz"
        self.index_file = os.path.join(this_file, mirror_dir, index_file)

    def test_argo_index_repr(self):
        self.assertEqual(repr(ArgoIndex('src', None, 0, 1)), """ArgoIndex('src', [], 0, 1)""")
        self.assertEqual(repr(ArgoIndex('src')), """ArgoIndex('src', [], 0, None)""")
    
    def test_argo_str(self):
        self.assertEqual(str(ArgoIndex('src', None, 0, 1)), """ArgoIndex('src', [], 0, 1)""")
        self.assertEqual(str(ArgoIndex('src')), """ArgoIndex('src', [], 0, None)""")

    def test_index_valid(self):
        self.assertFalse(ArgoIndex("not a file").is_valid())
        self.assertTrue(ArgoIndex(self.index_file).is_valid())
        self.assertFalse(ArgoIndex(self.index_file, [None, ]).is_valid())
        self.assertTrue(ArgoIndex(self.index_file, [lambda x: True, ]).is_valid())
    
    def test_index_length(self):
        self.assertEqual(len(ArgoIndex(self.index_file)), 2)
    
    def test_index_iter(self):
        for item in ArgoIndex(self.index_file):
            self.assertIn('file', item.keys())
            self.assertRegexpMatches(item['file'], '_meta.nc$')
    
    def test_slice(self):
        ind = ArgoIndex(self.index_file)
        self.assertIs(ind[:], ind)
        self.assertEqual(len(ind[:1]), 1)
        self.assertEqual(len(ind[1:]), 1)
        self.assertEqual(len(ind[0:-1]), 1)
        self.assertEqual(len(ind[-2:-1]), 1)
        self.assertEqual(len(ind[-1:]), 1)

        with self.assertRaises(ValueError):
            ind[1:2:3]
    
    def test_debug(self):
        ind = ArgoIndex(self.index_file)
        self.assertEqual(len(ind[-1:]), 1)
        self.assertEqual(len(ind[-2:-1]), 1)

    def test_extract(self):
        ind = ArgoIndex(self.index_file)
        self.assertEqual(ind[0]["file"], "csio/2900313/2900313_meta.nc")
        self.assertEqual(ind[1]["file"], "csio/2902746/2902746_meta.nc")

if __name__ == '__main__':
    unittest.main()
