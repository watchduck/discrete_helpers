from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e10_gap_variants_basiga import futare, futare_bloatless as bloatless, letters_a_to_h


def test_futare():
    assert futare.bloat == futare.blight == SetPartComp([[0, 2]], {(0, 3), (1, 4)})  # a = c; a comp d; b comp e

    assert futare.splits_equality_blocks == [[0, 2, 3], [1, 4], [5], [6], [7]]
    assert futare.splits_preferred_side == [0, 1, None, None, None]

    assert futare.filtrated_pairs_pretty(letters_a_to_h) == {
        'disjoint': [('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('C', 'E'), ('C', 'F'), ('C', 'G'), ('C', 'H'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'H')],
        'universal': [('B', 'D')],
        'subset': [('A', 'B'), ('C', 'B'), ('E', 'D'), ('F', 'B'), ('F', 'D'), ('F', 'G'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D'), ('H', 'G')],

        'complementary': [('A', 'D'), ('B', 'E'), ('C', 'D')],
        'equal': [('A', 'C')]
    }

    # bloatless default (B instead of E)
    assert bloatless == Boolf(fullspots={0, 3, 14, 26}, atomvals=[0, 1, 5, 6, 7])  # a, b, f, g, h
    assert bloatless.splits == [
        ({3}, {0, 26, 14}),  # a 0 0
        ({26, 3, 14}, {0}),  # b 1 1
        ({14}, {0, 26, 3}),  # f 5 2
        ({26, 14}, {0, 3}),  # g 6 3
        ({26}, {0, 3, 14})   # h 7 4
    ]
    assert bloatless.filtrated_pairs_pretty(['A', 'B', 'F', 'G', 'H']) == {
        'disjoint': [('A', 'F'), ('A', 'G'), ('A', 'H'), ('F', 'H')],
        'subset': [('A', 'B'), ('F', 'B'), ('F', 'G'), ('G', 'B'), ('H', 'B'), ('H', 'G')]
    }

    # bloatless alternative (E instead of B)
    filtrated = futare.filtrated_boolf([0, 4, 5, 6, 7])
    assert filtrated == filtrated.bloatless_boolf
    assert filtrated.splits == [
        ({1}, {24, 2, 12}),  # a 0 0
        ({2}, {24, 1, 12}),  # e 4 1
        ({12}, {24, 1, 2}),  # f 5 2
        ({24, 12}, {1, 2}),  # g 6 3
        ({24}, {1, 2, 12})   # h 7 4
    ]
    assert filtrated.filtrated_pairs_pretty(['A', 'E', 'F', 'G', 'H']) == {
        'disjoint': [('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'H')],
        'subset': [('F', 'G'), ('H', 'G')]
    }
