import pytest

from discretehelpers.a import is_error

from .ex import *


def abbrev_testing(expected, values):
    if is_error(expected):
        for value in values:
            with pytest.raises(expected):
                value()
    else:
        for value in values:
            assert value == expected
