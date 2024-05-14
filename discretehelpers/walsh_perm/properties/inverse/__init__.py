from functools import cached_property

import numpy as np

from discretehelpers.a import is_integer_matrix


@cached_property
def inverse(self):

    from discretehelpers.walsh_perm import WalshPerm

    inv_mat_real = np.linalg.inv(self.matrix_minimal)

    if is_integer_matrix(inv_mat_real):

        inv_mat_binary = np.array([_ % 2 for _ in inv_mat_real])
        result = WalshPerm(matrix=inv_mat_binary, trust=True)

    else:

        from discretehelpers.perm import Perm

        perm = Perm(self.cycles, perilen=self.perilen)
        inv_perm = perm.inverse
        result = WalshPerm(perm=inv_perm, trust=True)

    return result
