from discretehelpers.boolf import Boolf
from discretehelpers.set_part import SetPart

from discretehelpers.boolf.examples import dukeli


def test():
    assert dukeli.fullspots == {0, 1, 2, 3, 4, 6, 8, 12}
    assert dukeli.splits == [
        ({1, 3}, {0, 2, 4, 6, 8, 12}),  # a 0
        ({2, 3, 6}, {0, 1, 4, 8, 12}),  # b 1
        ({4, 12, 6}, {0, 1, 2, 3, 8}),  # c 2
        ({8, 12}, {0, 1, 2, 3, 4, 6})   # d 3
    ]
    assert dukeli.splits_overlap_counts == {(0, 1): 4, (0, 2): 3, (0, 3): 3, (1, 2): 4, (1, 3): 3, (2, 3): 4}
    assert dukeli.bundles == [[0, 1, 2, 3]]
    assert dukeli.gapless_boolf == dukeli
