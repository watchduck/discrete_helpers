from discretehelpers.perm import Perm


def test_compare_to_finite():

    fini = Perm([[0, 3]])
    peri = Perm([[0, 3]], 10)
    sequence_10 = [3, 1, 2, 0, 4, 5, 6, 7, 8, 9]

    assert fini.sequence() == fini.sequence(4) == [3, 1, 2, 0]
    assert fini.sequence(10) == peri.sequence(10) == sequence_10
    assert fini.sequence(20) == sequence_10 + list(range(10, 20))
    assert peri.sequence(20) == sequence_10 + [_ + 10 for _ in sequence_10]


def test_reduce_period():
    assert Perm([1, 0, 3, 2, 5, 4, 7, 6], 8) == Perm([1, 0, 3, 2, 5, 4], 6) == Perm([1, 0, 3, 2], 4) == Perm([1, 0], 2)
    assert Perm([1, 2, 3, 0, 5, 6, 7, 4], 8) == Perm([1, 2, 3, 0], 4)


