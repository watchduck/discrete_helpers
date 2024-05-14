from discretehelpers.boolf.examples.e09_gap_variants_grids import tevoga, tevoga_fs


def test_tevoga():
    assert tevoga.fullspots == tevoga_fs
    assert tevoga.splits == [
        ({3, 11, 123, 59, 27}, {124, 4, 120, 122, 12, 28, 60}),  # a 0 0
        ({3, 11, 123, 122, 59, 27}, {124, 4, 120, 12, 28, 60}),  # b 1 1
        ({124, 4, 12, 28, 60}, {3, 11, 123, 122, 59, 120, 27}),  # d 3 2
        ({59, 11, 12, 123, 60, 124, 120, 122, 27, 28}, {3, 4}),  # e 4 3
        ({27, 123, 60, 124, 120, 122, 59, 28}, {11, 3, 4, 12}),  # f 5 4
        ({120, 123, 122, 59, 124, 60}, {3, 4, 27, 11, 12, 28}),  # g 6 5
        ({120, 122, 123, 124}, {3, 4, 59, 11, 12, 60, 27, 28})   # h 7 6
    ]