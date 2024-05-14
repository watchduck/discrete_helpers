from discretehelpers.a import abbrev_testing as abbrev
from discretehelpers.ex import ArgValueError
from . import make_transposition


def test():

    assert make_transposition(0, 1, 2) == [1, 0]
    assert make_transposition(0, 1, 3) == [1, 0, 2]
    assert make_transposition(0, 3, 4) == [3, 1, 2, 0]

    abbrev(ArgValueError, [
        lambda: make_transposition(1, 1, 2),
        lambda: make_transposition(0, 1, 1)
    ])
