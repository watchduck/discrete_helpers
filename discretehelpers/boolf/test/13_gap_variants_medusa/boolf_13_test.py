from discretehelpers.boolf.examples import medusa
from discretehelpers.boolf.examples.e13_gap_variants_medusa import *


# unchanged shape

def test_kusiga():  # without cell 0
    assert kusiga.splits_overlap_counts == medusa.splits_overlap_counts


def test_nosafu():  # without cell 2
    assert nosafu.splits_overlap_counts == medusa.splits_overlap_counts


# changed shape

def test_rudege():  # without cell 0, 2
    assert rudege.splits_overlap_counts == kusiga.splits_overlap_counts


def test_farofe():  # without cell 3
    assert farofe.splits_overlap_counts == medusa.splits_overlap_counts


def test_niliko():  # without cells 2, 3
    assert niliko.splits_overlap_counts == medusa.splits_overlap_counts


def test_sapigi():  # without cells 0, 2, 4, 6
    assert sapigi.splits_overlap_counts == {(0, 1): 4, (0, 2): 4, (0, 3): 3, (1, 2): 4, (1, 3): 4, (2, 3): 4}  # A and D do not cross.
