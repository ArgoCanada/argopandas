
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
        self.assertEqual(repr(ArgoIndex('src')), """ArgoIndex('src', [], 0, -1)""")
    
    def test_argo_str(self):
        self.assertEqual(str(ArgoIndex('src', None, 0, 1)), """ArgoIndex('src', [], 0, 1)""")
        self.assertEqual(str(ArgoIndex('src')), """ArgoIndex('src', [], 0, -1)""")

    def test_index_valid(self):
        self.assertFalse(ArgoIndex("not a file").is_valid())
        self.assertTrue(ArgoIndex(self.index_file).is_valid())
        self.assertFalse(ArgoIndex(self.index_file, [None, ]).is_valid())
        self.assertTrue(ArgoIndex(self.index_file, [lambda x: True, ]).is_valid())
        

if __name__ == '__main__':
    unittest.main()
