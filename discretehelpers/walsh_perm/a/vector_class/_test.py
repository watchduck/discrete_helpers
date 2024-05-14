from discretehelpers.a import abbrev_testing as abbrev

from . import Vector
from .ex import *


def test_main():

    a_ = Vector()
    a0 = Vector([])
    a1 = Vector([1])
    a2 = Vector([1, 2])
    a3 = Vector([1, 2, 4])
    a4 = Vector([1, 2, 4, 8])

    for i in range(5):
        assert a_[i] == a0[i] == a1[i] == a2[i] == a3[i] == a4[i] == 2**i

    b = Vector([8, 12, 2, 3])
    b_seq = [8, 12, 2, 3, 16]
    for i in range(5):
        assert b[i] == b_seq[i]

    c = Vector({0: 7, 2: 5})
    c_seq = [7, 2, 5, 8, 16]
    for i in range(5):
        assert c[i] == c_seq[i]

    d = Vector([8, 12, 2, 3, 16, 32])
    assert d.length == 4
    assert d.extend_to_length(4) == (8, 12, 2, 3)
    assert d.extend_to_length(5) == (8, 12, 2, 3, 16)

    e = Vector([7, 6, 4])
    assert e.length == 2  # below the degree, which is 3
    assert e.extend_to_length(2)  # Should never be used this way, but does no harm.


def test_raise():
    abbrev(TypeError, [
        lambda: Vector(123),
        lambda: Vector('123'),
        lambda: Vector([[]]),
        lambda: Vector(['123']),
        lambda: Vector({123: -1}),
        lambda: Vector({-1: 123})
    ])

    abbrev(ExtendedLengthTooSmallError, [
        lambda: Vector([8, 12, 2, 3]).extend_to_length(3)
    ])
