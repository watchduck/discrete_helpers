import pytest

from discretehelpers.set_part import SetPart

from discretehelpers.boolf.examples.e09_gap_variants_grids import *


unchanged_55 = [medina, gunumi, deginu]
unchanged_54 = [manila, nafega, takeli, tevoga, luvati]


def test_bundle_overlap_counts():
    # Boolfs with the same Euler shape have the same `bundle_overlap_counts`.

    for boolf in unchanged_55:
        assert boolf.bundle_overlap_counts == {
            (0, 1, 2, 3, 4, 5, 6, 7): {
                3: [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)],
                4: [(0, 4), (0, 5), (0, 6), (0, 7), (1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7)]
            }
        }

    for boolf in unchanged_54:
        assert boolf.bundle_overlap_counts == {
            (0, 1, 2, 3, 4, 5, 6): {
                3: [(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)],
                4: [(0, 3), (0, 4), (0, 5), (0, 6), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6)]
            }
        }


@pytest.mark.parametrize('boolf', unchanged_55)
def test_many_55(boolf):
    assert boolf.splits_overlap_counts == {(0, 1): 3, (0, 2): 3, (0, 3): 3, (0, 4): 4, (0, 5): 4, (0, 6): 4, (0, 7): 4, (1, 2): 3, (1, 3): 3, (1, 4): 4, (1, 5): 4, (1, 6): 4, (1, 7): 4, (2, 3): 3, (2, 4): 4, (2, 5): 4, (2, 6): 4, (2, 7): 4, (3, 4): 4, (3, 5): 4, (3, 6): 4, (3, 7): 4, (4, 5): 3, (4, 6): 3, (4, 7): 3, (5, 6): 3, (5, 7): 3, (6, 7): 3}
    assert boolf.bundles == [[0, 1, 2, 3, 4, 5, 6, 7]]
    assert boolf.bundle_grid_partitions == {
        (0, 1, 2, 3, 4, 5, 6, 7): SetPart([[0, 1, 2, 3], [4, 5, 6, 7]])  # [a, b, c, d], [e, f, g, h]
    }


@pytest.mark.parametrize('boolf', unchanged_54)
def test_many_54(boolf):
    assert boolf.splits_overlap_counts == {(0, 1): 3, (0, 2): 3, (0, 3): 4, (0, 4): 4, (0, 5): 4, (0, 6): 4, (1, 2): 3, (1, 3): 4, (1, 4): 4, (1, 5): 4, (1, 6): 4, (2, 3): 4, (2, 4): 4, (2, 5): 4, (2, 6): 4, (3, 4): 3, (3, 5): 3, (3, 6): 3, (4, 5): 3, (4, 6): 3, (5, 6): 3}
    assert boolf.atomvals == [0, 1, 3, 4, 5, 6, 7]  # missing 2
    assert boolf.bloatless_atomkeys_undeflated == [0, 1, 2, 3, 4, 5, 6]  # missing 7
    assert boolf.bundles == [[0, 1, 2, 3, 4, 5, 6]]
    assert boolf.bundle_grid_partitions == {
        (0, 1, 2, 3, 4, 5, 6): SetPart([[0, 1, 2], [3, 4, 5, 6]])
    }
