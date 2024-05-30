from discretehelpers.perm import Perm

from discretehelpers.a import int_to_perm


def test():

    assert int_to_perm(0) == Perm()

    assert int_to_perm(1) == Perm([1, 0])

    assert int_to_perm(9) == Perm([3, 0, 1, 2])

    assert int_to_perm(119) == Perm([4, 3, 2, 1, 0])

    assert int_to_perm(21686) == Perm([0, 6, 4, 2, 1, 7, 5, 3])
