
import shutil
import unittest
import os
import tempfile

from netCDF4 import Dataset, Variable

from argopandas import netcdf as nc


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
        self.assertIsInstance(nc_abspath.dataset, Dataset)

        nc_relpath = nc.NetCDFWrapper(self.test_file)
        self.assertIsInstance(nc_relpath.dataset, Dataset)

    def test_dataset_bytes(self):
        with open(self.test_file, 'rb') as f:
            self.assertIsInstance(nc.NetCDFWrapper(f.read()).dataset, Dataset)

    def test_dataset_url(self):
        path = 'dac/csio/2900313/profiles/D2900313_002.nc'
        url = 'https://data-argo.ifremer.fr/' + path
        self.assertIsInstance(nc.NetCDFWrapper(url).dataset, Dataset)

    def test_dataset_dataset(self):
        ds = Dataset(self.test_file)
        self.assertIs(nc.NetCDFWrapper(ds).dataset, ds)

    def test_dataset_unknown(self):
        with self.assertRaises(ValueError):
            nc.NetCDFWrapper('this is not anything').dataset

    def test_variables(self):
        ncobj = nc.NetCDFWrapper(self.test_file)
        self.assertEqual(list(ncobj.variables), list(ncobj.dataset.variables))

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

        # preselected variables
        levels_temp = ncobj._data_frame_along(('N_PROF', 'N_LEVELS'), vars='TEMP')
        self.assertSetEqual(set(levels_temp.keys()), set(['TEMP']))
        levels_temp2 = ncobj._data_frame_along(('N_PROF', 'N_LEVELS'), vars=['TEMP'])
        self.assertSetEqual(set(levels_temp2.keys()), set(['TEMP']))

    def test_tables(self):
        ncobj = nc.NetCDFWrapper(self.test_file)
        self.assertIn('DATA_TYPE', ncobj.info.keys())

    def test_load(self):
        with tempfile.TemporaryDirectory() as temp:
            # real argo file with a non-argo name
            shutil.copy(self.test_file, os.path.join(temp, 'f1.nc'))
            with nc.load_netcdf(os.path.join(temp, 'f1.nc')) as ds:
                self.assertIsInstance(ds, nc.NetCDFWrapper)

            # not an Argo NetCDF without a filename
            ds = Dataset(os.path.join(temp, 'f2.nc'), mode='w')
            ds.close()

            with open(os.path.join(temp, 'f2.nc'), 'rb') as f:
                with nc.load_netcdf(f.read()) as ds:
                    self.assertIsInstance(ds, nc.NetCDFWrapper)


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

    def test_load(self):
        self.assertIsInstance(nc.load_netcdf(self.test_file), nc.ProfNetCDF)
        ncobj = nc.ProfNetCDF(self.test_file)
        self.assertIsInstance(nc.load_netcdf(ncobj.dataset), nc.ProfNetCDF)


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

    def test_load(self):
        self.assertIsInstance(nc.load_netcdf(self.test_file), nc.TrajNetCDF)
        ncobj = nc.ProfNetCDF(self.test_file)
        self.assertIsInstance(nc.load_netcdf(ncobj.dataset), nc.TrajNetCDF)


class TestTechNetCDF(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.test_path = 'dac/csio/2900313/2900313_tech.nc'
        self.test_file = os.path.join(test_dir, self.test_path)

    def test_tables(self):
        ncobj = nc.TechNetCDF(self.test_file)
        self.assertIn('CYCLE_NUMBER', ncobj.tech_param.keys())

    def test_load(self):
        self.assertIsInstance(nc.load_netcdf(self.test_file), nc.TechNetCDF)
        ncobj = nc.ProfNetCDF(self.test_file)
        self.assertIsInstance(nc.load_netcdf(ncobj.dataset), nc.TechNetCDF)


class TestMetaNetCDF(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(__file__)
        test_dir = os.path.join(this_dir, 'argo-test-mirror')
        self.test_path = 'dac/csio/2900313/2900313_meta.nc'
        self.test_file = os.path.join(test_dir, self.test_path)

    def test_tables(self):
        ncobj = nc.MetaNetCDF(self.test_file)
        self.assertIn('CONFIG_PARAMETER_VALUE', ncobj.config_param.keys())
        self.assertIn('CONFIG_PARAMETER_NAME', ncobj.config_param.keys())
        self.assertIn('CONFIG_MISSION_NUMBER', ncobj.missions.keys())
        self.assertIn('TRANS_SYSTEM', ncobj.trans_system.keys())
        self.assertIn('POSITIONING_SYSTEM', ncobj.positioning_system.keys())
        self.assertIn('LAUNCH_CONFIG_PARAMETER_NAME', ncobj.launch_config_param.keys())
        self.assertIn('SENSOR', ncobj.sensor.keys())
        self.assertIn('PARAMETER', ncobj.param.keys())

    def test_config_param_no_vars(self):
        tech_file_dir = os.path.dirname(self.test_file)
        tech_file = os.path.join(tech_file_dir, '2900313_tech.nc')
        ncobj = nc.MetaNetCDF(tech_file)
        self.assertEqual(tuple(ncobj.config_param.keys()), ())

    def test_load(self):
        self.assertIsInstance(nc.load_netcdf(self.test_file), nc.MetaNetCDF)
        ncobj = nc.ProfNetCDF(self.test_file)
        self.assertIsInstance(nc.load_netcdf(ncobj.dataset), nc.MetaNetCDF)


if __name__ == '__main__':
    unittest.main()
