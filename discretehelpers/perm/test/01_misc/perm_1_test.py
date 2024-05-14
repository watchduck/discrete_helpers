from discretehelpers.perm import Perm


def test_init():

    a = Perm([3, 0, 1, 2, 6, 5, 4])
    b = Perm([3, 0, 1, 2, 6, 5, 4, 7, 8])

    c = Perm([[0, 3, 2, 1], [4, 6]])
    d = Perm([[0, 3, 2, 1], [4, 6], [5], [999]])

    e = Perm([[6, 4], [2, 1, 0, 3]])
    f = Perm([[6, 4], [1, 2, 0, 3]])

    assert a == b == c == d == e
    assert e != f


def test_neutral():

    a = Perm()
    b = Perm([[1], [3]])
    assert a.neutral and b.neutral
    assert a.sequence() == a.cycles == b.sequence() == b.cycles == list()
    assert a.mapping == b.mapping == dict()
    assert a.moved == b.moved == set()
    assert a.order == b.order == 1


def test_features():

    sequence = [1, 2, 3, 0, 6, 5, 4]
    p = Perm(sequence)
    assert p.sequence() == sequence
    assert p.mapping == {0: 1, 1: 2, 2: 3, 3: 0, 4: 6, 6: 4}
    assert p.moved == {0, 1, 2, 3, 4, 6}
    assert p.cycles == [[0, 1, 2, 3], [4, 6]]
    assert p.order == 4
    assert p.inverse == Perm([3, 0, 1, 2, 6, 5, 4])

    sequence = [3, 2, 1, 0]
    p = Perm(sequence)
    assert p.sequence() == sequence
    assert p.mapping == {0: 3, 1: 2, 2: 1, 3: 0}
    assert p.moved == {0, 1, 2, 3}
    assert p.cycles == [[0, 3], [1, 2]]
    assert p.order == 2
    assert p.inverse == p

    cycles = [[0, 5, 4], [1, 7, 2, 8], [3, 6]]
    p = Perm(cycles)
    assert p.cycles == cycles
    assert p.sequence() == [5, 7, 8, 6, 0, 4, 3, 2, 1]
    assert p.mapping == {0: 5, 5: 4, 4: 0, 1: 7, 7: 2, 2: 8, 8: 1, 3: 6, 6: 3}
    assert p.moved == {0, 1, 2, 3, 4, 5, 6, 7, 8}
    assert p.order == 12
    assert p.inverse == Perm([4, 8, 7, 6, 5, 0, 3, 1, 2])


def test_slice():

    seq = [4, 3, 2, 1, 0]
    p_finite = Perm(seq)
    assert p_finite[:] == p_finite[::] == p_finite[:5] == p_finite[0:5] == p_finite[0:5:1] == seq
    p_periodic = Perm(seq, 5)
    assert p_periodic[:] == p_periodic[::] == p_periodic[:5] == p_periodic[0:5] == p_periodic[0:5:1] == seq
    assert p_periodic[:10] == p_periodic[0:10] == p_periodic[0:10:1] == [4, 3, 2, 1, 0, 9, 8, 7, 6, 5]

    neutral = Perm()
    assert neutral[:10] == neutral[0:10] == neutral[0:10:1] == list(range(10))
