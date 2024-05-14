import numpy as np

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.perm import Perm
from discretehelpers.walsh_perm import WalshPerm

from discretehelpers.walsh_perm.ex import NotPowerOfTwoError, RequestedDegreeSmallerActualDegreeError, RedundantParametersError


def test_shorten():

    p = WalshPerm([7, 5, 4])
    p_long = WalshPerm([7, 5, 4, 8])

    p3_sequence = [0, 7, 5, 2, 4, 3, 1, 6]
    p4_sequence = p3_sequence + [_ + 8 for _ in p3_sequence]

    assert p_long == p

    assert p.sequence() == p.sequence(length=8) == p.sequence(degree=3) == p3_sequence
    assert p.sequence(length=16) == p.sequence(degree=4) == p4_sequence

    assert p == Perm(p3_sequence, 8) == Perm(p4_sequence, 16)


def test_multiply():
    a = WalshPerm([8, 12, 2, 3])
    b = WalshPerm([6, 9, 1, 2])
    c = a * b
    assert c.vector(4) == (14, 11, 8, 12)


def test_inverses():
    a = WalshPerm([14, 11, 8, 12])
    b = WalshPerm([15, 9, 12, 4])
    c = a * b
    assert c.vector(4) == (1, 2, 4, 8)


def test_cycles():

    cycles = [[1, 8, 3, 4, 2, 12], [5, 10, 15], [6, 14, 13, 9, 11, 7]]
    vector = [8, 12, 2, 3]
    wp = WalshPerm(vector)
    p = Perm(cycles, 16)

    assert wp.perilen == p.perilen == 16

    assert wp.cycles == p.cycles == cycles == \
           p.cycles_dynamic() == p.cycles_dynamic(16) == \
           wp.cycles_dynamic() == wp.cycles_dynamic(length=16) == wp.cycles_dynamic(degree=4)

    assert p.cycles_dynamic(32) == wp.cycles_dynamic(length=32) == wp.cycles_dynamic(degree=5) == \
        cycles + [[_ + 16 for _ in cycle] for cycle in cycles]

    assert wp.order == p.order == 6
    assert wp == p

    assert WalshPerm([1, 3, 6]).cycles == [[2, 3], [4, 6, 5, 7]]
    assert WalshPerm([2, 1]).cycles == [[1, 2]]
    assert WalshPerm().cycles == []


def test_length():
    p = WalshPerm(vector=(1, 3))

    assert p.sequence(degree=2) == p.sequence(length=4) == [0, 1, 3, 2]
    assert p.sequence(degree=3) == p.sequence(length=8) == [0, 1, 3, 2, 4, 5, 7, 6]

    assert p.cycles_dynamic(degree=2) == p.cycles_dynamic(length=4) == [[2, 3]]
    assert p.cycles_dynamic(degree=3) == p.cycles_dynamic(length=8) == [[2, 3], [6, 7]]

    abbrev(RequestedDegreeSmallerActualDegreeError, [
        lambda: p.sequence(degree=1),
        lambda: p.sequence(length=2),
        lambda: p.cycles_dynamic(degree=1),
        lambda: p.cycles_dynamic(length=2),
    ])

    abbrev(NotPowerOfTwoError, [
        lambda: p.sequence(length=12),
        lambda: p.cycles_dynamic(length=12)
    ])

    abbrev(RedundantParametersError, [
        lambda: p.sequence(degree=2, length=4),
        lambda: p.cycles_dynamic(degree=2, length=4)
    ])


def test_matrices():

    vector_a = (5, 12, 11, 6)
    matrix_a = np.array([[1, 0, 1, 0],
                         [0, 0, 1, 1],
                         [1, 1, 0, 1],
                         [0, 1, 1, 0]])
    wp_a = WalshPerm(matrix=matrix_a)
    cycles_a = [[1, 5, 14], [2, 12, 13, 8, 6, 7], [3, 9], [4, 11, 15]]
    perm_a = Perm(cycles_a, perilen=16)
    assert wp_a.determinant == 3
    assert wp_a.vector() == vector_a
    assert wp_a == perm_a

    vector_b = (7, 11, 13, 14)
    matrix_b = np.array([[1, 1, 1, 0],
                         [1, 1, 0, 1],
                         [1, 0, 1, 1],
                         [0, 1, 1, 1]])
    wp_b = WalshPerm(matrix=matrix_b)
    cycles_b = [[1, 7], [2, 11], [3, 12], [4, 13], [5, 10], [8, 14]]
    perm_b = Perm(cycles_b, perilen=16)
    assert wp_b.determinant == -3
    assert wp_b.vector() == vector_b
    assert wp_b == perm_b

    wp_ab = wp_a * wp_b
    assert wp_ab.vector() == (2, 15, 8, 1)

    wp_ba = wp_b * wp_a
    assert wp_ba.vector() == (10, 3, 2, 6)
