import pytest

import numpy as np

from discretehelpers.binv import Binv
from discretehelpers.perm import Perm

from . import SigPerm


def test_3():

    matrix3 = [[ 0,  1,  0],
               [ 0,  0, -1],
               [-1,  0,  0]]
    matrix5 = np.eye(5)
    matrix5[0:3, 0:3] = matrix3

    a = SigPerm(valneg=[0, 1, 1], perm=[2, 0, 1])
    a2 = SigPerm(valneg=Binv(intval=6), perm=[2, 0, 1, 3, 4])
    a3 = SigPerm(valneg={1, 2}, perm=[2, 0, 1, 3, 4, 5])
    a4 = SigPerm(pair=(6, 3))
    a5 = SigPerm(keyneg=[1, 0, 1], perm=[2, 0, 1, 3, 4])
    a6 = SigPerm(keyneg_index=5, perm_index=3)
    b = SigPerm(sequence=[~2, 0, ~1])
    b2 = SigPerm(sequence=(~2, 0, ~1, 3, 4))
    b3 = SigPerm(matrix=matrix3)

    assert a == a2 == a3 == a4 == a5 == a6 == b == b2 == b3

    assert a.binv == Binv('011')
    assert a.perm == Perm([2, 0, 1])
    assert a.pair == (6, 3)

    assert a.sequence() == a.sequence(3) == [~2, 0, ~1] == [-3, 0, -2]
    assert a.sequence_string() == a.sequence_string(3) == '[~2, 0, ~1]'
    assert np.array_equal(a.matrix(), np.array(matrix3))

    assert a.sequence(5) == [~2, 0, ~1, 3, 4]
    assert a.sequence_string(5) == '[~2, 0, ~1, 3, 4]'
    assert np.array_equal(a.matrix(5), matrix5)

    assert a.inverse == SigPerm(sequence=[1, ~2, ~0])

    vector = [900, 911, 922, 933]
    assert np.array_equal(
        np.dot(a.matrix(4), vector),
        [911, -922, -900, 933]  # minus instead of negation
    )
    assert np.array_equal(
        a.apply_on_vector(vector),
        [911, ~922, ~900, 933]
    )


def test_4():

    matrix4 = [
        [ 0,  0, -1,  0],
        [ 0, -1,  0,  0],
        [ 0,  0,  0,  1],
        [ 1,  0,  0,  0]
    ]
    matrix6 = np.eye(6)
    matrix6[0:4, 0:4] = matrix4

    a = SigPerm(valneg=[1, 1, 0, 0], perm=[3, 1, 0, 2])
    a2 = SigPerm(valneg=Binv(intval=3), perm=[3, 1, 0, 2, 4, 5])
    a3 = SigPerm(valneg={0, 1}, perm=[3, 1, 0, 2, 4, 5, 6])
    a4 = SigPerm(pair=(3, 11))
    a5 = SigPerm(keyneg=[0, 1, 1, 0], perm=[3, 1, 0, 2, 4, 5])
    a6 = SigPerm(keyneg={1, 2}, perm=[3, 1, 0, 2, 4, 5])
    a7 = SigPerm(keyneg_index=6, perm_index=11)
    b = SigPerm(sequence=[3, ~1, ~0, 2])
    b2 = SigPerm(sequence=(3, ~1, ~0, 2, 4, 5))
    b3 = SigPerm(matrix=matrix4)

    assert a == a2
    assert a == a3
    assert a == a4
    assert a == a5
    assert a == a6
    assert a == a7
    assert a == a
    assert a == b
    assert a == b2
    assert a == b3

    assert a.binv == Binv('1100')
    assert a.perm == Perm([3, 1, 0, 2])
    assert a.pair == (3, 11)

    assert a.sequence() == a.sequence(4) == [3, ~1, ~0, 2] == [3, -2, -1, 2]
    assert a.sequence_string() == a.sequence_string(4) == '[3, ~1, ~0, 2]'
    assert np.array_equal(a.matrix(), np.array(matrix4))

    assert a.sequence(6) == [3, ~1, ~0, 2, 4, 5]
    assert a.sequence_string(6) == '[3, ~1, ~0, 2, 4, 5]'
    assert a.sequence_string(6, True) == '(3, ~1, ~0, 2, 4, 5)'
    assert np.array_equal(a.matrix(6), matrix6)

    assert a.inverse == SigPerm(sequence=[~2, ~1, 3, 0])

    vector = [900, 911, 922, 933, 944]
    assert np.array_equal(
        np.dot(a.matrix(5), vector),
        [-922, -911,  933,  900,  944]  # minus instead of negation
    )
    assert np.array_equal(
        a.apply_on_vector(vector),
        [~922, ~911,  933,  900,  944]
    )


def test_eq():
    p = Perm([5, 3, 1, 2, 4, 0])
    sp = SigPerm(valneg=[], perm=[5, 3, 1, 2, 4, 0])
    assert sp == p

    sp2 = SigPerm(valneg={3}, perm=[5, 3, 1, 2, 4, 0])
    assert sp2 != p


