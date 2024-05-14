import pytest

from discretehelpers.a import abbrev_testing as abbrev

from . import to_pretty_string as pretty
from .ex import *


def test_results():
    assert pretty([True]) == '1'
    assert pretty([False, True]) == '01'
    assert pretty('0101') == '0101'
    assert pretty('01010110') == '0101 0110'
    assert pretty('0101000001101111') == pretty(' 0  1 010 0000 1101 1 1 1 ') == '0101 0000 0110 1111'
    assert pretty('01010000011011110101000001101111') == '0101 0000 0110 1111  0101 0000 0110 1111'
    assert pretty('0101000001101111010100000110111101010000011011110101000001101111') == '0101 0000 0110 1111  0101 0000 0110 1111  0101 0000 0110 1111  0101 0000 0110 1111'


def test_error():
    abbrev(PrettyLengthError,[
        lambda: pretty('101'),
        lambda: pretty('01010')
    ])
