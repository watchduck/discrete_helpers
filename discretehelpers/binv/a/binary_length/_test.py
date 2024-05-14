from discretehelpers.a import abbrev_testing as abbrev

from . import binary_length, NotNaturalError


def test_assert():

    assert binary_length(0) == 0       # empty (not 0, because that would be a leading zero)
    assert binary_length(1) == 1       # 1
    assert binary_length(2) == 2      # 10
    assert binary_length(3) == 2      # 11
    assert binary_length(4) == 3     # 100
    assert binary_length(5) == 3     # 101
    assert binary_length(6) == 3     # 110
    assert binary_length(7) == 3     # 111
    assert binary_length(8) == 4    # 1000
    assert binary_length(9) == 4    # 1001

    assert binary_length(15) == 4   # 1111
    assert binary_length(16) == 5  # 10000
    assert binary_length(17) == 5  # 10001


def test_raise():

    abbrev(NotNaturalError, [
        lambda: binary_length(0.5),
        lambda: binary_length(-1.1),
        lambda: binary_length('01'),
        lambda: binary_length(-1),
    ])
