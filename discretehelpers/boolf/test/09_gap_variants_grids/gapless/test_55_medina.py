from discretehelpers.boolf.examples.e09_gap_variants_grids import medina, medina_fs, t9_grid_boolf_abcd, t9_grid_boolf_efgh


def test_medusa():
    assert medina == t9_grid_boolf_abcd & t9_grid_boolf_efgh
    assert medina.fullspots == medina_fs
    assert medina.splits == [
        ({3, 19, 51, 115, 243}, {0, 2, 4, 12, 16, 18, 20, 240, 28, 48, 112, 50, 114, 52, 116, 124, 242, 244, 252, 60}),  # a 0
        ({2, 3, 18, 19, 50, 51, 114, 115, 242, 243}, {0, 4, 12, 60, 16, 48, 112, 124, 20, 52, 116, 240, 244, 252, 28}),  # b 1
        ({4, 12, 60, 124, 20, 52, 116, 244, 252, 28}, {0, 2, 3, 16, 48, 18, 19, 50, 51, 112, 114, 115, 240, 242, 243}),  # c 2
        ({124, 252, 12, 28, 60}, {0, 2, 3, 4, 16, 18, 19, 20, 240, 48, 112, 242, 50, 51, 52, 114, 115, 116, 243, 244}),  # d 3
        ({16, 18, 19, 20, 240, 28, 60, 48, 112, 242, 243, 244, 50, 51, 52, 114, 115, 116, 124, 252}, {0, 2, 3, 4, 12}),  # e 4
        ({252, 48, 112, 50, 51, 52, 114, 115, 116, 124, 240, 242, 243, 60, 244}, {0, 2, 3, 4, 12, 16, 18, 19, 20, 28}),  # f 5
        ({112, 240, 114, 115, 116, 242, 243, 244, 252, 124}, {0, 2, 3, 4, 12, 60, 16, 48, 18, 19, 20, 50, 51, 52, 28}),  # g 6
        ({240, 242, 243, 244, 252}, {0, 2, 3, 4, 12, 16, 18, 19, 20, 28, 48, 112, 50, 51, 52, 114, 115, 116, 124, 60})   # h 7
    ]
