"""
This module contains functions that operate on Argo filenames.
These filenames follow specific conventions that can be hard
to remember. This is built-in to the interactive module. The
``path`` argument for all functions in this module can be a string
file path, an iterable of file paths, a ``pandas.Series`` or
a ``pandas.DataFrame`` (whose 'file' column is used as input).

>>> import argopandas as argo
>>> argo.path.info('2902746_tech.nc')
{'type': 'tech', 'modifier': None, 'data_mode': None, 'float': 2902746, 'aux': None}
"""


import re
import warnings
import pandas as pd


# general file regexes
def _re_types(types=('traj', 'prof', 'tech', 'meta')):
    types = '|'.join(types)
    return re.compile(r'([0-9]+)_(B|S)?(R|D)?(' + types + ')(_aux)?\.nc')


_re_prof = re.compile(r'(B|S)?(R|D)([0-9]+)_([0-9]+)(D)?(_aux)?\.nc$')
_re_non_prof = _re_types()

# these are for testing specific bits...faster than parsing an entire
# expression match
_re_descending = re.compile(r'[0-9]{3,4}D\.nc')


def _re_data_mode(data_mode):
    data_mode_chr = data_mode.upper()[0]
    re_prof = data_mode_chr + r'[0-9]+[^/]+$'
    re_not_prof = r'[0-9]+_(B|S)?' + data_mode_chr + r'(traj|prof|tech|meta)\.nc$'
    return re.compile('(' + re_prof + ')|(' + re_not_prof + ')')


def _re_float(float):
    floats = '|'.join(str(int(f)) for f in float)
    return re.compile(r'[^0-9](' + floats + r')[^0-9][^/]*$')


def _info(path):
    match = _re_prof.search(path)
    if match:
        return {
            'type': 'prof',
            'modifier': match.group(1),
            'data_mode': match.group(2),
            'float': int(match.group(3)),
            'cycle': int(match.group(4)),
            'descending': match.group(5),
            'aux': match.group(6)
        }

    match = _re_non_prof.search(path)
    if match:
        return {
            'type': match.group(4),
            'modifier': match.group(2),
            'data_mode': match.group(3),
            'float': int(match.group(1)),
            'aux': match.group(5)
        }

    return {'type': None}


def _info_iter(path):
    for p in path:
        yield _info(p)


def _re_search_iter(path, regex):
    for p in path:
        yield regex.search(p) is not None


def _re_search(path, regex):
    if isinstance(path, str):
        return regex.search(path) is not None
    elif isinstance(path, pd.Series):
        # pandas warns about capture groups here but we don't care
        # (we're using them to group alternation |)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            return path.str.contains(regex.pattern)
    elif isinstance(path, pd.DataFrame):
        return _re_search(path['file'], regex)
    else:
        return _re_search_iter(path, regex)


def info(path):
    """
    Return a dictionary of information that can be obtained
    from the file path. ``pandas.Series`` objects are expanded
    to ``pandas.DataFrame`` s; ``pandas.DataFrame`` objects are
    appended to the output ``pandas.DataFrame``.
    """
    if isinstance(path, str):
        return _info(path)
    elif isinstance(path, pd.Series):
        return pd.DataFrame.from_records(_info_iter(path))
    elif isinstance(path, pd.DataFrame):
        info_df = info(path['file'])
        info_with_file_names = {'file_' + k: v for k,v in info_df.items()}
        return pd.concat([path, pd.DataFrame(info_with_file_names)])
    else:
        return _info_iter(path)


def is_descending(path):
    """
    Return ``True`` if this profile is a descending
    profile.
    """
    return _re_search(path, _re_descending)


def is_float(path, floats):
    """
    Return ``True`` if ``path`` matches one of the floats listed
    in ``floats``.

    :param floats: An integer, string, or iterable of those
        representing the float identifier(s).
    """
    if isinstance(floats, str) or isinstance(floats, int):
        floats = [floats]
    else :
        floats = [str(f) for f in floats]

    return _re_search(path, _re_float(floats))


def is_data_mode(path, data_mode):
    """
    Return ``True`` if  ``path`` is path a to a real-time ('R')
    or delayed ('D') mode file.

    :param data_mode: One of 'R', 'D', 'realtime' or 'delayed'
    """
    return _re_search(path, _re_data_mode(data_mode))


def is_prof(path):
    """
    Return ``True`` if  ``path`` is path to a profile NetCDF
    or ``False`` otherwise.
    """
    re_cycle = _re_prof.pattern
    re_float = _re_types(['prof']).pattern
    re_both = '(' + re_cycle + ')|(' + re_float + ')'
    return _re_search(path, re.compile(re_both))


def is_traj(path):
    """
    Return ``True`` if  ``path`` is path to a traj NetCDF
    or ``False`` otherwise.
    """
    return _re_search(path, _re_types(['traj']))


def is_tech(path):
    """
    Return ``True`` if  ``path`` is path to a tech NetCDF
    or ``False`` otherwise.
    """
    return _re_search(path, _re_types(['tech']))


def is_meta(path):
    """
    Return ``True`` if  ``path`` is path to a meta NetCDF
    or ``False`` otherwise.
    """
    return _re_search(path, _re_types(['meta']))


__all__ = [
    'info', 'is_descending', 'is_float', 'is_data_mode',
    'is_prof', 'is_traj', 'is_tech', 'is_meta'
]
