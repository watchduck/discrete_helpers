from functools import cached_property

from discretehelpers.a import true_except
from discretehelpers.boolf.ex import BoolfNotBlightlessError

from .ex import TooManyOverlapsERROR, SmallerThanSelfERROR


@cached_property
def gapless_boolf(self):

    from discretehelpers.boolf import Boolf

    true_except(self.is_blightless, BoolfNotBlightlessError)

    result = Boolf('1')

    for a, b in self.split_pairs_with_3_overlaps:
        
        atomval_a, atomval_b = self.atomvals[a], self.atomvals[b]

        set_a, set_b = self.splits[a][0], self.splits[b][0]
        comp_a, comp_b = self.splits[a][1], self.splits[b][1]

        if intersection_empty(comp_a, comp_b):
            result &= Boolf('0111', [atomval_a, atomval_b])
        elif intersection_empty(set_a, comp_b):
            result &= Boolf('1011', [atomval_a, atomval_b])
        elif intersection_empty(comp_a, set_b):
            result &= Boolf('1101', [atomval_a, atomval_b])
        elif intersection_empty(set_a, set_b):
            result &= Boolf('1110', [atomval_a, atomval_b])
        else:
            raise TooManyOverlapsERROR

    true_except(result.bitwise_ge(self), SmallerThanSelfERROR)

    self.gapless_boolf = result
    return result


def intersection_empty(x, y):
    return len(x.intersection(y)) == 0
