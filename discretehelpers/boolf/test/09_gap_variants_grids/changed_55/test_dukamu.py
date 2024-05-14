from discretehelpers.boolf.examples.e09_gap_variants_grids import dukamu, dukamu_fs, medina


def test_dukamu():
    assert dukamu.fullspots == dukamu_fs
    assert dukamu.splits == [
        ({19, 51, 3, 115}, {0, 2, 4, 16, 18, 20, 28, 112, 240, 50, 114, 52, 116, 244, 252, 60}),  # a 0
        ({2, 3, 18, 19, 50, 51, 114, 115}, {0, 4, 60, 16, 112, 240, 20, 52, 116, 244, 252, 28}),  # b 1
        ({4, 60, 20, 52, 116, 244, 252, 28}, {0, 2, 3, 16, 112, 18, 19, 50, 51, 114, 115, 240}),  # c 2
        ({28, 252, 60}, {0, 2, 3, 4, 16, 18, 19, 20, 112, 240, 50, 51, 52, 114, 115, 116, 244}),  # d 3
        ({16, 18, 19, 20, 28, 112, 240, 50, 51, 52, 114, 115, 116, 244, 252, 60}, {0, 2, 3, 4}),  # e 4
        ({112, 240, 50, 51, 52, 114, 115, 116, 244, 252, 60}, {0, 2, 3, 4, 16, 18, 19, 20, 28}),  # f 5
        ({112, 240, 114, 115, 116, 244, 252}, {0, 2, 3, 4, 60, 16, 18, 19, 20, 50, 51, 52, 28}),  # g 6
        ({240, 244, 252}, {0, 2, 3, 4, 16, 18, 19, 20, 28, 112, 50, 51, 52, 114, 115, 116, 60})   # h 7
    ]
