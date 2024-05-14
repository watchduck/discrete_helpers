from discretehelpers.boolf import Boolf
from discretehelpers.set_part import SetPart

from discretehelpers.boolf.examples import putuki


def test():
    assert putuki == Boolf('1111 1010 1100 1000')
    assert putuki.fullspots == {0, 1, 2, 3, 4, 6, 8, 9, 12}
    assert putuki.splits == [
        ({1, 3, 9}, {0, 2, 4, 6, 8, 12}),  # a 0
        ({2, 3, 6}, {0, 1, 4, 8, 9, 12}),  # b 1
        ({4, 12, 6}, {0, 1, 2, 3, 8, 9}),  # c 2
        ({8, 9, 12}, {0, 1, 2, 3, 4, 6})   # d 3
    ]
    assert putuki.splits_overlap_counts == {(0, 1): 4, (0, 2): 3, (0, 3): 4, (1, 2): 4, (1, 3): 3, (2, 3): 4}
    assert putuki.bundles == [[0, 1, 2, 3]]
    assert putuki.bundle_overlap_counts == {
        (0, 1, 2, 3): {
            3: [(0, 2), (1, 3)],  # (a, c), (b, d)
            4: [(0, 1), (0, 3), (1, 2), (2, 3)]
        }
    }
    assert putuki.bundle_grid_partitions == {
        (0, 1, 2, 3): SetPart([[0, 2], [1, 3]])  # [a, c], [b, d]
    }
    assert putuki.gapless_boolf == putuki
