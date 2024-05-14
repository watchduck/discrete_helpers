from discretehelpers.perm import Perm
from discretehelpers.walsh_perm import WalshPerm
from discretehelpers.a import true_except, sort_together


def reorder_if_atomvals_not_asc(binv, atomvals):

    from discretehelpers.binv import Binv

    true_except(type(binv) == Binv, ValueError)
    vector = binv.vector
    if type(atomvals) == list:
        atomvals = atomvals.copy()

    if atomvals == sorted(atomvals):
        return Binv(vector), atomvals

    asc_integers = list(range(len(atomvals)))
    sorted_atomvals, reordered_integers = sort_together(atomvals, asc_integers)
    fin_perm = Perm(reordered_integers).inverse

    asc_powers = [2 ** i for i in asc_integers]
    bit_perm_vector = fin_perm.apply_on_vector(asc_powers)
    bit_perm = WalshPerm(bit_perm_vector)
    sorted_vector = bit_perm.apply_on_vector(vector)

    return Binv(sorted_vector), sorted_atomvals
