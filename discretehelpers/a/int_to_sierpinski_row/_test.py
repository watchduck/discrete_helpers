import pytest

from discretehelpers.a import abbrev_testing as abbrev

from . import int_to_sierpinski_row as f
from .ex import *
from discretehelpers.ex import ArgComboError


# Both tests below show the same results (which all correspond to rows in the example image).
# The exposet are exponents. The corresponding powers of 2 sum up to the respective integer.

def test_intval():
    assert f(0) == [0]
    assert f(1) == [0, 1]
    assert f(2) == [0, 2]
    assert f(3) == [0, 1, 2, 3]
    assert f(4) == [0, 4]
    assert f(5) == [0, 1, 4, 5]
    assert f(6) == [0, 2, 4, 6]
    assert f(7) == list(range(8))

    assert f(11) == [0, 1, 2, 3, 8, 9, 10, 11]
    assert f(15) == list(range(16))
    assert f(18) == [0, 2, 16, 18]


def test_exposet():
    assert f(exposet=set()) == [0]
    assert f(exposet={0}) == [0, 1]
    assert f(exposet={1}) == [0, 2]
    assert f(exposet={0, 1}) == [0, 1, 2, 3]
    assert f(exposet={2}) == [0, 4]
    assert f(exposet={0, 2}) == [0, 1, 4, 5]
    assert f(exposet={1, 2}) == [0, 2, 4, 6]
    assert f(exposet={0, 1, 2}) == list(range(8))

    assert f(exposet={0, 1, 3}) == [0, 1, 2, 3, 8, 9, 10, 11]
    assert f(exposet={0, 1, 2, 3}) == list(range(16))
    assert f(exposet={1, 4}) == [0, 2, 16, 18]


def test_raise():
    abbrev(NotNaturalError, [
        lambda: f('123'),
        lambda: f(123.45),
        lambda: f([123]),
        lambda: f(-1)
    ])
    abbrev(ArgComboError, [
        lambda: f()
    ])
