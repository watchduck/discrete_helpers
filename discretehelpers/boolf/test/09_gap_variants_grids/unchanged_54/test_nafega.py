from discretehelpers.boolf.examples.e09_gap_variants_grids import nafega, nafega_fs


def test_nafega():
    assert nafega.fullspots == nafega_fs
    assert nafega.splits == [
        ({123, 3}, {2, 56, 4, 8, 24, 122, 124}),  # a 0 0
        ({123, 2, 3, 122}, {4, 8, 24, 56, 124}),  # b 1 1
        ({124, 4}, {2, 3, 56, 8, 24, 122, 123}),  # d 3 2
        ({56, 8, 24, 122, 123, 124}, {2, 3, 4}),  # e 4 3
        ({56, 24, 122, 123, 124}, {8, 2, 3, 4}),  # f 5 4
        ({56, 122, 123, 124}, {2, 3, 4, 8, 24}),  # g 6 5
        ({122, 123, 124}, {2, 3, 4, 8, 24, 56})   # h 7 6
    ]
