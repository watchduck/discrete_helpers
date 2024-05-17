import pytest

from discretehelpers.boolf.examples import bunese, darimi, vumali, sapigi, medusa, farofe, niliko, rudege


def test_bunese():
    assert bunese.atom_to_crossing_atoms == {
        0: [1, 2],  # A: [B, C]
        1: [0, 2],  # B: [A, C]
        2: [0, 1]   # C: [A, B]
    }


def test_darimi():
    assert darimi.atom_to_crossing_atoms == {
        0: [1, 2, 3],  # B: [C, D, E]
        1: [0, 2],     # C: [B, D]
        2: [0, 1],     # D: [B, C]
        3: [0]         # E: [B]
    }


def test_vumali():
    assert vumali.atom_to_crossing_atoms == {
        0: [1, 2],     # A: [B, C]
        1: [0, 3, 4],  # B: [A, D, E]
        2: [0, 3],     # C: [A, D]
        3: [1, 2],     # D: [B, C]
        4: [1],        # E: [B]
        5: [6],        # F: [G]
        6: [5],        # G: [F]
        7: []          # H: []
    }


def test_sapigi():
    assert sapigi.atom_to_crossing_atoms == {
        0: [1, 2],     # A: [B, C]
        1: [0, 2, 3],  # B: [A, C, D]
        2: [0, 1, 3],  # C: [A, B, D]
        3: [1, 2]      # D: [B, C]
    }


medusa_etc = [medusa, farofe, niliko, rudege]


@pytest.mark.parametrize('boolf', medusa_etc)
def test_medusa_etc(boolf):  # false positives
    assert boolf.atom_to_crossing_atoms == {
        0: [1, 2, 3],  # A: [   B, C, D]
        1: [0, 2, 3],  # B: [A,    C, D]
        2: [0, 1, 3],  # C: [A, B,    D]
        3: [0, 1, 2]   # D: [A, B, C   ]
    }
