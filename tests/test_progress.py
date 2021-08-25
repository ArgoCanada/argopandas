
import unittest
import io
from argopandas.progress import ProgressBar


class TestProgressBar(unittest.TestCase):

    def test_progressbar_interactive(self):
        f = io.StringIO()
        pb = ProgressBar(10, file=f, init_message='init!', interactive=True)
        with pb:
            self.assertRegex(f.getvalue(), r'^init!\n')
            pb.bump()
            self.assertRegex(f.getvalue(), r'10%\s+$')
            pb.bump(message='msg')
            self.assertRegex(f.getvalue(), r'msg *$')
            pb.bump(message='this is a message that will be truncated')
            self.assertRegex(f.getvalue(), r'\.\.\.$')
            for i in range(7):
                pb.bump(message=str(i))
            self.assertRegex(f.getvalue(), r'100% 6 +$')
        self.assertRegex(f.getvalue(), r'\r +\r$')

        with self.assertRaises(RuntimeError):
            pb.bump()

    def test_progressbar_static(self):
        f = io.StringIO()
        pb = ProgressBar(10, file=f, init_message='init!', interactive=False)
        with pb:
            self.assertRegex(f.getvalue(), r'^init!\n\[ +\]\n $')
            for i in range(10):
                pb.bump(message=str(i))
            self.assertRegex(f.getvalue(), ' =+$')
        self.assertRegex(f.getvalue(), ' =+\n$')

        with self.assertRaises(RuntimeError):
            pb.bump()


if __name__ == '__main__':
    unittest.main()
