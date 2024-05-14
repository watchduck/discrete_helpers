from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.ex import ArgTypeError, ArgValueError

from . import logic_abs_increase, logic_abs_increase_vector


def test_int():
    assert logic_abs_increase(~0, 0) == ~0
    assert logic_abs_increase(~0, 1) == ~1

    assert logic_abs_increase(0, 0) == 0
    assert logic_abs_increase(0, 1) == 1

    assert logic_abs_increase(1, 0) == 1
    assert logic_abs_increase(1, 1) == 2

    assert logic_abs_increase(5, 1) == 6
    assert logic_abs_increase(5, -1) == 4
    assert logic_abs_increase(~5, 1) == ~6
    assert logic_abs_increase(~5, -1) == ~4

    assert logic_abs_increase(5, 1, want_string=True) == '6'
    assert logic_abs_increase(5, -1, want_string=True) == '4'
    assert logic_abs_increase(~5, 1, want_string=True) == '~6'
    assert logic_abs_increase(~5, -1, want_string=True) == '~4'


def test_vector():
    assert logic_abs_increase_vector([5, 5, ~5, ~5], [1, -1, 1, -1]) == [6, 4, ~6, ~4]
    assert logic_abs_increase_vector([5, 5, ~5, ~5], [1, -1, 1, -1], want_string=True) == '[6, 4, ~6, ~4]'


def test_except():
    abbrev(ArgTypeError, [
        lambda: logic_abs_increase('5', '-1', 0)
    ])
    abbrev(ArgValueError, [
        lambda: logic_abs_increase(0, -1),
        lambda: logic_abs_increase(~0, -1),
        lambda: logic_abs_increase_vector([1, 2, 3], [1, 2])
    ])