def test_product():
    sp_6_0 = SigPerm(sequence=[0, ~1, ~2])
    sp_0_3 = SigPerm(sequence=[2, 0, 1])
    sp_6_3 = SigPerm(sequence=[~2, 0, ~1])
    assert sp_6_0 * sp_0_3 == sp_6_3

    assert sp_6_0.schoute_perm == Perm([6, 7, 4, 5, 2, 3, 0, 1], perilen=8)
    assert sp_0_3.schoute_perm == Perm([0, 4, 1, 5, 2, 6, 3, 7], perilen=8)
    assert sp_6_3.schoute_perm == Perm([6, 2, 7, 3, 4, 0, 5, 1], perilen=8)


def test_length():
    perm_a = Perm([3, 2, 0, 1])
    perm_b = Perm([2, 0, 1, 3])
    a = SigPerm(valneg={1, 3}, perm=perm_a)
    b = SigPerm(valneg={3, 9}, perm=perm_b)

    assert a == SigPerm(sequence=[~3, 2, 0, ~1])
    assert a.length == 4

    assert b == SigPerm(sequence=[2, 0, 1, ~3, 4, 5, 6, 7, 8, ~9])
    assert b.length == 10

    assert a * b == SigPerm(sequence=[0, ~3, 2, 1, 4, 5, 6, 7, 8, ~9])
    assert b * a == SigPerm(sequence=[3, 1, 2, ~0, 4, 5, 6, 7, 8, ~9])

    assert (perm_a * perm_b).sequence(4) == [0, 3, 2, 1]
    assert (perm_b * perm_a).sequence(4) == [3, 1, 2, 0]


@pytest.mark.parametrize('pair', [(0, 0), (0, 3), (5, 0), (6, 13)])
def test_pair(pair):
    sig_perm = SigPerm(pair=pair)
    assert sig_perm.pair == pair


def test_apply():
    # This describes the mirror symmetry of the Euler diagram of `niliko`.
    sp = SigPerm(pair=(12, 7))

    applied_on_1001 = sp.apply_on_vector([1, 0, 0, 1])
    assert applied_on_1001 == [0, 1, -2, -1]
    assert [_ % 2 for _ in applied_on_1001] == [0, 1, 0, 1]

    applied_on_0101 = sp.apply_on_vector([0, 1, 0, 1])
    assert applied_on_0101 == [1, 0, -2, -1]
    assert [_ % 2 for _ in applied_on_0101] == [1, 0, 0, 1]

    assert sp.apply_on_natural_number(9) == 10
    assert sp.apply_on_natural_number(10) == 9

    assert sp.apply_on_natural_number(0) == 12
    assert sp.apply_on_natural_number(12) == 0

    assert sp.apply_on_natural_number(8) == 8
    assert sp.apply_on_natural_number(4) == 4
    assert sp.apply_on_natural_number(7) == 7

    # It must also work if the vector length (or the binary vector of the natural number)
    # is longer than the signed permutation (`sp.length`).

    applied_on_10011 = sp.apply_on_vector([1, 0, 0, 1, 1])
    assert applied_on_10011 == [0, 1, -2, -1, 1]
    assert [_ % 2 for _ in applied_on_10011] == [0, 1, 0, 1, 1]

    assert sp.apply_on_natural_number(25) == 26
    assert sp.apply_on_natural_number(26) == 25

    binv = Binv('0111 0001 1110 1000')
    sp = SigPerm(pair=(0, 23))
    assert sp.schoute_perm.apply_on_vector(binv) == Binv('0101 1100 1100 1010')


def test_misc():
    a = SigPerm(keyneg_index=0, perm=[3, 1, 2, 0])
    assert a.sequence_string() == '[3, 1, 2, 0]'
    assert a.perm_index == 21

    b = SigPerm(keyneg_index=1, perm=[3, 1, 2, 0])
    assert b.sequence_string() == '[~3, 1, 2, 0]'
    assert b.keyneg_index == 1
    assert b.valneg_index == 8
    assert b.perm_index == 21
    assert b.pair == (8, 21)

    c = SigPerm(keyneg=[1, 0, 1], perm=[3, 1, 2, 0, 4])
    assert c.sequence_string() == '[~3, 1, ~2, 0]'
    assert c.keyneg_index == 5
    assert c.valneg_index == 12

    d = SigPerm(sequence=[])
    assert d == SigPerm(sequence=[0, 1])
    assert d.binv == Binv('')
    assert d.perm == Perm()
    assert d.length == 0

    e = SigPerm(sequence=[~0])
    assert e == SigPerm(sequence=[~0, 1])
    assert e.binv == Binv('1')
    assert e.perm == Perm()
    assert e.length == 1


def test_no_args():
    from discretehelpers.ex import ArgComboError

    with pytest.raises(ArgComboError):
        SigPerm()  # TO DO: would be nice
