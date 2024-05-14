from itertools import product

from discretehelpers.sig_perm import SigPerm
from discretehelpers.perm import Perm
from discretehelpers.a import create_hasse_matrix


def test():

    pairs = sorted(product(range(8), range(6)))

    pair_to_inversion_set = dict()

    for pair in pairs:
        sp = SigPerm(pair=pair)
        schoute_sequence = sp.schoute_perm.sequence(8)
        p = Perm(schoute_sequence)
        pair_to_inversion_set[pair] = p.inversion_set

    def is_under(pair_1, pair_2):
        inversion_set_1 = pair_to_inversion_set[pair_1]
        inversion_set_2 = pair_to_inversion_set[pair_2]
        return inversion_set_1.issubset(inversion_set_2)

    def pair_str(pair):
        a, b = pair
        return f"{a}-{b}"

    hasse = create_hasse_matrix(pairs, is_under)

    edges = []

    for i, row in enumerate(hasse):
        for j, entry in enumerate(row):
            if entry:
                a, b = pair_str(pairs[i]), pair_str(pairs[j])
                edges.append((a, b))

    assert edges == [('0-0', '0-1'), ('0-0', '0-2'), ('0-0', '1-0'), ('0-1', '0-3'), ('0-1', '1-1'), ('0-2', '0-4'), ('0-2', '1-2'), ('0-3', '0-5'), ('0-3', '1-3'), ('0-4', '1-4'), ('0-5', '1-5'), ('1-0', '1-2'), ('1-0', '2-1'), ('1-1', '1-3'), ('1-1', '2-0'), ('1-2', '2-4'), ('1-3', '2-5'), ('1-4', '2-2'), ('1-5', '2-3'), ('2-0', '3-0'), ('2-0', '4-2'), ('2-1', '3-1'), ('2-1', '4-3'), ('2-2', '3-2'), ('2-2', '4-0'), ('2-3', '3-3'), ('2-3', '4-1'), ('2-4', '3-4'), ('2-5', '3-5'), ('3-0', '5-2'), ('3-1', '3-0'), ('3-1', '5-3'), ('3-2', '5-0'), ('3-3', '5-1'), ('3-4', '3-2'), ('3-5', '3-3'), ('4-0', '4-1'), ('4-0', '5-0'), ('4-1', '5-1'), ('4-2', '4-4'), ('4-2', '5-2'), ('4-3', '4-5'), ('4-3', '5-3'), ('4-4', '5-4'), ('4-5', '5-5'), ('5-0', '6-1'), ('5-1', '6-0'), ('5-2', '6-4'), ('5-3', '6-5'), ('5-4', '6-2'), ('5-5', '6-3'), ('6-0', '7-0'), ('6-1', '7-1'), ('6-2', '6-0'), ('6-2', '7-2'), ('6-3', '6-1'), ('6-3', '7-3'), ('6-4', '7-4'), ('6-5', '7-5'), ('7-1', '7-0'), ('7-2', '7-0'), ('7-3', '7-1'), ('7-4', '7-2'), ('7-5', '7-3')]
