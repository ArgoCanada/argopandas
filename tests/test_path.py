
import unittest
from argopandas.path import path_info

class TestPath(unittest.TestCase):

    def test_path_info(self):
        info = path_info('R2901633_052.nc')
        self.assertEqual(list(path_info(['R2901633_052.nc'])), [info])

    def test_path_prof(self):
        info = path_info('R2901633_052.nc')
        self.assertEqual(info['type'], 'prof')
        self.assertEqual(info['float'], 2901633)
        self.assertEqual(info['cycle'], 52)
        self.assertEqual(info['data_mode'], 'R')
        self.assertIsNone(info['modifier'])
        self.assertIsNone(info['descending'])
        self.assertIsNone(info['aux'])

    def test_path_not_prof(self):
        info = path_info('2900313_Rtraj.nc')
        self.assertEqual(info['type'], 'traj')
        self.assertEqual(info['float'], 2900313)
        self.assertEqual(info['data_mode'], 'R')
        self.assertIsNone(info['modifier'])
        self.assertIsNone(info['aux'])

if __name__ == '__main__':
    unittest.main()
