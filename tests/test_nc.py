
import unittest
import os

from netCDF4 import Dataset, Variable

from argodata.nc import NetCDFFile


class TestNetCDFFile(unittest.TestCase):

    def setUp(self) -> None:
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.test_path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        self.test_file = os.path.join(test_dir, self.test_path)

    def test_dataset_file(self):
        nc_abspath = NetCDFFile(os.path.abspath(self.test_file))
        self.assertIsInstance(nc_abspath.dataset(), Dataset)

        nc_relpath = NetCDFFile(self.test_file)
        self.assertIsInstance(nc_relpath.dataset(), Dataset)

    def test_dataset_bytes(self):
        with open(self.test_file, 'rb') as f:
            self.assertIsInstance(NetCDFFile(f.read()).dataset(), Dataset)

    def test_dataset_url(self):
        path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        url = 'https://data-argo.ifremer.fr/' + path
        self.assertIsInstance(NetCDFFile(url).dataset(), Dataset)

    def test_dataset_dataset(self):
        ds = Dataset(self.test_file)
        self.assertIs(NetCDFFile(ds).dataset(), ds)

    def test_getitem(self):
        nc = NetCDFFile(self.test_file)
        self.assertIsInstance(nc['PRES'], Variable)

    def test_ndarray(self):
        import numpy as np
        nc = NetCDFFile(self.test_file)
        self.assertEqual(np.shape(nc._ndarray('PRES')), (1, 70))

    def test_vars_along(self):
        nc = NetCDFFile(self.test_file)
        prof_vars = nc._var_names_along(('N_PROF', ))
        self.assertIn('PLATFORM_NUMBER', prof_vars)
        self.assertIn('CYCLE_NUMBER', prof_vars)

    def test_data_frame_along(self):
        nc = NetCDFFile(self.test_file)
        levels = nc._data_frame_along(('N_PROF', 'N_LEVELS'))
        self.assertSetEqual(
            set(levels.keys()),
            set(nc._var_names_along(('N_PROF', 'N_LEVELS')))
        )

        # zero variables
        self.assertEqual(list(nc._data_frame_along(['not a dim']).keys()), [])

        # scalar dimensions
        self.assertIn('DATA_TYPE', nc._data_frame_along([]).keys())


if __name__ == '__main__':
    unittest.main()
