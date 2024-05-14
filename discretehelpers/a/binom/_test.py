from . import binom


def test_4():
    row = [1, 4, 6, 4, 1]
    for k in range(5):
        assert binom(4, k) == row[k]


def test_5():
    row = [1, 5, 10, 10, 5, 1]
    for k in range(6):
        assert binom(5, k) == row[k]
