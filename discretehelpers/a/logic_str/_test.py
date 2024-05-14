from . import logic_str, logic_str_vector


def test_int():
    assert logic_str(~1) == '~1'
    assert logic_str(~0) == '~0'
    assert logic_str(0) == '0'
    assert logic_str(1) == '1'


def test_vector():
    assert logic_str_vector([~1, ~0, 0, 1]) == '[~1, ~0, 0, 1]'
