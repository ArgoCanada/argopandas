
from argodata.mirror import FileMirror, UrlMirror
import unittest
from argodata import globals

class TestGlobalMirrors(unittest.TestCase):

    def test_global_mirror(self):
        mirror = UrlMirror('something')
        prev_mirror = globals.set_default_mirror(mirror)
        self.assertIs(globals.get_default_mirror(), mirror)
        globals._default_mirror = None
        self.assertIs(globals.get_default_mirror(), globals._default_mirror_if_none)
        self.assertIs(globals.set_default_mirror(prev_mirror), globals._default_mirror_if_none)
        self.assertIs(globals.get_default_mirror(), prev_mirror)

if __name__ == '__main__':
    unittest.main()
