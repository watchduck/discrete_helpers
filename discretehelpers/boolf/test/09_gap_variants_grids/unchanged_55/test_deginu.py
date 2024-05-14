from discretehelpers.boolf.examples.e09_gap_variants_grids import deginu, deginu_fs


def test_deginu():
    assert deginu.fullspots == deginu_fs
    assert deginu.splits == [
        ({3, 19, 51, 115, 243}, {0, 2, 12, 240, 242, 20, 52, 116, 252}),  # a 0
        ({2, 3, 242, 19, 51, 115, 243}, {0, 240, 116, 20, 52, 252, 12}),  # b 1
        ({116, 20, 52, 252, 12}, {0, 2, 3, 240, 242, 19, 51, 115, 243}),  # c 2
        ({12, 252}, {0, 2, 3, 240, 242, 19, 20, 51, 52, 115, 116, 243}),  # d 3
        ({240, 242, 115, 51, 19, 20, 52, 116, 243, 252}, {0, 2, 3, 12}),  # e 4
        ({240, 242, 115, 116, 51, 52, 243, 252}, {0, 2, 3, 19, 20, 12}),  # f 5
        ({240, 242, 115, 116, 243, 252}, {0, 2, 3, 12, 19, 20, 51, 52}),  # g 6
        ({240, 242, 243, 252}, {0, 2, 3, 12, 19, 20, 51, 52, 115, 116})   # h 7
    ]