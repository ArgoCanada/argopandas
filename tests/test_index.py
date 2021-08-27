
import os
import unittest
import pandas as pd
import argopandas.index as dfi
from argopandas.mirror import FileMirror


class TestDataFrameIndex(unittest.TestCase):

    def setUp(self) -> None:
        this_file = os.path.dirname(__file__)
        mirror_dir = "argo-test-mirror"
        self.mirror = FileMirror(os.path.join(this_file, mirror_dir))

    def test_subset(self):
        df = pd.DataFrame.from_records([{'file': 'csio/2900313/2900313_prof.nc'}])
        df = dfi.DataFrameIndex(df)
        self.assertIsInstance(df[[]], dfi.DataFrameIndex)
        self.assertIsInstance(df.iloc[[], :], dfi.DataFrameIndex)

    def test_info(self):
        df = pd.DataFrame.from_records([{'file': 'csio/2900313/2900313_prof.nc'}])
        df = dfi.DataFrameIndex(df, _mirror=self.mirror)
        self.assertIn('DATA_TYPE', df.info.keys())

    def test_prof(self):
        df = pd.DataFrame.from_records([{'file': 'csio/2900313/profiles/D2900313_002.nc'}])
        df = dfi.ProfIndex(df, _mirror=self.mirror)
        self.assertIn('PRES', df.levels.keys())
        self.assertIn('PLATFORM_NUMBER', df.prof.keys())
        self.assertIn('PARAMETER', df.calib.keys())
        self.assertIn('STATION_PARAMETERS', df.param.keys())
        self.assertIn('HISTORY_DATE', df.history.keys())

    def test_traj(self):
        df = pd.DataFrame.from_records([{'file': 'csio/2900313/2900313_Rtraj.nc'}])
        df = dfi.TrajIndex(df, _mirror=self.mirror)
        self.assertIn('LATITUDE', df.measurement.keys())
        self.assertIn('JULD_DESCENT_START', df.cycle.keys())
        self.assertIn('TRAJECTORY_PARAMETERS', df.param.keys())
        self.assertIn('HISTORY_DATE', df.history.keys())

    def test_tech(self):
        df = pd.DataFrame.from_records([{'file': 'csio/2900313/2900313_tech.nc'}])
        df = dfi.TechIndex(df, _mirror=self.mirror)
        self.assertIn('CYCLE_NUMBER', df.tech_param.keys())

    def test_meta(self):
        df = pd.DataFrame.from_records([{'file': 'csio/2900313/2900313_meta.nc'}])
        df = dfi.MetaIndex(df, _mirror=self.mirror)
        self.assertIn('CONFIG_PARAMETER_VALUE', df.config_param.keys())
        self.assertIn('CONFIG_PARAMETER_NAME', df.config_param.keys())
        self.assertIn('CONFIG_MISSION_NUMBER', df.missions.keys())
        self.assertIn('TRANS_SYSTEM', df.trans_system.keys())
        self.assertIn('POSITIONING_SYSTEM', df.positioning_system.keys())
        self.assertIn('LAUNCH_CONFIG_PARAMETER_NAME', df.launch_config_param.keys())
        self.assertIn('SENSOR', df.sensor.keys())
        self.assertIn('PARAMETER', df.param.keys())

    def test_zero_length(self):
        df = pd.DataFrame({'file': []})
        df = dfi.DataFrameIndex(df)
        self.assertEqual({k: list(v) for k, v in df.info.items()}, {'file': []})

if __name__ == '__main__':
    unittest.main()
