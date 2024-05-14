from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e10_gap_variants_basiga import duvola, duvola_blightless


def test_duvola():
    assert duvola.bloat == SetPartComp([[0, 2]], {(1, 5), (0, 3)})  # a = c; (univ =) b comp f (= empty); a comp d
    assert duvola.blight == SetPartComp([[-1, 1], [0, 2]], {(0, 3), (-1, 5)})  # univ = b; a = c; a comp d; univ (= b) comp f (= empty)

    assert duvola.splits_equality_blocks == [[0, 2, 3], [1, 5], [4], [6], [7]]
    assert duvola.splits_preferred_side == [0, 1, None, None, None]  # a (= c) is preferred over d; universe b is preferred over empty f

    assert duvola_blightless == Boolf(fullspots={0, 1, 2, 4, 8}, atomvals=[0, 4, 6, 7])
    assert duvola_blightless.splits ==[
        ({1}, {0, 8, 2, 4}),  # a 0 0
        ({2}, {0, 1, 4, 8}),  # e 4 1
        ({4}, {0, 1, 2, 8}),  # g 6 2
        ({8}, {0, 1, 2, 4})   # h 7 3
    ]
    assert duvola_blightless.filtrated_pairs_pretty(['A', 'E', 'G', 'H']) == {
        'disjoint': [('A', 'E'), ('A', 'G'), ('A', 'H'), ('E', 'G'), ('E', 'H'), ('G', 'H')]
    }
