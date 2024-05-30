from discretehelpers.perm import Perm
from discretehelpers.a import is_natural, true_except, int_to_factoradic
from discretehelpers.perm.a import left_inversion_count_to_permutation


def int_to_perm(n):

    true_except(is_natural(n), ValueError)

    left = int_to_factoradic(n)

    perm_sequence = left_inversion_count_to_permutation(left)

    return Perm(perm_sequence)
