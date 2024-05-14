from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e05_blight import rudafi


def test_rudafi():
    assert rudafi.bloat == SetPartComp([], {(0, 2)})
    assert rudafi.splits == [
        ({9, 17}, {4, 6}),  # a 0   complement of c
        ({6}, {9, 4, 17}),  # b 1
        ({4, 6}, {9, 17}),  # c 2   preferred over a
        ({9}, {17, 4, 6}),  # d 3
        ({17}, {9, 4, 6})   # e 4
    ]
    assert rudafi.splits_equality_blocks == [ [1], [0, 2],  [3],  [4]]
    assert rudafi.splits_preferred_side  == [None,      2, None, None]

    assert rudafi.bloatless_boolf.splits == [
        ({3}, {8, 2, 4}),  # b 1 0
        ({2, 3}, {8, 4}),  # c 2 1
        ({4}, {8, 2, 3}),  # d 3 2
        ({8}, {2, 3, 4})   # e 4 3
    ]

    # bloatless alternative (A instead of C)
    filtrated = rudafi.filtrated_boolf([0, 1, 3, 4])  # A, B, D, E
    assert filtrated == filtrated.bloatless_boolf
    assert filtrated.splits == [
        ({9, 5}, {0, 2}),  # a 0 0
        ({2}, {0, 9, 5}),  # b 1 1
        ({5}, {0, 9, 2}),  # d 3 2
        ({9}, {0, 2, 5})   # e 4 3
    ]
