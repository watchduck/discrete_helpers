import numpy as np

from discretehelpers.a import true_except, is_power_of_two, atompattern_to_signed_index, log_floor
from discretehelpers.perm import Perm
from discretehelpers.binv import Binv
from discretehelpers.ex import ArgTypeError, ArgValueError


def schoute_to_finite_inverse(perm):

    if type(perm) in [list, tuple]:
        perm = Perm(perm, perilen=len(perm))

    true_except(type(perm) == Perm, ArgTypeError)

    if perm.neutral:
        return []

    long = perm.length
    true_except(is_power_of_two(long), ArgValueError)
    short = log_floor(long)

    long_matrix = np.zeros([short, long], dtype=int)

    for i in range(long):
        long_matrix[:, i] = Binv(intval=perm[i], length=short)

    inverse_sequence = []
    for i in range(short):
        row = long_matrix[i, :]
        atomval, negate = atompattern_to_signed_index(row)
        entry = atomval if not negate else ~atomval
        inverse_sequence.append(entry)

    return inverse_sequence
