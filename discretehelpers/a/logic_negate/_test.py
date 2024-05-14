from discretehelpers.a import abbrev_testing as abbrev

from . import logic_negate, logic_negate_vector


def test_int():
    assert logic_negate(~1) == logic_negate(~1, True) == logic_negate( 1, False) == 1
    assert logic_negate(~0) == logic_negate(~0, True) == logic_negate( 0, False) == 0
    assert logic_negate( 0) == logic_negate( 0, True) == logic_negate(~0, False) == ~0 == -1
    assert logic_negate( 1) == logic_negate( 1, True) == logic_negate(~1, False) == ~1 == -2
    assert logic_negate( 2) == logic_negate( 2, True) == logic_negate(~2, False) == ~2 == -3

    assert logic_negate(~1, want_string=True) == logic_negate( 1, do_it=False, want_string=True) == '1'
    assert logic_negate(~0, want_string=True) == logic_negate( 0, do_it=False, want_string=True) == '0'
    assert logic_negate( 0, want_string=True) == logic_negate(~0, do_it=False, want_string=True) == '~0'
    assert logic_negate( 1, want_string=True) == logic_negate(~1, do_it=False, want_string=True) == '~1'
    assert logic_negate( 2, want_string=True) == logic_negate(~2, do_it=False, want_string=True) == '~2'


def test_vector_where():
    assert logic_negate_vector([0, 1, 2, 3], [0, 0, 1, 1]) \
           == logic_negate_vector(values=[0, 1, 2, 3], where=[0, 0, 1, 1]) \
           == [0, 1, ~2, ~3]
    assert logic_negate_vector([11, 22, ~33, ~44], [0, 1, 0, 1]) == [11, ~22, ~33, 44]

    assert logic_negate_vector([11, 22, ~33, ~44], [0, 1, 0, 1], want_string=True) == '[11, ~22, ~33, 44]'


def test_vector_which():
    assert logic_negate_vector(values=[0, 1, 2, 3], which=[2, 3]) == [0, 1, ~2, ~3]
    assert logic_negate_vector(values=[0, ~1, 2, ~3], which=[2, 3]) == [0, ~1, ~2, 3]
    assert logic_negate_vector([11, 22, ~33, ~44], which={22, 44}) == [11, ~22, ~33, 44]

    assert logic_negate_vector([11, 22, ~33, ~44], which={22, 44}, want_string=True) == '[11, ~22, ~33, 44]'
