from discretehelpers.binv import Binv

from discretehelpers.a import true_except, have

from .ex import *

"""
Within this file, the original binary expression is called "major" and that of the result "minor". 
(Both are little-endian.)
"""


def bloatless_spotint(self, spotint):

    if self.is_constant:
        return int(self.root[0])

    true_except(spotint < 2 ** self.valency, TooBigError)
    major_binv = Binv(intval=spotint, length=self.valency)

    true_except(self.bloat.int_matches(spotint), BloatMismatchError)

    # map from major to minor places
    map_dict = dict()
    for block_index, block in enumerate(self.splits_equality_blocks):
        for element in block:
            map_dict[element] = block_index  # block exposet are minor places, elements in them are major places

    minor_places_to_do = set(range(self.number_of_distinct_splits))  # multiple major places correspond to same minor place, avoid assigning twice

    minor_exposet = set()  # result will be made from this (use set to avoid preallocating binary vector)

    # copy values from major to minor places
    for major_place in range(major_binv.length):
        minor_place = map_dict[major_place]
        if minor_place in minor_places_to_do:
            pref = self.splits_preferred_side[minor_place]
            used_major_place = pref if have(pref) else major_place
            if major_binv[used_major_place]:  # copy the value from major to minor (by adding the index if true)
                minor_exposet.add(minor_place)

    return Binv(exposet=minor_exposet).intval
