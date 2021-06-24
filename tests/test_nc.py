
import unittest
import os

from netCDF4 import Dataset, Variable

from argodata import nc


class TestNetCDFWrapper(unittest.TestCase):

    def setUp(self) -> None:
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.test_path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        self.test_file = os.path.join(test_dir, self.test_path)

    def test_init(self):
        with self.assertRaises(TypeError):
            nc.NetCDFWrapper(None)

    def test_repr(self):
        self.assertEqual(
            repr(nc.NetCDFWrapper('something')),
            "NetCDFWrapper('something')"
        )

    def test_dataset_file(self):
        nc_abspath = nc.NetCDFWrapper(os.path.abspath(self.test_file))
        self.assertIsInstance(nc_abspath.dataset(), Dataset)

        nc_relpath = nc.NetCDFWrapper(self.test_file)
        self.assertIsInstance(nc_relpath.dataset(), Dataset)

    def test_dataset_bytes(self):
        with open(self.test_file, 'rb') as f:
            self.assertIsInstance(nc.NetCDFWrapper(f.read()).dataset(), Dataset)

    def test_dataset_url(self):
        path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        url = 'https://data-argo.ifremer.fr/' + path
        self.assertIsInstance(nc.NetCDFWrapper(url).dataset(), Dataset)

    def test_dataset_dataset(self):
        ds = Dataset(self.test_file)
        self.assertIs(nc.NetCDFWrapper(ds).dataset(), ds)

    def test_dataset_unknown(self):
        with self.assertRaises(ValueError):
            nc.NetCDFWrapper('this is not anything').dataset()

    def test_getitem(self):
        ncobj = nc.NetCDFWrapper(self.test_file)
        self.assertIsInstance(ncobj['PRES'], Variable)

    def test_ndarray(self):
        import numpy as np
        ncobj = nc.NetCDFWrapper(self.test_file)
        self.assertEqual(np.shape(ncobj._ndarray('PRES')), (1, 70))

    def test_vars_along(self):
        ncobj = nc.NetCDFWrapper(self.test_file)
        prof_vars = ncobj._var_names_along(('N_PROF', ))
        self.assertIn('PLATFORM_NUMBER', prof_vars)
        self.assertIn('CYCLE_NUMBER', prof_vars)

    def test_data_frame_along(self):
        ncobj = nc.NetCDFWrapper(self.test_file)
        levels = ncobj._data_frame_along(('N_PROF', 'N_LEVELS'))
        self.assertSetEqual(
            set(levels.keys()),
            set(ncobj._var_names_along(('N_PROF', 'N_LEVELS')))
        )

        # zero variables
        self.assertEqual(list(ncobj._data_frame_along(['not a dim']).keys()), [])

        # scalar dimensions
        self.assertIn('DATA_TYPE', ncobj._data_frame_along([]).keys())

    def test_tables(self):
        ncobj = nc.NetCDFWrapper(self.test_file)
        self.assertIn('DATA_TYPE', ncobj.info.keys())

class TestProfNetCDF(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.test_path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        self.test_file = os.path.join(test_dir, self.test_path)

    def test_tables(self):
        ncobj = nc.ProfNetCDF(self.test_file)
        self.assertIn('PRES', ncobj.levels.keys())
        self.assertIn('PLATFORM_NUMBER', ncobj.prof.keys())
        self.assertIn('PARAMETER', ncobj.calib.keys())
        self.assertIn('STATION_PARAMETERS', ncobj.param.keys())
        self.assertIn('HISTORY_DATE', ncobj.history.keys())


class TestTrajNetCDF(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.test_path = 'dac/csio/2900313/2900313_Rtraj.nc'
        self.test_file = os.path.join(test_dir, self.test_path)

    def test_tables(self):
        ncobj = nc.TrajNetCDF(self.test_file)
        self.assertIn('LATITUDE', ncobj.measurement.keys())
        self.assertIn('JULD_DESCENT_START', ncobj.cycle.keys())
        self.assertIn('TRAJECTORY_PARAMETERS', ncobj.param.keys())
        self.assertIn('HISTORY_DATE', ncobj.history.keys())


class TestTechNetCDF(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.test_path = 'dac/csio/2900313/2900313_tech.nc'
        self.test_file = os.path.join(test_dir, self.test_path)

    def test_tables(self):
        ncobj = nc.TechNetCDF(self.test_file)
        self.assertIn('CYCLE_NUMBER', ncobj.tech_param.keys())

if __name__ == '__main__':
    unittest.main()
