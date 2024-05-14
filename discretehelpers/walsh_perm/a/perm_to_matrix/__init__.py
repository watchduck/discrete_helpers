import numpy as np
from math import log

from discretehelpers.binv import Binv
from discretehelpers.perm import Perm
from discretehelpers.a import true_except, is_natural

from discretehelpers.perm.ex import IsNeutralFail
from ...ex import NotEvenPermutationError, InvalidPermError
from .ex import PermLengthError
from discretehelpers.a.walsh_function_to_index.ex import NotWalshRowError


def perm_to_matrix(perm, trust=False):
    from discretehelpers.a import walsh_function_to_index

    if type(perm) == Perm:
        perm = perm.sequence()
    else:
        true_except(sorted(perm) == list(range(len(perm))), NotEvenPermutationError)

    perilen = len(perm)

    log_perilen = log(perilen, 2)  # `perilen` should be a power of two. `degree` is the corresponding exponent.
    true_except(is_natural(log_perilen), PermLengthError)
    degree = int(log_perilen)

    if perm in [[0], [0, 1]]:
        raise IsNeutralFail

    long_matrix = np.zeros([degree, perilen], dtype=int)
    for n in range(perilen):
        long_matrix[:, n] = Binv(intval=perm[n], length=degree).vector

    try:
        transpose_vector_object = []
        for m in range(degree):
            row = long_matrix[m, :]
            row_index = walsh_function_to_index(row, trust=trust)
            transpose_vector_object.append(row_index)
    except NotWalshRowError:
        raise InvalidPermError

    matrix = np.zeros([degree, degree], dtype=int)
    for m in range(degree):
        matrix[m, :] = Binv(intval=transpose_vector_object[m], length=degree).vector

    return matrix
