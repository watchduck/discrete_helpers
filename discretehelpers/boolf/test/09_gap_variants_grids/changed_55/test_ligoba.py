from discretehelpers.boolf.examples.e09_gap_variants_grids import ligoba, ligoba_fs, medina


def test_ligoba():
    assert ligoba.fullspots == ligoba_fs
    assert ligoba.splits == [
        ({115, 243}, {2, 4, 16, 112, 18, 50, 20, 52, 114, 240, 242, 244, 252, 124}),  # a 0
        ({2, 18, 115, 50, 114, 242, 243}, {4, 16, 112, 240, 20, 52, 244, 252, 124}),  # b 1
        ({124, 4, 244, 20, 52, 252}, {2, 16, 112, 18, 50, 114, 115, 240, 242, 243}),  # c 2
        ({124, 252}, {2, 4, 16, 112, 18, 50, 20, 52, 114, 115, 240, 242, 243, 244}),  # d 3
        ({16, 112, 18, 50, 20, 52, 114, 115, 240, 242, 243, 244, 124, 252}, {2, 4}),  # e 4
        ({112, 240, 50, 115, 52, 114, 242, 243, 244, 252, 124}, {16, 2, 18, 4, 20}),  # f 5
        ({112, 240, 114, 115, 242, 243, 244, 252, 124}, {16, 2, 18, 4, 50, 20, 52}),  # g 6
        ({240, 242, 243, 244, 252}, {2, 4, 16, 112, 18, 50, 20, 52, 114, 115, 124})   # h 7
    ]
