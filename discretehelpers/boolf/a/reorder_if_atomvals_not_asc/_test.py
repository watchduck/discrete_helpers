from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.binv import Binv

from . import reorder_if_atomvals_not_asc


def test_no_change():
    vector = Binv('0010')
    atomvals = [3, 4]
    assert reorder_if_atomvals_not_asc(vector, atomvals) == (vector, atomvals)


def test_2():
    assert reorder_if_atomvals_not_asc(Binv('0100'), [1, 0]) == (Binv('0010'), [0, 1])
    assert reorder_if_atomvals_not_asc(Binv('0100'), [5, 2]) == (Binv('0010'), [2, 5])


def test_3():
    assert reorder_if_atomvals_not_asc(Binv('0100 1011'), [2, 0, 1]) == (Binv('0110 0101'), [0, 1, 2])
    assert reorder_if_atomvals_not_asc(Binv('0100 1011'), [5, 1, 3]) == (Binv('0110 0101'), [1, 3, 5])


def test_raise():
    abbrev(ValueError, [
        lambda: reorder_if_atomvals_not_asc([0, 1, 0, 0], [0, 1])  # Binv instead of tuple expected
    ])
