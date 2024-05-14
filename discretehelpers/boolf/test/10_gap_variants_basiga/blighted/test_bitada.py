from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e10_gap_variants_basiga import bitada, bitada_blightless, letters_a_to_h


def test_bitada():
    assert bitada.bloat == SetPartComp([[0, 2]], {(1, 5)})  # a = c; (univ =) b comp f (= empty)
    assert bitada.blight == SetPartComp([[-1, 1], [0, 2]], {(-1, 5)})  # univ = b; a = c; univ (= b) comp f (= empty)

    assert bitada.splits_equality_blocks == [[0, 2], [1, 5], [3], [4], [6], [7]]
    assert bitada.splits_preferred_side == [None, 1, None, None, None, None]

    assert bitada.filtrated_pairs_pretty(letters_a_to_h) == {
        'disjoint': [('A', 'D'), ('A', 'E'), ('A', 'G'), ('A', 'H'), ('C', 'D'), ('C', 'E'), ('C', 'G'), ('C', 'H'), ('E', 'G'), ('E', 'H'), ('G', 'H')],
        'subset': [('E', 'D'), ('G', 'D'), ('H', 'D')],

        'equal': [('A', 'C')],
        '0100': [('B', 'F')],

        '1100': [('A', 'F'), ('C', 'F'), ('D', 'F'), ('E', 'F')],
        '1010': [('F', 'G'), ('F', 'H')],
        '0101': [('B', 'C'), ('B', 'D'), ('B', 'E'), ('B', 'G'), ('B', 'H')],
        '0011': [('A', 'B')],
    }

    assert bitada_blightless == Boolf(fullspots={0, 1, 2, 6, 10, 18}, atomvals=[0, 3, 4, 6, 7])
    assert bitada_blightless.splits == [
        ({1}, {0, 2, 18, 6, 10}),  # a 0 0
        ({18, 2, 10, 6}, {0, 1}),  # d 3 1
        ({6}, {0, 1, 2, 18, 10}),  # e 4 2
        ({10}, {0, 1, 2, 18, 6}),  # g 6 3
        ({18}, {0, 1, 2, 6, 10})   # h 7 4
    ]
    assert bitada_blightless.filtrated_pairs_pretty(['A', 'D', 'E', 'G', 'H']) == {
        'disjoint': [('A', 'D'), ('A', 'E'), ('A', 'G'), ('A', 'H'), ('E', 'G'), ('E', 'H'), ('G', 'H')],
        'subset': [('E', 'D'), ('G', 'D'), ('H', 'D')]
    }
