"""
The root package contains the interface for
argopandas.

Global indexes
--------------

``argopandas.meta``

    The :class:`argopandas.global_index.GlobalMeta` for the current :func:`default_mirror`.

``argopandas.tech``

    The :class:`argopandas.global_index.GlobalTech` for the current :func:`default_mirror`.

``argopandas.prof``

    The :class:`argopandas.global_index.GlobalProf` for the current :func:`default_mirror`.

``argopandas.traj``

    The :class:`argopandas.global_index.GlobalTraj` for the current :func:`default_mirror`.

``argopandas.bio_traj``

    The :class:`argopandas.global_index.GlobalBioTraj` for the current :func:`default_mirror`.

``argopandas.bio_prof``

    The :class:`argopandas.global_index.GlobalBioProf` for the current :func:`default_mirror`.

``argopandas.synthetic_prof``

    The :class:`argopandas.global_index.GlobalSyntheticProf` for the current :func:`default_mirror`.

>>> import argopandas as argo
>>> argo.meta.head(1)
                       file  profiler_type institution               date_update
0  aoml/13857/13857_meta.nc            845          AO 2018-10-11 20:00:14+00:00
>>> argo.tech.head(1)
                       file institution               date_update
0  aoml/13857/13857_tech.nc          AO 2021-04-28 20:03:35+00:00
>>> argo.prof.head(1)
                                file                      date  latitude  longitude ocean  profiler_type institution               date_update
0  aoml/13857/profiles/R13857_001.nc 1997-07-29 20:03:00+00:00     0.267    -16.032     A            845          AO 2018-10-11 18:05:20+00:00
>>> argo.bio_prof.head(1)
                                     file                      date  latitude  ...                       parameters parameter_data_mode               date_update
0  aoml/1900722/profiles/BD1900722_001.nc 2006-10-22 02:16:24+00:00   -40.316  ...  PRES TEMP_DOXY BPHASE_DOXY DOXY                RRRD 2020-03-12 15:32:30+00:00
[1 rows x 10 columns]
>>> argo.synthetic_prof.head(1)
                                     file                      date  latitude  longitude  ... institution           parameters parameter_data_mode               date_update
0  aoml/1900722/profiles/SD1900722_001.nc 2006-10-22 02:16:24+00:00   -40.316     73.389  ...          AO  PRES TEMP PSAL DOXY                DDDD 2020-10-30 13:30:05+00:00
[1 rows x 10 columns]
>>> argo.bio_traj.head(1)
                             file latitude_max latitude_min  ... institution                                         parameters               date_update
0  bodc/3901496/3901496_BRtraj.nc         None         None  ...          BO  PRES C1PHASE_DOXY C2PHASE_DOXY TEMP_DOXY DOXY ... 2021-07-22 15:44:18+00:00
[1 rows x 9 columns]

"""

from . import path
from ._interactive import default_mirror, set_default_mirror, reset, \
    url_mirror, file_mirror, \
    filename, url, float, nc, open, \
    _index_all, _index_hooks
from . import global_index as _global_index

# we need some trickery to get these to work as variables instead of functions
meta: _global_index.GlobalMeta = _index_all['meta']
tech: _global_index.GlobalTech = _index_all['tech']
traj: _global_index.GlobalTraj = _index_all['traj']
prof: _global_index.GlobalProf = _index_all['prof']
bio_traj: _global_index.GlobalBioTraj = _index_all['bio_traj']
bio_prof: _global_index.GlobalBioProf = _index_all['bio_prof']
synthetic_prof: _global_index.GlobalSyntheticProf = _index_all['synthetic_prof'] 


def _redefine_global_indexes(_index_all):
    global meta, tech, traj, prof, bio_prof, bio_traj, synthetic_prof
    meta = _index_all['meta']
    tech = _index_all['tech']
    traj = _index_all['traj']
    prof = _index_all['prof']
    bio_traj = _index_all['bio_traj']
    bio_prof = _index_all['bio_prof']
    synthetic_prof = _index_all['synthetic_prof']


_index_hooks.append(_redefine_global_indexes)

# don't include 'open' in * because it shadows the builtin open()
__all__ = (
    'filename', 'url', 'default_mirror', 'set_default_mirror',
    'file_mirror', 'url_mirror',
    'meta', 'tech', 'traj', 'prof', 'bio_traj', 'bio_prof', 'nc',
    'synthetic_prof', 'path', 'float', 'reset'
)
