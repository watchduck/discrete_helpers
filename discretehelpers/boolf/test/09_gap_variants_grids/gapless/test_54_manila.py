from discretehelpers.boolf.examples.e09_gap_variants_grids import manila, manila_bloated, manila_fs, t9_grid_boolf_abd, t9_grid_boolf_efgh


def test_manila():
    assert manila == manila_bloated.bloatless_boolf
    assert manila == t9_grid_boolf_abd & t9_grid_boolf_efgh
    assert manila.fullspots == manila_fs
    assert manila.splits == [
        ({3, 11, 123, 59, 27}, {0, 2, 56, 4, 58, 122, 8, 10, 12, 120, 60, 124, 24, 26, 28}),  # a 0 0
        ({2, 3, 58, 122, 59, 10, 11, 123, 26, 27}, {0, 4, 8, 12, 120, 60, 124, 24, 56, 28}),  # b 1 1
        ({124, 4, 12, 28, 60}, {0, 2, 3, 56, 58, 122, 8, 59, 10, 11, 123, 24, 26, 27, 120}),  # d 3 2
        ({8, 10, 11, 12, 24, 26, 27, 120, 28, 122, 123, 124, 56, 58, 59, 60}, {0, 2, 3, 4}),  # e 4 3
        ({26, 58, 122, 59, 123, 120, 60, 124, 24, 56, 27, 28}, {0, 2, 3, 4, 8, 10, 11, 12}),  # f 5 4
        ({122, 123, 120, 124, 56, 58, 59, 60}, {0, 2, 3, 4, 8, 10, 11, 12, 24, 26, 27, 28}),  # g 6 5
        ({120, 122, 123, 124}, {0, 2, 3, 4, 8, 10, 11, 12, 24, 26, 27, 28, 56, 58, 59, 60})   # h 7 6
    ]
