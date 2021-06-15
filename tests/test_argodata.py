
import unittest
import argodata.argodata as argodata

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(argodata.hello_world(), "Hello, world!")

    def test_mirror_exists(self):
        import os
        test_dir = os.path.join(os.path.dirname(__file__), "argo-test-mirror")
        self.assertTrue(os.path.isdir(test_dir))

if __name__ == '__main__':
    unittest.main()
