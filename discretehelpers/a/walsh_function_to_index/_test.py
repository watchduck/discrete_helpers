import pytest

from discretehelpers.a import abbrev_testing as abbrev
from .. import make_linear_binv
from . import walsh_function_to_index
from .ex import NotWalshRowError


@pytest.mark.parametrize('index', range(8))
def test_3(index):
    row = make_linear_binv(index, 3)
    assert walsh_function_to_index(row) == index


@pytest.mark.parametrize('index', range(16))
def test_4(index):
    row = make_linear_binv(index, 4)
    assert walsh_function_to_index(row) == index


def test_explicit():
    assert walsh_function_to_index('0') == 0
    assert walsh_function_to_index('00') == 0
    assert walsh_function_to_index('0011 0011') == 2
    assert walsh_function_to_index('0000 1111 1111 0000') == 12


def test_raise():
    abbrev(NotWalshRowError, [
        lambda: walsh_function_to_index('0101 0011')
    ])
