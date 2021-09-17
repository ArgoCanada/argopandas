
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
        self.assertEqual(len(self.index.subset_data_mode("realtime")), 2)
        self.assertEqual(len(self.index.subset_data_mode("delayed")), 1)

        self.assertEqual(len(self.index.subset_direction("ascending")), 3)
        self.assertEqual(len(self.index.subset_direction("descending")), 0)
        with self.assertRaises(ValueError):
            self.index.subset_direction("squareways")
        
        self.assertEqual(len(self.index.subset_float(1901499)), 1)

        df_params = pd.DataFrame.from_records([
            {'parameters': 'DOXY PSAL'},
            {'parameters': 'PSAL TEMP'}
        ])
        index_params = dfi.DataFrameIndex(df_params)
        self.assertEqual(len(index_params.subset_parameter('DOXY')), 1)
        self.assertEqual(len(index_params.subset_parameter(['DOXY', 'PSAL'])), 2)
        self.assertEqual(len(index_params.subset_parameter([])), 0)
        self.assertEqual(len(index_params.subset_parameter('BANANAS')), 0)

    def test_subset_date(self):
        self.assertEqual(len(self.index.subset_date()), 3)
        self.assertEqual(len(self.index.subset_date(date_start="2000-01")), 1)
        self.assertEqual(len(self.index.subset_date(date_end="2000-01")), 2)
        self.assertEqual(len(self.index.subset_date("1997-01", "1997-12")), 1)

        self.assertEqual(len(self.index.subset_updated()), 3)
        self.assertEqual(len(self.index.subset_updated(date_start="2018-09")), 2)
        self.assertEqual(len(self.index.subset_updated(date_end="2018-09")), 1)
        self.assertEqual(len(self.index.subset_updated("2018-07-01", "2018-07-31")), 1)

    def test_subset_radius(self):
        self.assertEqual(len(self.index.subset_radius(7, -52, 1000)), 1)

    def test_subset_rect_point(self):
        self.assertEqual(len(self.index.subset_rect()), 3)
        self.assertEqual(len(self.index.subset_rect(7, -53, 8, -52)), 1)

        # test across the dateline
        r_dl = {'latitude_min': -10, 'latitude_max': 12, 'longitude_min': 178, 'longitude_max': -179}
        df_dateline = pd.DataFrame.from_records([
            {'longitude': -179.5, 'latitude': 0},
            {'longitude': 178.5, 'latitude': 0},
            {'longitude': 0, 'latitude': 0}
        ])
        index_dateline = dfi.DataFrameIndex(df_dateline)
        self.assertEqual(len(index_dateline.subset_rect()), 3)
        self.assertEqual(len(index_dateline.subset_rect(**r_dl)), 2)
        
    def test_subset_rect_rect(self):
        # test normal rect
        r_norm = {'latitude_min': -10, 'latitude_max': 12, 'longitude_min': -10, 'longitude_max': 11}
        r_norm_int = {'latitude_min': -1, 'latitude_max': 1, 'longitude_min': -1, 'longitude_max': 1}
        r_norm_noint = {'latitude_min': -1, 'latitude_max': 1, 'longitude_min': 12, 'longitude_max': 13}
        df = pd.DataFrame(r_norm, index=[1])
        index = dfi.DataFrameIndex(df)
        self.assertEqual(len(index.subset_rect()), 1)
        self.assertEqual(len(index.subset_rect(**r_norm_int)), 1)
        self.assertEqual(len(index.subset_rect(**r_norm_noint)), 0)

        # test across the dateline
        r_dl = {'latitude_min': -10, 'latitude_max': 12, 'longitude_min': 178, 'longitude_max': -179}
        r_int = {'latitude_min': -1, 'latitude_max': 1, 'longitude_min': -179.5, 'longitude_max': -179}
        r_int2 = {'latitude_min': -1, 'latitude_max': 1, 'longitude_min': 179, 'longitude_max': 179.5}
        r_noint = {'latitude_min': -1, 'latitude_max': 1, 'longitude_min': -1, 'longitude_max': 1}

        df_dateline = pd.DataFrame(r_dl, index=[1])
        index_dateline = dfi.DataFrameIndex(df_dateline)
        self.assertEqual(len(index_dateline.subset_rect()), 1)
        self.assertEqual(len(index_dateline.subset_rect(**r_int)), 1)
        self.assertEqual(len(index_dateline.subset_rect(**r_int2)), 1)
        self.assertEqual(len(index_dateline.subset_rect(**r_noint)), 0)
    
    def test_subset_rect_error(self):
        with self.assertRaises(ValueError):
            dfi.DataFrameIndex({'none of the right cols': []}).subset_rect()


if __name__ == '__main__':
    unittest.main()
