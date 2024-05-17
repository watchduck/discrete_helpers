from functools import cached_property


@cached_property
def transpose(self):

    from discretehelpers.walsh_perm import WalshPerm

    result = WalshPerm(vector=self.transpose_vector())

    return result
