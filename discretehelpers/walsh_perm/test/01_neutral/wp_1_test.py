from discretehelpers.walsh_perm import WalshPerm


def test_neutral():
    empty = WalshPerm()

    v0 = WalshPerm([])
    v1 = WalshPerm([1])
    v2 = WalshPerm([1, 2])
    v3 = WalshPerm([1, 2, 4])
    v4 = WalshPerm([1, 2, 4, 8])

    m0 = WalshPerm(matrix=[])
    m1 = WalshPerm(matrix=[[1]])
    m1a = WalshPerm(matrix=[1])
    m2 = WalshPerm(matrix=[[1, 0], [0, 1]])
    m3 = WalshPerm(matrix=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    p0 = WalshPerm(perm=[0])
    p1 = WalshPerm(perm=[0, 1])
    p2 = WalshPerm(perm=[0, 1, 2, 3])
    p3 = WalshPerm(perm=[0, 1, 2, 3, 4, 5, 6, 7])

    assert empty == v0 == v1 == v2 == v3 == v4 == m0 == m1 == m1a == m2 == m3 == p0 == p1 == p2 == p3
    assert empty.mapping == dict()
    assert empty.moved == set()
    assert empty.inverse == empty
