"""
Internal tools needed to query the index based on rectangles
and position/radius. Based on tools in argodata:
https://github.com/ArgoCanada/argodata/blob/master/R/utils.R#L54-L165
"""

import warnings
import numpy as np


def geodist_rad(long1, lat1, long2, lat2, R=6371.010):
    delta_long = long2 - long1
    delta_lat = lat2 - lat1
    a = np.sin(delta_lat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(delta_long / 2) ** 2
    c = 2 * np.arcsin(np.minimum(1, np.sqrt(a)))
    return R * c


def geodist_lnglat(xy1, xy2, R=6371.010):
    return geodist_rad(
        xy1['x'] * np.pi / 180, xy1['y'] * np.pi / 180,
        xy2['x'] * np.pi / 180, xy2['y'] * np.pi / 180,
        R=R
    )

def rect_intersects(r1, r2):
    limits = {
        'xmin': np.maximum(r1['xmin'], r2['xmin']),
        'xmax': np.minimum(r1['xmax'], r2['xmax']),
        'ymin': np.maximum(r1['ymin'], r2['ymin']),
        'ymax': np.minimum(r1['ymax'], r2['ymax'])
    }

    return (limits['xmax'] >= limits['xmin']) & (limits['ymax'] >= limits['ymin'])

def rect_contains(r, xy):
    return (xy['x'] >= r['xmin']) & \
        (xy['x'] <= r['xmax']) & \
        (xy['y'] >= r['ymin']) & \
        (xy['y'] <= r['ymax'])


def rect_split_dateline(r):
    is_wrap = r['xmax'] < r['xmin']
    xmin1 = np.asarray(r['xmin']).copy()
    xmin1[is_wrap] = -180
    xmin2 = r['xmin']
    xmax1 = r['xmax']
    xmax2 = np.asarray(r['xmax']).copy()
    xmax2[is_wrap] = 180

    return (
        {'xmin': xmin1, 'ymin': r['ymin'], 'xmax': xmax1, 'ymax': r['ymax']},
        {'xmin': xmin2, 'ymin': r['ymin'], 'xmax': xmax2, 'ymax': r['ymax']}
    )


def normalize_lat(latitude):
    # some latitude values are -99.999 instead of missing
    latitude = np.asfarray(latitude).copy()
    latitude[latitude == -99.999] = np.nan
    return latitude


def normalize_lng(longitude):
    # -999.999 is occasionally used to denote missing in the profile index
    # some longitudes are greater than 180, but we handle that more robustly
    # here.
    with warnings.catch_warnings():
        # Suppress warnings of 'invalid remainder' because we know there are
        # nan values already.
        warnings.simplefilter("ignore")
        
        longitude = np.asfarray(longitude).copy()
        longitude[longitude == -999.999] = np.nan
        longitude_inf = np.isinf(longitude)
        normalized = np.asfarray(((longitude + 180.0) % 360) - 180.0)
        normalized[longitude == 180.0] = 180.0
        normalized[longitude_inf] = longitude[longitude_inf]
        return normalized
