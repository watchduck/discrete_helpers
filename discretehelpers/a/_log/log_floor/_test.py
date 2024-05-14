from discretehelpers.a import log_floor as f, abbrev_testing as abbrev
from discretehelpers.ex import ArgValueError


def test_int():

    assert f(1) == 0

    assert f(2) == f(3) == 1

    assert f(4) == f(5) == f(6) == f(7) == 2

    for x in range(8, 16):
        assert f(x) == 3

    for x in range(16, 32):
        assert f(x) == 4


def test_raise():

    abbrev(ArgValueError, [
        lambda: f(.5),
        lambda: f(1.5),
        lambda: f(1j),  # complex
        lambda: f(-1),
        lambda: f(0)
    ])
