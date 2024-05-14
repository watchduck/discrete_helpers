from functools import cached_property


@cached_property
def inverse(self):

    from discretehelpers.sig_perm import SigPerm

    inverse_matrix = self.matrix().transpose()
    result = SigPerm(matrix=inverse_matrix)

    return result
