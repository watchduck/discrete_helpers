from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.set_part import SetPart
from discretehelpers.set_part_comp import SetPartComp
from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples.e05_blight import tokosi, tokosi_bloatless
from discretehelpers.boolf.ex import BoolfNotBlightlessError
from fractions import Fraction


def test_tokosi():
    assert tokosi.atomvals == [1, 3, 5, 7, 9]
    assert tokosi.atomvals_integer == 682
    assert tokosi.atomvals_sierpinski == [0, 2, 8, 10, 32, 34, 40, 42, 128, 130, 136, 138, 160, 162, 168, 170, 512, 514, 520, 522, 544, 546, 552, 554, 640, 642, 648, 650, 672, 674, 680, 682]
    assert tokosi.adicity == 10
    assert tokosi.valency == 5

    assert tokosi.complement == Boolf('1110 1101 1111 1111  1111 1111 0111 0011', [1, 3, 5, 7, 9])
    assert tokosi.number_of_distinct_splits == 3
    assert tokosi.weight_fract == Fraction(5, 32)

    assert tokosi.splits == [
        ({3, 29}, {24, 28, 6}),  # 0: 1
        ({3, 6}, {24, 28, 29}),  # 1: 3
        ({28, 29, 6}, {24, 3}),  # 2: 5
        ({24, 28, 29}, {3, 6}),  # 3: 7
        ({24, 28, 29}, {3, 6})   # 4: 9
    ]
    assert tokosi.splits_overlap_counts == {(0, 1): 4, (0, 2): 4, (0, 3): 4, (0, 4): 4, (1, 2): 4, (1, 3): 2, (1, 4): 2, (2, 3): 4, (2, 4): 4, (3, 4): 2}
    assert tokosi.splits_equal == {(0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (1, 2): False, (1, 3): True, (1, 4): True, (2, 3): False, (2, 4): False, (3, 4): True}
    assert tokosi.splits_onesided == [False, False, False, False, False]
    assert tokosi.splits_equality_blocks == [[0], [1, 3, 4], [2]]
    assert tokosi.splits_preferred_side == [None, 1, None]

    assert tokosi.bloatless_atomkeys_undeflated == [0, 1, 2]
    assert tokosi.fullspots == {3, 6, 24, 28, 29}
    assert tokosi.bloat == SetPartComp([[3, 4]], {(1, 3)})  # atomkeys (thin labels in the images)

    abbrev(BoolfNotBlightlessError, [
        lambda: tokosi.bundles,
        lambda: tokosi.bundle_grid_partitions,
        lambda: tokosi.bundle_overlap_counts
    ])

    # separated bloat
    tokosi_bloat = tokosi.bloat_boolf
    assert tokosi_bloat == Boolf('0100 0010', [3, 7, 9])  # atomvals (thick labels in the images)
    assert tokosi_bloat.fullspots == {1, 6}
    assert tokosi_bloat.bloat_boolf == tokosi_bloat
    assert tokosi_bloat.bloatless_boolf == Boolf('1')

    # separated content (bloatless)
    assert tokosi_bloatless == Boolf('1001 1110', [1, 3, 5])
    assert tokosi_bloatless.fullspots == {0, 3, 4, 5, 6}
    assert tokosi_bloatless.adicity == 6
    assert tokosi_bloatless.valency == 3

    assert tokosi_bloatless.bloat_boolf == Boolf('1')
    assert tokosi_bloatless.bloatless_boolf == tokosi_bloatless
    assert tokosi_bloatless.bundles == [[0, 1, 2]]
    assert tokosi_bloatless.value_fract() == Fraction(4402341479684, 5519032976645)  # high numbers because of gaps between atomvals
    assert tokosi_bloatless.bundle_grid_partitions == {
        (0, 1, 2): SetPart([])
    }
    assert tokosi_bloatless.bundle_overlap_counts == {
        (0, 1, 2): {
            3: [],
            4: [(0, 1), (0, 2), (1, 2)]
        }
    }

    # combined again
    assert tokosi_bloatless & tokosi_bloat == tokosi
