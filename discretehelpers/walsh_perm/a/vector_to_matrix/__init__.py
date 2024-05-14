import numpy as np

from discretehelpers.binv import Binv

from discretehelpers.perm.ex import IsNeutralFail
from .ex import *


def vector_to_matrix(vector):

    if vector in [[], [1]]:
        raise IsNeutralFail

    degree = len(vector)

    matrix = np.zeros([degree, degree], dtype=int)
    for n in range(degree):
        matrix[:, n] = Binv(intval=vector[n], length=degree).vector

    return matrix
