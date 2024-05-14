from discretehelpers.boolf.examples.e09_gap_variants_grids import nusure, nusure_fs, manila


def test_nusure():
    assert nusure.fullspots == nusure_fs
    assert nusure.splits == [
        ({27, 59, 11}, {2, 58, 10, 12, 120, 24, 56, 28}),  # a 0 0
        ({2, 58, 11, 27, 10, 59}, {120, 24, 56, 12, 28}),  # b 1 1
        ({12, 28}, {2, 58, 59, 10, 11, 24, 56, 27, 120}),  # d 3 2
        ({58, 59, 10, 11, 12, 120, 24, 56, 27, 28}, {2}),  # e 4 3
        ({56, 120, 24, 58, 59, 28, 27}, {11, 2, 10, 12}),  # f 5 4
        ({56, 58, 59, 120}, {2, 24, 27, 10, 11, 12, 28}),  # g 6 5
        ({120}, {2, 58, 59, 10, 11, 12, 24, 56, 27, 28})   # h 7 6
    ]
