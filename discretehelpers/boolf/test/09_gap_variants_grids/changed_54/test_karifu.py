from discretehelpers.boolf.examples.e09_gap_variants_grids import karifu, karifu_fs, manila


def test_karifu():
    assert karifu.fullspots == karifu_fs
    assert karifu.splits == [
        ({59, 11}, {2, 4, 122, 8, 124, 56, 26, 28}),  # a 0 0
        ({2, 26, 59, 122, 11}, {124, 4, 8, 56, 28}),  # b 1 1
        ({124, 4, 28}, {2, 56, 26, 8, 59, 122, 11}),  # d 3 2
        ({122, 8, 11, 124, 56, 26, 59, 28}, {2, 4}),  # e 4 3
        ({26, 56, 122, 59, 124, 28}, {8, 2, 11, 4}),  # f 5 4
        ({56, 122, 59, 124}, {2, 4, 8, 26, 11, 28}),  # g 6 5
        ({122, 124}, {2, 4, 8, 11, 56, 26, 59, 28})   # h 7 6
    ]
