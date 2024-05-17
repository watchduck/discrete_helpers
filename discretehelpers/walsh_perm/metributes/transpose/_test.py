from discretehelpers.walsh_perm import WalshPerm


wp137 = WalshPerm(vector=(1, 3, 7))
wp764 = WalshPerm(vector=(7, 6, 4))


def test():
    assert wp137.transpose == wp764
