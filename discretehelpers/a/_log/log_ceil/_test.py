from discretehelpers.a import log_ceil as f, abbrev_testing as abbrev
from discretehelpers.ex import ArgValueError


def test_int():

    assert f(1) == 0

    assert f(2) == 1

    assert f(3) == f(4) == 2

    assert f(5) == f(6) == f(7) == f(8) == 3

    for x in range(9, 17):
        assert f(x) == 4

    for x in range(17, 33):
        assert f(x) == 5


def test_raise():

    abbrev(ArgValueError, [
        lambda: f(.5),
        lambda: f(1.5),
        lambda: f(1j),  # complex
        lambda: f(-1),
        lambda: f(0)
    ])
