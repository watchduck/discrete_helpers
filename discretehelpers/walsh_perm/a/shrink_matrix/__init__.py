import numpy as np

from discretehelpers.a import true_except
from discretehelpers.perm.ex import IsNeutralFail

from .ex import *


def shrink_matrix(matrix):

    matrix = np.array(matrix, dtype=int)  # should be redundant

    true_except(matrix.size > 1, IsNeutralFail)
    true_except(matrix.shape[0] == matrix.shape[1], NotSquareError)

    degree = matrix.shape[0]

    while True:
        if degree < 2:
            raise IsNeutralFail

        last = degree - 1
        if sum(matrix[last, :]) == sum(matrix[:, last]) == int(matrix[last, last]) == 1:
            matrix = matrix[:-1, :-1]
            degree -= 1
        else:
            break

    return matrix, degree
