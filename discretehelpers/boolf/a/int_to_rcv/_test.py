from discretehelpers.a import abbrev_testing as abbrev

from . import int_to_rcv
from .ex import *


def test_misc():
    assert int_to_rcv(0) == []
    assert int_to_rcv(1) == [1]
    assert int_to_rcv(2) == [1, 1]
    assert int_to_rcv(4) == [1, 1, 1]
    assert int_to_rcv(16) == [1, 1, 1, 1]
    assert int_to_rcv(65536) == [1, 1, 1, 1, 1]

    abbrev(SpecifiedLengthTooShortError, [
        lambda: int_to_rcv(1, 0),
        lambda: int_to_rcv(9, 2)
    ])


def test_1():
    assert int_to_rcv(0, 1) == [0]
    assert int_to_rcv(1, 1) == [1]


def test_2():
    assert int_to_rcv(0, 2) == [0, 0]
    assert int_to_rcv(1, 2) == [1, 0]
    assert int_to_rcv(2, 2) == [1, 1]
    assert int_to_rcv(3, 2) == [2, 1]


def test_3():
    assert int_to_rcv(0, 3) == [0, 0, 0]
    assert int_to_rcv(1, 3) == [1, 0, 0]
    assert int_to_rcv(2, 3) == [1, 1, 0]
    assert int_to_rcv(3, 3) == [2, 1, 0]
    assert int_to_rcv(4, 3) == [1, 1, 1]
    assert int_to_rcv(5, 3) == [2, 1, 1]
    assert int_to_rcv(6, 3) == [2, 2, 1]
    assert int_to_rcv(7, 3) == [3, 2, 1]
    assert int_to_rcv(8, 3) == [1, 2, 1]
    assert int_to_rcv(9, 3) == [2, 2, 1]
    assert int_to_rcv(10, 3) == [2, 3, 1]
    assert int_to_rcv(11, 3) == [3, 3, 1]
    assert int_to_rcv(12, 3) == [2, 3, 2]
    assert int_to_rcv(13, 3) == [3, 3, 2]
    assert int_to_rcv(14, 3) == [3, 4, 2]
    assert int_to_rcv(15, 3) == [4, 4, 2]


def test_4():
    assert int_to_rcv(16) == [1, 1, 1, 1]  # 0000 1000 0000 0000 (index 4)
    assert int_to_rcv(576) == [2, 4, 4, 2]  # 0000 0010 0100 0000 (exposet 6 and 9)
    assert int_to_rcv(65535) == [16, 32, 32, 16]  # 1111 1111 1111 1111 (exposet 0..15)
