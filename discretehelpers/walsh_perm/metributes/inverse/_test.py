from discretehelpers.walsh_perm import WalshPerm


wp137 = WalshPerm(vector=(1, 3, 7))
wp136 = WalshPerm(vector=(1, 3, 6))


def test():
    assert wp137.inverse == wp136
