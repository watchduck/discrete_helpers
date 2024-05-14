from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e05_blight import rigeko


def test_rigeko():
    assert rigeko.bloat == SetPartComp([], {(0, 2)})
    assert rigeko.splits == [
        ({17, 11}, {4, 6}),  # a 0   complement of c
        ({11, 6}, {17, 4}),  # b 1
        ({4, 6}, {17, 11}),  # c 2   preferred over a
        ({11}, {17, 4, 6}),  # d 3
        ({17}, {11, 4, 6})   # e 4
    ]
    assert rigeko.splits_equality_blocks == [ [1], [0, 2],  [3],  [4]]
    assert rigeko.splits_preferred_side  == [None,      2, None, None]

    assert rigeko.bloatless_boolf.splits == [
        ({3, 5}, {8, 2}),  # b 1 0
        ({2, 3}, {8, 5}),  # c 2 1
        ({5}, {8, 2, 3}),  # d 3 2
        ({8}, {2, 3, 5})   # e 4 3
    ]

    # bloatless alternative (A instead of C)
    filtrated = rigeko.filtrated_boolf([0, 1, 3, 4])  # A, B, D, E
    assert filtrated == filtrated.bloatless_boolf
    assert filtrated.splits == [
        ({9, 7}, {0, 2}),  # a 0 0
        ({2, 7}, {0, 9}),  # b 1 1
        ({7}, {0, 9, 2}),  # d 3 2
        ({9}, {0, 2, 7})   # e 4 3
    ]
