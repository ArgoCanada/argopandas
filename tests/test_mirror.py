
import unittest
import os

from argodata.mirror import Mirror, FileMirror, PathsDoNotExistError, UrlMirror

class TestPathsDoNotExistError(unittest.TestCase):

    def test_error(self):
        self.assertEqual(PathsDoNotExistError(["some file"]).bad_paths, ["some file"])
        self.assertRegex(str(PathsDoNotExistError(["some file"] * 21)), r'\.\.\.and 1 more')

class TestAbstractMirror(unittest.TestCase):

    def test_abstract_mirror(self):
        with self.assertRaises(NotImplementedError):
            Mirror().open("file")
        with self.assertRaises(NotImplementedError):
            Mirror().prepare(["file", ])
        with self.assertRaises(NotImplementedError):
            Mirror().filename("file")

class TestFileMirror(unittest.TestCase):

    def setUp(self):
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        self.mirror_dir = os.path.join(this_file, mirror_dir)

    def test_init(self):
        with self.assertRaises(ValueError):
            FileMirror("not a directory")

    def test_repl(self):
        self.assertRegex(repr(FileMirror(self.mirror_dir)), r'FileMirror\([^\)]+\)')

    def test_open(self):
        with FileMirror(self.mirror_dir).open('ar_index_global_meta.txt.gz') as f:
            self.assertEqual(f.read(4), b'\x1f\x8b\x08\x00')

    def test_filename(self):
        mirror = FileMirror(self.mirror_dir)
        self.assertEqual(
            mirror.filename("some_file"),
            os.path.join(self.mirror_dir, "some_file")
        )

    def test_prepare(self):
        mirror = FileMirror(self.mirror_dir)
        self.assertIs(mirror.prepare(['ar_index_global_meta.txt.gz']), mirror)
        with self.assertRaises(PathsDoNotExistError):
            mirror.prepare(["not a file"])

class TestUrlMirror(unittest.TestCase):

    def test_url(self):
        self.assertEqual(UrlMirror('some_url').url('some_file'), 'some_url/some_file')
        self.assertEqual(UrlMirror('some_url/').url('some_file'), 'some_url/some_file')
        self.assertEqual(UrlMirror('some_url').url('/some_file'), 'some_url/some_file')
        self.assertEqual(UrlMirror('some_url/').url('/some_file'), 'some_url/some_file')

    def test_repr(self):
        self.assertEqual(repr(UrlMirror('something')), "argo.UrlMirror('something')")
    
    def test_filename(self):
        with self.assertRaises(NotImplementedError):
            UrlMirror('something').filename('something')
    
    def test_prepare(self):
        mirror = UrlMirror('something')
        self.assertIs(mirror.prepare([]), mirror)
    
    def test_open(self):
        mirror = UrlMirror('https://httpbin.org')
        with mirror.open('get') as f:
            self.assertTrue(hasattr(f, 'read'))
