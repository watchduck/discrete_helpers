import numpy as np

from discretehelpers.a import have, true_except

from discretehelpers.walsh_perm.ex import RequestedDegreeSmallerActualDegreeError


def matrix(self, size=None):

    if not have(size):
        size = self.degree

    true_except(size >= self.degree, RequestedDegreeSmallerActualDegreeError)

    matrix_big = np.eye(size, dtype=int)
    matrix_big[0:self.degree, 0:self.degree] = self.matrix_minimal
    return matrix_big
