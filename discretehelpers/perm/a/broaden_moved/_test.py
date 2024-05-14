from discretehelpers.a import abbrev_testing as abbrev

from . import broaden_moved as main, sub


def test_sub():
    assert sub([0, 1], 5, 3) == {0, 1, 5, 6, 10, 11}
    assert sub([1, 2, 3], 1000, 5) == {1, 2, 3, 4001, 4002, 4003, 1001, 1002, 1003, 2001, 2002, 2003, 3001, 3002, 3003}


def test_main():
    assert main(3, 5, [0, 1], [0, 1]) == (15, {0, 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13})
    assert main(6, 15, [0, 1], [12, 13, 14]) == (30, {0, 1, 6, 7, 12, 13, 14, 18, 19, 24, 25, 27, 28, 29})
