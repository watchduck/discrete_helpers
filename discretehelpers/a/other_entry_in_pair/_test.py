from discretehelpers.a import abbrev_testing as abbrev

from . import other_entry_in_pair
from .ex import *


def test_list():
    pair = [123, 456]
    assert other_entry_in_pair(pair, 123) == 456
    assert other_entry_in_pair(pair, 456) == 123


def test_tuple():
    pair = (123, 456)
    assert other_entry_in_pair(pair, 123) == 456
    assert other_entry_in_pair(pair, 456) == 123


def test_set():
    pair = {123, 456}
    assert other_entry_in_pair(pair, 123) == 456
    assert other_entry_in_pair(pair, 456) == 123


def test_raise():

    abbrev(WrongTypeError, [
        lambda: other_entry_in_pair({1: 2}, 3) == 4
    ])

    abbrev(WrongLengthError, [
        lambda: other_entry_in_pair([1], 2) == 3,
        lambda: other_entry_in_pair([1, 2, 3], 4) == 5
    ])
