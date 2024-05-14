from functools import cached_property

from itertools import combinations


@cached_property
def filtrated_pairs(self):

    result = dict()

    atomkey_pairs = combinations(range(self.valency), 2)

    for a, b in atomkey_pairs:
        atomval_pair = [self.atomvals[a], self.atomvals[b]]
        boolf = self.filtrated_boolf(atomval_pair)
        binv = boolf.tt(atomval_pair)
        result[(a, b)] = binv.string

    return result
