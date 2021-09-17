
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


class TestDataFrameIndexHelpers(unittest.TestCase):

    def setUp(self) -> None:
        # recs = prof_all.iloc[[0, 1000, 100000]].to_records()
        # [{k: r[k] for k in prof_all.columns} for r in recs]
        records = [
            {
                'file': 'aoml/13857/profiles/R13857_001.nc',
                'date': pd.Timestamp('1997-07-29 20:03:00+0000', tz='UTC'),
                'latitude': 0.267,
                'longitude': -16.032,
                'ocean': 'A',
                'profiler_type': 845,
                'institution': 'AO',
                'date_update': pd.Timestamp('2018-10-11 18:05:20+0000', tz='UTC')
            },
            {
                'file': 'aoml/15854/profiles/R15854_030.nc',
                'date': pd.Timestamp('1998-07-01 02:22:54+0000', tz='UTC'),
                'latitude': -5.997,
                'longitude': -9.028,
                'ocean': 'A',
                'profiler_type': 845,
                'institution': 'AO',
                'date_update': pd.Timestamp('2018-10-11 18:11:16+0000', tz='UTC')
            },
            {
                'file': 'aoml/1901499/profiles/D1901499_139.nc',
                'date': pd.Timestamp('2015-03-09 07:39:02+0000', tz='UTC'),
                'latitude': 7.959,
                'longitude': -52.677,
                'ocean': 'A',
                'profiler_type': 851,
                'institution': 'AO',
                'date_update': pd.Timestamp('2018-07-17 10:28:15+0000', tz='UTC')
            }
        ]

        self.index = dfi.DataFrameIndex(pd.DataFrame.from_records(records))

    def test_subset_regex(self):
        self.index.subset_data_mode("realtime")
        self.index.subset_data_mode("delayed")

        self.index.subset_direction("ascending")
        self.index.subset_direction("descending")
        with self.assertRaises(ValueError):
            self.index.subset_direction("squareways")
        
        self.index.subset_float(1901499)

    def test_subset_date(self):
        self.index.subset_date(date_start="2000-01")
        self.index.subset_date(date_end="2000-01")

    def test_subset_radius(self):
        self.index.subset_radius(7, -52, 1000)

    def test_subset_rect_point(self):
        self.index.subset_rect()
        self.index.subset_rect(7, -53, 8, -52)
        # make sure to test backside of the earth

    def test_subset_rect_rect(self):
        pass


if __name__ == '__main__':
    unittest.main()
