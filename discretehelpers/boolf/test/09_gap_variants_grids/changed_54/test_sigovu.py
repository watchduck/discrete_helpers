from discretehelpers.boolf.examples.e09_gap_variants_grids import sigovu, sigovu_fs, manila


def test_sigovu():
    assert sigovu.fullspots == sigovu_fs
    assert sigovu.splits == [
        ({123, 27}, {2, 26, 120, 24, 122, 12, 60}),  # a 0 0
        ({2, 26, 27, 122, 123}, {24, 12, 120, 60}),  # b 1 1
        ({12, 60}, {2, 26, 24, 27, 122, 123, 120}),  # d 3 2
        ({122, 123, 12, 120, 24, 26, 27, 60}, {2}),  # e 4 3
        ({26, 120, 24, 122, 123, 60, 27}, {2, 12}),  # f 5 4
        ({120, 122, 123, 60}, {2, 24, 26, 27, 12}),  # g 6 5
        ({120, 122, 123}, {2, 24, 26, 27, 12, 60})   # h 7 6
    ]
