from . import is_natural


def test():
    assert is_natural(0)
    assert is_natural(1)

    assert not is_natural('1')
    assert not is_natural(1.5)
    assert not is_natural(-1)
