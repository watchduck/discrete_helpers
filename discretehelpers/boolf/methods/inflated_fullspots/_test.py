from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf import Boolf
from discretehelpers.binv import Binv

from discretehelpers.ex import ArgMismatchError

b_and_d = Boolf('0001', [1, 3])


def test_main():
    assert b_and_d.fullspots == {3}

    atoms = [0, 1, 2, 3]
    tt_0123 = '0000 0000 0011 0011'
    assert b_and_d.tt() == Binv(tt_0123)
    assert b_and_d == Boolf(tt_0123, atoms)
    assert b_and_d.inflated_fullspots(atoms) == {10, 11, 14, 15}

    atoms = [0, 1, 3]
    assert b_and_d == Boolf('0000 0011', atoms)
    assert b_and_d.inflated_fullspots(atoms) == {6, 7}

    atoms = [1, 2, 3]
    tt_123 = '0000 0101'
    assert b_and_d == Boolf(tt_123, atoms)
    assert b_and_d.inflated_fullspots(atoms) == {5, 7}

    atoms = [0, 1, 2, 3, 4]
    assert b_and_d == Boolf(2 * tt_0123, atoms)
    assert b_and_d.inflated_fullspots(atoms) == {10, 11, 14, 15, 26, 27, 30, 31}

    atoms = [1, 2, 3, 4]
    assert b_and_d == Boolf(2 * tt_123, atoms)
    assert b_and_d.inflated_fullspots(atoms) == {5, 7, 13, 15}

    atoms_5 = [1, 2, 3, 4, 5]
    atoms_99 = [1, 2, 3, 4, 99]
    assert b_and_d == Boolf(4 * tt_123, atoms_5) == Boolf(4 * tt_123, atoms_99)
    assert b_and_d.inflated_fullspots(atoms_5) == b_and_d.inflated_fullspots(atoms_99) == {5, 7, 13, 15, 21, 23, 29, 31}


def test_raise():
    abbrev(ArgMismatchError, [
        lambda: b_and_d.inflated_fullspots([0, 1, 2])  # 3 is missing
    ])
