from discretehelpers.boolf.examples.e09_gap_variants_grids import linaki, linaki_fs, manila


def test_linaki():
    assert linaki.fullspots == linaki_fs
    assert linaki.splits == [
        ({27, 123, 3}, {0, 58, 120, 24, 10, 12, 60}),  # a 0 0
        ({3, 58, 27, 10, 123}, {0, 24, 12, 120, 60}),  # b 1 1
        ({12, 60}, {0, 3, 10, 123, 24, 58, 27, 120}),  # d 3 2
        ({10, 123, 12, 120, 24, 58, 27, 60}, {0, 3}),  # e 4 3
        ({120, 24, 58, 123, 60, 27}, {0, 10, 3, 12}),  # f 5 4
        ({120, 58, 123, 60}, {0, 3, 24, 10, 27, 12}),  # g 6 5
        ({120, 123}, {0, 3, 10, 12, 24, 58, 27, 60})   # h 7 6
    ]
