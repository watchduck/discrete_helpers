from discretehelpers.perm import Perm


def test():
    assert Perm([]).inversion_set == set()
    assert Perm([2, 1, 3, 0]).inversion_set == {(0, 1), (2, 3), (0, 3), (1, 3)}
