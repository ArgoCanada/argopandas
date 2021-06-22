
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


if __name__ == '__main__':
    unittest.main()
