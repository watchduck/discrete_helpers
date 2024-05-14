from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples import medusa


def test():
    assert medusa.splits == [
        ({1, 3, 5, 7, 9}, {0, 2, 4, 6, 8, 10, 12, 14}),  # a 0
        ({2, 3, 6, 7, 10, 14}, {0, 1, 4, 5, 8, 9, 12}),  # b 1
        ({4, 5, 6, 7, 12, 14}, {0, 1, 2, 3, 8, 9, 10}),  # c 2
        ({8, 9, 10, 12, 14}, {0, 1, 2, 3, 4, 5, 6, 7})   # d 3
    ]
    assert medusa.splits_overlap_counts == {(0, 1): 4, (0, 2): 4, (0, 3): 4, (1, 2): 4, (1, 3): 4, (2, 3): 4}  # all have 4 overlaps
    assert medusa.bundles == [[0, 1, 2, 3]]
    assert medusa.splits_onesided == [False, False, False, False]
    assert medusa.splits_preferred_side == [None, None, None, None]
    assert medusa.gapless_boolf == Boolf('1')
