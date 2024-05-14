import pytest

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf.examples import vumali

from discretehelpers.boolf.ex import NotPairOfAtomKeysError
from .ex import BordersCrossingError


subset_pairs = [
    (5, 1),  # F, B
    (6, 1),  # G, B
    (7, 1),  # H, B

    (5, 3),  # F, D
    (6, 3),  # G, D
    (7, 3),  # H, D

    (7, 6),  # H, G

    (4, 2),  # E, C
    (4, 3),  # E, D
]

true_pairs = subset_pairs + [
    (1, 2),  # B, C
    (2, 1),  # C, B
]


@pytest.mark.parametrize('pair', true_pairs)
def test_true(pair):
    assert vumali.atom_border_in_atom_side(*pair)


@pytest.mark.parametrize('pair', subset_pairs)
def test_false_supersets(pair):
    a, b = pair
    assert not vumali.atom_border_in_atom_side(b, a)


def test_false_disjoint():
    assert not vumali.atom_border_in_atom_side(0, 3)  # A, D
    assert not vumali.atom_border_in_atom_side(3, 0)  # D, A
    assert not vumali.atom_border_in_atom_side(2, 5)  # C, F
    assert not vumali.atom_border_in_atom_side(5, 2)  # F, C


def test_raise():
    abbrev(NotPairOfAtomKeysError, [
        lambda: vumali.atom_border_in_atom_side(3, 3),  # equal
        lambda: vumali.atom_border_in_atom_side(7, 8),  # 8 too big
    ])
    abbrev(BordersCrossingError, [
        lambda: vumali.atom_border_in_atom_side(0, 1),  # A, B
        lambda: vumali.atom_border_in_atom_side(5, 6)  # F, G
    ])
