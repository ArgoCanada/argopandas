
import unittest
import tempfile
import os

from argodata.mirror import PathsDoNotExistError, NullMirror, \
    FileMirror, UrlMirror, CachedUrlMirror


class TestPathsDoNotExistError(unittest.TestCase):

    def test_error(self):
        self.assertEqual(PathsDoNotExistError(["some file"]).bad_paths, ["some file"])
        self.assertRegex(str(PathsDoNotExistError(["some file"] * 21)), r'\.\.\.and 1 more')


class TestAbstractMirror(unittest.TestCase):

    def test_abstract_mirror(self):
        with self.assertRaises(NotImplementedError):
            NullMirror().open("file")
        with self.assertRaises(NotImplementedError):
            NullMirror().prepare(["file", ])
        with self.assertRaises(NotImplementedError):
            NullMirror().filename("file")
        with self.assertRaises(NotImplementedError):
            NullMirror().url("file")


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

    def test_url(self):
        mirror = FileMirror(self.mirror_dir)
        self.assertRegex(mirror.url('some_file'), r'^file://.*?some_file$')

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


class TestCachedUrlMirror(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            CachedUrlMirror('some_url', 'not a directory')

    def test_repr(self):
        self.assertEqual(
            repr(CachedUrlMirror('something')),
            "argo.CachedUrlMirror('something')"
        )

        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(
                repr(CachedUrlMirror('something', temp)),
                f"argo.CachedUrlMirror('something', {repr(temp)})"
            )

    def test_filename(self):
        with tempfile.TemporaryDirectory() as temp:
            mirror = CachedUrlMirror('something', temp)
            self.assertEqual(mirror.filename('file'), os.path.join(temp, 'file'))

    def test_open(self):
        with tempfile.TemporaryDirectory() as temp:
            mirror = CachedUrlMirror('something', temp)
            with open(os.path.join(temp, 'some_file'), 'wb') as f:
                f.write(b'some content')
            with mirror.open('some_file') as f:
                self.assertEqual(f.read(), b'some content')

    def test_del(self):
        mirror = CachedUrlMirror('something')
        temp_dir = mirror._cache_dir
        self.assertTrue(os.path.isdir(temp_dir))
        del mirror
        self.assertFalse(os.path.exists(temp_dir))

    def test_prepare(self):
        mirror = CachedUrlMirror('https://httpbin.org')

        # regular file
        import json
        mirror.prepare(['get'])
        self.assertTrue(os.path.isfile(mirror.filename('get')))
        with mirror.open('get') as f:
            obj = json.load(f)
            self.assertEqual(obj['url'], 'https://httpbin.org/get')

        # file in a nested directory
        mirror.prepare(['status/200'])
        self.assertTrue(os.path.isfile(mirror.filename('status/200')))

        with self.assertRaises(PathsDoNotExistError):
            mirror.prepare(["this is a bad url"])

        with self.assertRaises(PathsDoNotExistError):
            mirror.prepare(["status/404"])
            self.assertFalse(os.path.exists(mirror.filename('status/404')))
