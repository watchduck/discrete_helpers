from discretehelpers.set_part_comp import SetPartComp
from discretehelpers.boolf.examples.e05_blight import demole


def test_demole():

    assert demole.bloat == SetPartComp([[0, 4]], {(0, 2)})
    assert demole.splits == [
        ({17}, {4, 12, 6}),  # a 0   equal to e, complement of c
        ({6}, {17, 4, 12}),  # b 1
        ({4, 12, 6}, {17}),  # c 2   preferred over a and e
        ({12}, {17, 4, 6}),  # d 3
        ({17}, {4, 12, 6})   # e 4   equal to a, complement of c
    ]
    assert demole.splits_equality_blocks == [ [1], [0, 2, 4],  [3]]
    assert demole.splits_preferred_side  == [None,         2, None]

    assert demole.bloatless_boolf.splits == [
        ({3}, {0, 2, 6}),  # b 1 0
        ({2, 3, 6}, {0}),  # c 2 1
        ({6}, {0, 2, 3})   # d 3 2
    ]

    # bloatless alternative (A instead of C)
    filtrated = demole.filtrated_boolf([0, 1, 3])  # A, B, D
    assert filtrated == filtrated.bloatless_boolf
    assert filtrated.splits == [
        ({1}, {0, 2, 4}),  # a 0 0
        ({2}, {0, 1, 4}),  # b 1 1
        ({4}, {0, 1, 2})   # d 3 2
    ]
