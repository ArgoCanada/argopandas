
import unittest
import tempfile
import os

from netCDF4 import Dataset

from argodata.ncfile import NetCDFFile
from argodata.mirror import FileMirror, UrlMirror


class TestNetCDFFile(unittest.TestCase):

    def setUp(self) -> None:
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.mirror = FileMirror(test_dir)

    def test_getitem(self):
        nc = NetCDFFile(None, data={'key': 'value'})
        self.assertEqual(nc['key'], 'value')

    def test_dataset_file(self):
        path = 'dac/csio/2900313/profiles/D2900313_002.nc'

        nc_mirror = NetCDFFile(path, mirror=self.mirror)
        self.assertIsInstance(nc_mirror.dataset(), Dataset)

        nc_abspath = NetCDFFile(os.path.abspath(self.mirror.filename(path)))
        self.assertIsInstance(nc_abspath.dataset(), Dataset)

        nc_relpath = NetCDFFile(self.mirror.filename(path))
        self.assertIsInstance(nc_relpath.dataset(), Dataset)

    def test_dataset_bytes(self):
        path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        with self.mirror.open(path) as f:
            self.assertIsInstance(NetCDFFile(f.read()).dataset(), Dataset)

    def test_dataset_url(self):
        path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        url = 'https://data-argo.ifremer.fr/' + path
        self.assertIsInstance(NetCDFFile(url).dataset(), Dataset)

        mirror = UrlMirror('https://data-argo.ifremer.fr')
        nc_url_mirror = NetCDFFile(path, mirror=mirror)
        self.assertIsInstance(nc_url_mirror.dataset(), Dataset)



if __name__ == '__main__':
    unittest.main()
