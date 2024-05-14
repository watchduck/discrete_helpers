import pytest

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.perm import Perm

from discretehelpers.perm.ex import LengthTooSmallError, LengthMismatchPerilenError


p_0 = Perm([0, 1, 2, 3])
p_3 = Perm([2, 0, 1, 3])
p_4 = Perm([1, 2, 0, 3])
p_5 = Perm([2, 1, 0, 3])
p_9 = Perm([3, 0, 1, 2])
p_10 = Perm([1, 3, 0, 2])
p_12 = Perm([0, 2, 3, 1])
p_13 = Perm([2, 0, 3, 1])
p_17 = Perm([3, 2, 0, 1])
p_20 = Perm([1, 3, 2, 0])
p_23 = Perm([3, 2, 1, 0])

p_10_powers = {
    -2: p_23,
    -1: p_13,
    0: p_0,
    1: p_10,
    2: p_23,
    3: p_13,
    4: p_0,
    5: p_10,
    6: p_23
}


def test_concat():

    assert p_0 * p_0 == p_0
    assert p_5 * p_5 == p_0

    assert p_0 * p_3 == p_3
    assert p_3 * p_0 == p_3

    assert p_3 * p_9 == p_17
    assert p_9 * p_3 == p_10

    assert p_3 * p_9 * p_5 == p_12
    assert p_5 * p_9 * p_3 == p_20


@pytest.mark.parametrize('n', p_10_powers.keys())
def test_powers(n):
    assert p_10 ** n == p_10_powers[n]


def test_inverse():

    assert p_0.inverse == p_0
    assert p_5.inverse == p_5
    assert p_23.inverse == p_23

    assert p_3.inverse == p_4
    assert p_4.inverse == p_3

    assert p_10.inverse == p_13
    assert p_13.inverse == p_10


def test_sequence():

    assert p_10.sequence() == p_10.sequence(4) == [1, 3, 0, 2]
    assert p_10.sequence(5) == [1, 3, 0, 2, 4]

    abbrev(LengthTooSmallError, [
        lambda: p_10.sequence(3)
    ])
