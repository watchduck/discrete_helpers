from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e10_gap_variants_basiga import geteso, geteso_bloatless


def test_geteso():
    assert geteso.bloat == SetPartComp([[6, 7]], {(0, 1)})
    assert geteso.blight == SetPartComp([[6, 7]], {(0, 1)})

    assert geteso.splits_equality_blocks == [[0, 1], [2], [3], [4], [5], [6, 7]]
    assert geteso.splits_preferred_side == [1, None, None, None, None, None]

    assert geteso_bloatless == Boolf(fullspots={1, 2, 3, 37, 15, 21}, atomvals=[1, 2, 3, 4, 5, 6])
    assert geteso_bloatless.splits == [
        ({1, 3, 37, 21, 15}, {2}),  # b 1 0
        ({2, 3, 15}, {1, 37, 21}),  # c 2 1
        ({37, 21, 15}, {1, 2, 3}),  # d 3 2
        ({15}, {1, 2, 3, 37, 21}),  # e 4 3
        ({21}, {1, 2, 3, 37, 15}),  # f 5 4
        ({37}, {1, 2, 3, 21, 15})   # g 6 5
    ]
    assert geteso_bloatless.filtrated_pairs_pretty(['B', 'C', 'D', 'E', 'F', 'G']) == {
        'crossing': [('C', 'D')],
        'disjoint': [('C', 'F'), ('C', 'G'), ('E', 'F'), ('E', 'G'), ('F', 'G')],
        'universal': [('B', 'C')],
        'subset': [('D', 'B'), ('E', 'B'), ('E', 'C'), ('E', 'D'), ('F', 'B'), ('F', 'D'), ('G', 'B'), ('G', 'D')]
    }
