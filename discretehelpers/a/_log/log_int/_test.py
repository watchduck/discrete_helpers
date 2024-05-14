from discretehelpers.a import log_int as f, abbrev_testing as abbrev
from discretehelpers.ex import ArgValueError


def test_int():

    for i in range(5):
        assert f(2 ** i) == i


def test_raise():

    abbrev(ArgValueError, [
        lambda: f(.5),
        lambda: f(1.5),
        lambda: f(1j),  # complex
        lambda: f(-1),
        lambda: f(0),
        lambda: f(3),
        lambda: f(5)
    ])
