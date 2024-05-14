from functools import cached_property

import numpy as np

from discretehelpers.a import make_atompattern


@cached_property
def schoute_perm(self):

    from discretehelpers.binv import Binv
    from discretehelpers.perm import Perm

    minor = self.length
    major = 2 ** self.length

    long_matrix = np.zeros([minor, major], dtype=bool)
    for rownum, signed_int in enumerate(self.inverse.sequence()):
        long_matrix[rownum, :] = make_atompattern(signed_int, minor)

    long_sequence = []
    for colnum in range(major):
        binary_col = long_matrix[:, colnum]
        natural_int = Binv(vector=binary_col).intval
        long_sequence.append(natural_int)

    return Perm(long_sequence, perilen=major)
