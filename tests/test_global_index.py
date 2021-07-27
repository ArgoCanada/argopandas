
import unittest
from argopandas.global_index import GlobalIndex


class TestGlobalIndex(unittest.TestCase):

    def test_init(self):
        self.assertEqual(
            list(GlobalIndex([{'key': 'something'}])),
            [{'key': 'something'}]
        )

    def test_filter(self):
        self.assertEqual(
            list(GlobalIndex([{'key': 'something'}]).filter(lambda x: False)),
            []
        )

    def test_repr(self):
        self.assertEqual(repr(GlobalIndex([])), 'GlobalIndex([], mirror=None)')


if __name__ == '__main__':
    unittest.main()
