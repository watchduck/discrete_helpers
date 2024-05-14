from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e05_blight import megomi


def test_megomi():
    assert megomi.bloat == SetPartComp([], {(0, 2)})
    assert megomi.splits == [
        ({17, 3}, {4, 12, 6}),  # a 0   preferred over c
        ({3, 6}, {17, 4, 12}),  # b 1
        ({4, 12, 6}, {17, 3}),  # c 2   complement of a
        ({12}, {17, 3, 4, 6}),  # d 3
        ({17}, {3, 4, 12, 6})   # e 4
    ]
    assert megomi.splits_equality_blocks == [[0, 2],  [1],  [3],  [4]]
    assert megomi.splits_preferred_side  == [     0, None, None, None]

    assert megomi.bloatless_boolf.splits == [
        ({9, 3}, {0, 2, 4}),  # a 0 0
        ({2, 3}, {0, 9, 4}),  # b 1 1
        ({4}, {0, 9, 2, 3}),  # d 3 2
        ({9}, {0, 2, 3, 4})   # e 4 3
    ]

    # bloatless alternative (C instead of A)
    filtrated = megomi.filtrated_boolf([1, 2, 3, 4])  # B, C, D, E
    assert filtrated == filtrated.bloatless_boolf
    assert filtrated.splits == [
        ({1, 3}, {8, 2, 6}),  # b 1 0
        ({2, 3, 6}, {8, 1}),  # c 2 1
        ({6}, {8, 1, 2, 3}),  # d 3 2
        ({8}, {1, 2, 3, 6})   # e 4 3
    ]
