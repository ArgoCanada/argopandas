
import unittest
import argopandas.path as path

class TestPath(unittest.TestCase):

    def test_path_info(self):
        info = path.info('R2901633_052.nc')
        self.assertEqual(list(path.info(['R2901633_052.nc'])), [info])

    def test_path_prof(self):
        info = path.info('R2901633_052.nc')
        self.assertEqual(info['type'], 'prof')
        self.assertEqual(info['float'], 2901633)
        self.assertEqual(info['cycle'], 52)
        self.assertEqual(info['data_mode'], 'R')
        self.assertIsNone(info['modifier'])
        self.assertIsNone(info['descending'])
        self.assertIsNone(info['aux'])

    def test_path_not_prof(self):
        info = path.info('2900313_Rtraj.nc')
        self.assertEqual(info['type'], 'traj')
        self.assertEqual(info['float'], 2900313)
        self.assertEqual(info['data_mode'], 'R')
        self.assertIsNone(info['modifier'])
        self.assertIsNone(info['aux'])

    def test_descending(self):
        self.assertTrue(path.is_descending('R2901633_052D.nc'))
        self.assertFalse(path.is_descending('R2901633_052.nc'))
        self.assertEqual([path.is_descending('a')], list(path.is_descending(['a'])))

    def test_is_float(self):
        self.assertTrue(path.is_float('R2901633_052.nc', 2901633))
        self.assertTrue(path.is_float('R2901633_052.nc', '2901633'))
        self.assertTrue(path.is_float('R2901633_052D.nc', [2901633]))

    def test_is_data_mode(self):
        self.assertTrue(path.is_data_mode('R2901633_052.nc', 'r'))
        self.assertTrue(path.is_data_mode('D2901633_052.nc', 'delayed'))

    def test_is_prof(self):
        self.assertTrue(path.is_prof('R2901633_052.nc'))
        self.assertTrue(path.is_prof('2902746_Sprof.nc'))
        self.assertFalse(path.is_prof('2900313_Rtraj.nc'))

    def test_is_traj(self):
        self.assertFalse(path.is_traj('R2901633_052.nc'))
        self.assertTrue(path.is_traj('2900313_Rtraj.nc'))

    def test_is_tech(self):
        self.assertFalse(path.is_tech('R2901633_052.nc'))
        self.assertTrue(path.is_tech('2900313_tech.nc'))

    def test_is_meta(self):
        self.assertFalse(path.is_meta('R2901633_052.nc'))
        self.assertTrue(path.is_meta('2900313_meta.nc'))


if __name__ == '__main__':
    unittest.main()
