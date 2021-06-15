
import unittest
import argodata.argodata as argodata

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(argodata.hello_world(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()
