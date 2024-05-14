from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.set_part_comp import SetPartComp
from discretehelpers.boolf import Boolf

from discretehelpers.boolf.methods.bloatless_spotint.ex import BloatMismatchError, TooBigError
from discretehelpers.boolf.ex import BoolfNotBlightlessError


def test():
    boolf = Boolf('1000 0001')  # clan 14
    assert boolf.fullspots == {0, 7}
    assert boolf.splits == [
        ({7}, {0}),
        ({7}, {0}),
        ({7}, {0})
    ]
    assert boolf.splits_overlap_counts == {(0, 1): 2, (0, 2): 2, (1, 2): 2}
    assert boolf.splits_equal == {(0, 1): True, (0, 2): True, (1, 2): True}
    assert boolf.splits_onesided == [False, False, False]
    assert boolf.splits_equality_blocks == [[0, 1, 2]]

    boolf = Boolf('0000 0001')  # clan 17
    assert boolf.fullspots == {7}
    assert boolf.splits == [
        ({7}, set()),  # 0
        ({7}, set()),  # 1
        ({7}, set())   # 2
    ]
    assert boolf.splits_overlap_counts == {(0, 1): 1, (0, 2): 1, (1, 2): 1}
    assert boolf.splits_equal == {(0, 1): True, (0, 2): True, (1, 2): True}
    assert boolf.splits_onesided == [True, True, True]
    assert boolf.splits_equality_blocks == [[0, 1, 2]]

    boolf = Boolf('0000 1001')  # clan 8
    assert boolf.fullspots == {4, 7}
    assert boolf.splits == [
        ({7}, {4}),       # 0
        ({7}, {4}),       # 1
        ({4, 7}, set())   # 2
    ]
    assert boolf.splits_overlap_counts == {(0, 1): 2, (0, 2): 2, (1, 2): 2}
    assert boolf.splits_equal == {(0, 1): True, (0, 2): False, (1, 2): False}
    assert boolf.splits_onesided == [False, False, True]
    assert boolf.splits_equality_blocks == [[0, 1], [2]]
    assert boolf.bloatless_boolf.bundles == [[0]]
    abbrev(BoolfNotBlightlessError, [
        lambda: boolf.bundles
    ])

    boolf = Boolf('1101 0001')  # clan 15
    assert boolf.fullspots == {0, 1, 3, 7}
    assert boolf.splits == [
        ({1, 3, 7}, {0}),  # 0
        ({3, 7}, {0, 1}),  # 1
        ({7}, {0, 1, 3})   # 2
    ]
    assert boolf.splits_overlap_counts == {(0, 1): 3, (0, 2): 3, (1, 2): 3}
    assert boolf.splits_equal == {(0, 1): False, (0, 2): False, (1, 2): False}
    assert boolf.splits_onesided == [False, False, False]
    assert boolf.splits_equality_blocks == [[0], [1], [2]]
    assert boolf.bundles == [[0], [1], [2]]


def test_same_clan():  # clan 9
    first_places_equal = [0, 3, 4, 7]
    first_places_different = [1, 2, 5, 6]

    a = Boolf('1001 0001', [10, 20, 30])
    assert a.fullspots == {0, 3, 7}
    assert a.splits == [
        ({3, 7}, {0}),  # 0
        ({3, 7}, {0}),  # 1
        ({7}, {0, 3})   # 2
    ]
    assert a.splits_preferred_side == [None, None]
    assert a.bloatless_atomkeys_undeflated == [0, 2]

    assert a.bloat == SetPartComp([[0, 1]])
    assert a.bloat_boolf == Boolf('1001', [10, 20])
    assert a.bloatless_boolf == Boolf('1101', [10, 30])
    assert [a.bloatless_spotint(_) for _ in first_places_equal] == [0, 1, 2, 3]
    abbrev(BloatMismatchError, [lambda: a.bloatless_spotint(_) for _ in first_places_different])
    abbrev(TooBigError, [lambda: a.bloatless_spotint(_) for _ in [8, 9, 10]])

    # The Boolean function above is (C subset of A) and (A EQUALS B).
    # The following one is also from clan 9, but (C subset of A) and (A COMPLEMENT B).
    b = Boolf('0110 0100', [10, 20, 30])
    assert b.fullspots == {1, 2, 5}
    assert b.splits == [
        ({1, 5}, {2}),  # 0
        ({2}, {1, 5}),  # 1
        ({5}, {1, 2})   # 2
    ]
    assert b.splits_equality_blocks == [[0, 1], [2]]
    assert b.splits_preferred_side == [0, None]
    assert b.bloatless_atomkeys_undeflated == [0, 2]

    assert b.bloat == SetPartComp([], {(0, 1)})
    assert b.bloatless_boolf == Boolf('1101', [10, 30])
    assert [b.bloatless_spotint(_) for _ in first_places_different] == [1, 0, 3, 2]
    abbrev(BloatMismatchError, [lambda: b.bloatless_spotint(_) for _ in first_places_equal])
    abbrev(TooBigError, [lambda: b.bloatless_spotint(_) for _ in [8, 9, 10]])

    for boolf in [a, b]:
        assert boolf.splits_overlap_counts == {(0, 1): 2, (0, 2): 3, (1, 2): 3}
        assert boolf.splits_equal == {(0, 1): True, (0, 2): False, (1, 2): False}
        assert boolf.splits_onesided == [False, False, False]
        assert boolf.splits_equality_blocks == [[0, 1], [2]]
