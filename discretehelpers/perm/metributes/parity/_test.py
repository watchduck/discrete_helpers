from discretehelpers.perm import Perm


def test():
    assert Perm([]).parity == 0
    assert Perm([2, 1, 3, 0]).parity == 0
    assert Perm([3, 0, 1, 2]).parity == 1
