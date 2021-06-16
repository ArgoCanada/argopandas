
import unittest
import os

from argodata.mirror import Mirror, FileMirror, PathsDoNotExistError

class TestMirror(unittest.TestCase):

    def setUp(self):
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        self.mirror_dir = os.path.join(this_file, mirror_dir)
    
    def test_abstract_mirror(self):
        with self.assertRaises(NotImplementedError):
            Mirror().open("file")
        with self.assertRaises(NotImplementedError):
            Mirror().prepare(["file", ])
        with self.assertRaises(NotImplementedError):
            Mirror().filename("file")

    def test_file_mirror(self):
        with self.assertRaises(ValueError):
            FileMirror("not a directory")

    def test_file_mirror_repl(self):
        self.assertRegex(repr(FileMirror(self.mirror_dir)), r'FileMirror\([^\)]+\)')

    def test_file_mirror_open(self):
        with FileMirror(self.mirror_dir).open('ar_index_global_meta.txt.gz') as f:
            self.assertEqual(f.read(4), b'\x1f\x8b\x08\x00')

    def test_file_mirror_filename(self):
        mirror = FileMirror(self.mirror_dir)
        self.assertEqual(
            mirror.filename("some_file"),
            os.path.join(self.mirror_dir, "some_file")
        )

    def test_file_mirror_prepare(self):
        mirror = FileMirror(self.mirror_dir)
        self.assertIs(mirror.prepare(['ar_index_global_meta.txt.gz']), mirror)
        with self.assertRaises(PathsDoNotExistError):
            mirror.prepare(["not a file"])

        # has a slightly different error message
        with self.assertRaises(PathsDoNotExistError):
            mirror.prepare(["not a file"] * 21)
