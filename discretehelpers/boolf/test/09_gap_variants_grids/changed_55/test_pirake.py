from discretehelpers.boolf.examples.e09_gap_variants_grids import pirake, pirake_fs, medina


def test_pirake():
    assert pirake.fullspots == pirake_fs
    assert pirake.splits == [
        ({51, 19}, {16, 50, 114, 4, 244, 12, 60}),  # a 0
        ({51, 50, 19, 114}, {16, 4, 244, 12, 60}),  # b 1
        ({244, 4, 12, 60}, {16, 50, 51, 19, 114}),  # c 2
        ({12, 60}, {16, 50, 51, 4, 19, 114, 244}),  # d 3
        ({16, 50, 51, 19, 114, 244, 60}, {4, 12}),  # e 4
        ({50, 51, 244, 114, 60}, {16, 19, 4, 12}),  # f 5
        ({114, 244}, {16, 50, 19, 4, 51, 12, 60}),  # g 6
        ({244}, {4, 12, 16, 50, 19, 51, 114, 60})   # h 7
    ]
