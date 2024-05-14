from . import logic_abs, logic_abs_vector


def test_int():
    assert logic_abs(0) == logic_abs(~0) == 0
    assert logic_abs(1) == logic_abs(~1) == 1
    assert logic_abs(2) == logic_abs(~2) == 2


def test_vector():
    assert logic_abs_vector([3, ~1, 0, 99]) == logic_abs_vector([~3, 1, ~0, ~99]) == [3, 1, 0, 99]
    assert logic_abs_vector([]) == []
