from discretehelpers.boolf.examples.e09_gap_variants_grids import gatade, gatade_fs, medina


def test_gatade():
    assert gatade.fullspots == gatade_fs
    assert gatade.splits == [
        ({3}, {0, 2, 60, 16, 48, 112, 124, 20, 52, 116, 240, 244, 252, 28}),  # a 0
        ({2, 3}, {0, 60, 16, 48, 112, 124, 20, 52, 116, 240, 244, 252, 28}),  # b 1
        ({60, 124, 116, 20, 52, 244, 252, 28}, {0, 16, 2, 3, 48, 112, 240}),  # c 2
        ({124, 28, 252, 60}, {0, 2, 3, 16, 48, 112, 240, 20, 52, 116, 244}),  # d 3
        ({60, 16, 48, 112, 124, 20, 52, 116, 240, 244, 252, 28}, {0, 2, 3}),  # e 4
        ({48, 112, 124, 240, 116, 52, 244, 252, 60}, {0, 16, 2, 3, 20, 28}),  # f 5
        ({112, 240, 124, 116, 244, 252}, {0, 2, 3, 60, 16, 48, 20, 52, 28}),  # g 6
        ({240, 244, 252}, {0, 2, 3, 60, 16, 48, 112, 124, 20, 52, 116, 28})   # h 7
    ]
