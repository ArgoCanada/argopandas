
import re

_re_prof = re.compile(r'^(B|S)?(R|D)([0-9]+)_([0-9]+)(D)?(_aux)?\.nc$')
_re_non_prof = re.compile(r'([0-9]+)_(B|S)?(R|D)?(traj|prof|tech|meta)(_aux)?\.nc')

def _path_info(path):
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


def _path_info_iter(path):
    for p in path:
        yield _path_info(p)


def path_info(path):
    if isinstance(path, str):
        return _path_info(path)
    else:
        return _path_info_iter(path)
