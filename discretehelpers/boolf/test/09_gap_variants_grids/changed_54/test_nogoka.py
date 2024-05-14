from discretehelpers.boolf.examples.e09_gap_variants_grids import nogoka, nogoka_fs, manila


def test_nogoka():
    assert nogoka.fullspots == nogoka_fs
    assert nogoka.splits == [
        ({27, 59, 11}, {2, 58, 122, 10, 12, 24, 56, 28}),  # a 0 0
        ({2, 10, 58, 11, 27, 122, 59}, {24, 56, 12, 28}),  # b 1 1
        ({12, 28}, {2, 58, 122, 59, 10, 11, 24, 56, 27}),  # d 3 2
        ({58, 122, 59, 10, 11, 12, 24, 56, 27, 28}, {2}),  # e 4 3
        ({56, 122, 24, 27, 58, 59, 28}, {11, 2, 10, 12}),  # f 5 4
        ({56, 58, 59, 122}, {2, 24, 27, 10, 11, 12, 28}),  # g 6 5
        ({122}, {2, 58, 59, 10, 11, 12, 24, 56, 27, 28})   # h 7 6
    ]
