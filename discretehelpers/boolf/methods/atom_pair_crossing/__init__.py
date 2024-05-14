from discretehelpers.a import true_except

from discretehelpers.boolf.ex import NotPairOfAtomKeysError


def atom_pair_crossing(self, a, b):

    true_except(a != b and a < self.valency and b < self.valency, NotPairOfAtomKeysError)

    return self.filtrated_pair(a, b) == '1111'
