from functools import cached_property

import numpy as np

from discretehelpers.binv import Binv

from discretehelpers.a import true_except, make_atompatterns
from discretehelpers.a import make_linear_binv

from ...ex import InvalidMatrixError


@cached_property
def mapping(self):

    if self.neutral:
        result = dict()
    else:
        atoms = make_atompatterns(self.degree)
        long_matrix = np.zeros([self.degree, self.perilen], dtype=int)
        for m in range(self.degree):
            long_matrix[m, :] = make_linear_binv(self.transpose_vector_object[m], self.degree, prefab_atom_patterns=atoms)
        result = dict()
        sequence = [None] * self.perilen
        for key in range(self.perilen):
            val = Binv(vector=list(long_matrix[:, key])).intval
            sequence[key] = val
            if val != key:
                result[key] = val
        true_except(sorted(sequence) == list(range(self.perilen)), InvalidMatrixError)

    return result
