from discretehelpers.a import abbrev_testing as abbrev

from . import decimal_length, NotNaturalError


def test_assert():

    assert decimal_length(0) == 0       # empty (not 0, because that would be a leading zero)
    assert decimal_length(1) == decimal_length(9) == 1
    assert decimal_length(10) == decimal_length(99) == 2
    assert decimal_length(100) == decimal_length(999) == 3

    abbrev(5, [
        decimal_length(10000),
        decimal_length(12345),
        decimal_length(54321),
        decimal_length(99999)
    ])

def test_raise():

    abbrev(NotNaturalError, [
        lambda: decimal_length(0.5),
        lambda: decimal_length(-1.1),
        lambda: decimal_length('01'),
        lambda: decimal_length(-1)
    ])
