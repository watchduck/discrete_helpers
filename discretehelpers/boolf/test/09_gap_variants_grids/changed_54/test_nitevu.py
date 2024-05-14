from discretehelpers.boolf.examples.e09_gap_variants_grids import nitevu, nitevu_fs, manila


def test_nitevu():
    assert nitevu.fullspots == nitevu_fs
    assert nitevu.splits == [
        ({27, 59, 11}, {0, 10, 26, 58, 124, 60}),  # a 0 0
        ({10, 26, 11, 27, 58, 59}, {0, 124, 60}),  # b 1 1
        ({124, 60}, {0, 10, 26, 11, 27, 58, 59}),  # d 3 2
        ({58, 59, 10, 11, 124, 26, 27, 60}, {0}),  # e 4 3
        ({26, 59, 58, 27, 124, 60}, {0, 10, 11}),  # f 5 4
        ({124, 58, 59, 60}, {0, 26, 27, 10, 11}),  # g 6 5
        ({124}, {0, 58, 59, 10, 11, 26, 27, 60})   # h 7 6
    ]
