from collections import defaultdict

"""
How to convert defaultdict of defaultdicts [of defaultdicts] to dict of dicts [of dicts]?
https://stackoverflow.com/questions/26496831
"""


def default_to_regular_dict(d):
    if isinstance(d, defaultdict):
        d = {k: default_to_regular_dict(v) for k, v in d.items()}
    return d
