from discretehelpers.a import true_except

from discretehelpers.boolf.ex import NotPairOfAtomKeysError
from .ex import BordersCrossingError


def atom_border_in_atom_side(self, a, b):

    true_except(a != b and a < self.valency and b < self.valency, NotPairOfAtomKeysError)
    true_except(not self.atom_pair_crossing(a, b), BordersCrossingError)

    return self.atom_pair_subset(a, b) or self.atom_pair_intersect(a, b)
