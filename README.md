# argopandas

[![Check](https://github.com/ArgoCanada/argopandas/actions/workflows/check.yaml/badge.svg)](https://github.com/ArgoCanada/argopandas/actions/workflows/check.yaml)
[![Codecov test coverage](https://codecov.io/gh/ArgoCanada/argopandas/branch/master/graph/badge.svg)](https://codecov.io/gh/ArgoCanada/argopandas?branch=master)

The goal of argopandas is to provide seamless access to Argo NetCDF files using a pandas `DataFrame`-based interface. It is a Python port of the [argodata package for R](https://github.com/ArgoCanada/argodata). The package is under heavy development and we would love feedback on the interface or anything else about the package!

## Installation

You can install the `argopandas` package using `pip`.

``` bash
pip install git+https://github.com/ArgoCanada/argopandas.git
```

The package depends on `pandas`, `numpy`, and `netCDF4`, which you can install using `pip install pandas numpy netCDF4` or via your favourite Python package management system. The `argopandas` package requires Python 3.6 or later.

## Examples

The intended interface for most usage is contained in the `argopandas.interactive` module. You can import this as `argo` for pretty-looking syntax:


```python
import argopandas.interactive as argo
```

The global indexes are available via `argo.prof`, `argo.meta`, `argo.tech`, and `argo.traj`:


```python
argo.meta[:5]
```




    GlobalIndex([{'date_update': '20181011200014', 'file': 'aoml/13857/13857_meta.nc', 'institution': 'AO', 'profiler_type': '845'}, {'date_update': '20181011200015', 'file': 'aoml/13858/13858_meta.nc', 'institution': 'AO', 'profiler_type': '845'}, {'date_update': '20181011200025', 'file': 'aoml/13859/13859_meta.nc', 'institution': 'AO', 'profiler_type': '845'}, {'date_update': '20181011200016', 'file': 'aoml/15819/15819_meta.nc', 'institution': 'AO', 'profiler_type': '845'}, {'date_update': '20181011200018', 'file': 'aoml/15820/15820_meta.nc', 'institution': 'AO', 'profiler_type': '845'}], mirror=argo.CachedUr...o.ifremer.fr'))



By defaut, downloads are lazily cached from the [Ifremer https mirror](https://data-argo.ifremer.fr). You can use `argo.url_mirror()` or `argo.file_mirror()` with `argo.set_default_mirror()` to point `argopandas` at your favourite copy of Argo.

To get Argo data from one or more NetCDF files, subset the indexes and use one of the table accessors to download, cache, and read variables aligned along common dimensions. The accessor you probably want is the `.levels` accessor from the `argo.prof` index:


```python
argo.prof[:5].levels[['PRES', 'PRES_QC', 'TEMP', 'TEMP_QC']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>PRES</th>
      <th>PRES_QC</th>
      <th>TEMP</th>
      <th>TEMP_QC</th>
    </tr>
    <tr>
      <th>file</th>
      <th>N_PROF</th>
      <th>N_LEVELS</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">aoml/13857/profiles/R13857_001.nc</th>
      <th rowspan="5" valign="top">0</th>
      <th>0</th>
      <td>11.900000</td>
      <td>b'1'</td>
      <td>22.235001</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>1</th>
      <td>17.000000</td>
      <td>b'1'</td>
      <td>21.987000</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22.100000</td>
      <td>b'1'</td>
      <td>21.891001</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27.200001</td>
      <td>b'1'</td>
      <td>21.812000</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32.299999</td>
      <td>b'1'</td>
      <td>21.632000</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">aoml/13857/profiles/R13857_005.nc</th>
      <th rowspan="5" valign="top">0</th>
      <th>102</th>
      <td>976.500000</td>
      <td>b'1'</td>
      <td>4.527000</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>103</th>
      <td>986.700012</td>
      <td>b'1'</td>
      <td>4.527000</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>104</th>
      <td>996.799988</td>
      <td>b'1'</td>
      <td>4.533000</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>105</th>
      <td>1007.000000</td>
      <td>b'1'</td>
      <td>4.487000</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>106</th>
      <td>1017.200012</td>
      <td>b'1'</td>
      <td>4.471000</td>
      <td>b'1'</td>
    </tr>
  </tbody>
</table>
<p>551 rows × 4 columns</p>
</div>



You can get data from every variable in an Argo NetCDF file using one of these accessors. The variables grouped in each are aligned along the same dimensions and are documented together in the Argo user's manual.

- All indexes have a `.info` accessor that contains length-one variables that aren't aligned along any dimensions
- `argo.prof`: `argo.prof.levels`, `arog.prof.prof`, `argo.prof.calib`, `argo.prof.param`, and `argo.prof.history`
- `argo.traj`: `argo.traj.cycle`, `argo.traj.measurement`, `argo.traj.param`, and `argo.traj.history`
- `argo.tech`: `argo.tech.tech_param`
- `argo.meta`: `argo.meta.config_param`, `argo.meta.missions`, `argo.meta.trans_system`, `argo.meta.positioning_system`, `argo.meta.launch_config_param`, `argo.meta.sensor`, and `argo.meta.param`

Once you have a data frame you do anything you'd do with a regular `pd.DataFrame()`, like plot your data using the built-in plot method:


```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for label, df in argo.prof[:5].levels.groupby('file'):
    df.plot(x='TEMP', y = 'PRES', ax=ax, label=label)
ax.invert_yaxis()
```


    
![png](README_files/README_8_0.png)
    

