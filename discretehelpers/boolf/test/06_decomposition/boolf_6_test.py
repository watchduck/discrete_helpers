from discretehelpers.set_part_comp import SetPartComp
from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples.e06_decomposition import *


def test():
    # clan 127 (white)
    assert kibime == Boolf('1111 0010 1000 0000')
    assert kibime.fullspots == {0, 1, 2, 3, 6, 8}
    assert kibime.splits == [({1, 3}, {0, 8, 2, 6}), ({2, 3, 6}, {0, 1, 8}), ({6}, {0, 1, 2, 3, 8}), ({8}, {0, 1, 2, 3, 6})]

    # clan 41 a
    assert murife == Boolf('1101 0010 1000 0000')
    assert murife.fullspots == {0, 1, 3, 6, 8}
    assert murife.splits == [({1, 3}, {0, 8, 6}), ({3, 6}, {0, 1, 8}), ({6}, {0, 1, 3, 8}), ({8}, {0, 1, 3, 6})]

    # clan 41 b
    assert menabe == Boolf('0111 0010 1000 0000')
    assert menabe.fullspots == {1, 2, 3, 6, 8}
    assert menabe.splits == [({1, 3}, {8, 2, 6}), ({2, 3, 6}, {8, 1}), ({6}, {8, 1, 2, 3}), ({8}, {1, 2, 3, 6})]

    # clan 205
    assert tefabi == Boolf('0101 0010 1000 0000')
    assert tefabi.fullspots == {8, 1, 3, 6}
    assert tefabi.splits == [({1, 3}, {8, 6}), ({3, 6}, {8, 1}), ({6}, {8, 1, 3}), ({8}, {1, 3, 6})]

    # clan 196 (not the same Euler shape)
    assert fobope == Boolf('1111 0000 1000 0000')
    assert fobope.fullspots == {0, 1, 2, 3, 8}
    assert fobope.splits == [({1, 3}, {0, 8, 2}), ({2, 3}, {0, 1, 8}), (set(), {0, 1, 2, 3, 8}), ({8}, {0, 1, 2, 3})]
    assert fobope.splits_onesided == [False, False, True, False]  # Argument 2 (c) is empty, so the other side of this split is the universe.

    # all
    boolfs = [kibime, murife, menabe, tefabi]

    for boolf in boolfs:
        assert boolf.splits_overlap_counts == {(0, 1): 4, (0, 2): 3, (0, 3): 3, (1, 2): 3, (1, 3): 3, (2, 3): 3}
        assert boolf.splits_equal == {(0, 1): False, (0, 2): False, (0, 3): False, (1, 2): False, (1, 3): False, (2, 3): False}
        assert boolf.splits_onesided == [False, False, False, False]

        boolf_and_equal = boolf & Boolf('1001', [3, 4])
        boolf_and_comp = boolf & Boolf('0110', [3, 4])
        assert boolf_and_equal.bloatless_boolf == boolf_and_comp.bloatless_boolf == boolf
        assert boolf_and_equal.bloat == SetPartComp([[3, 4]])
        assert boolf_and_comp.bloat == SetPartComp([], {(3, 4)})
        assert boolf.gapless_boolf == kibime

    for boolf in boolfs + [fobope]:
        assert boolf.bloatless_boolf == boolf
        assert boolf.splits_equality_blocks == [[0], [1], [2], [3]]
        assert boolf.bundles == [[0, 1], [2], [3]]
        assert boolf.bundle_overlap_counts == {
            (0, 1): {3: [], 4: [(0, 1)]},
            (2,): {3: [], 4: []},
            (3,): {3: [], 4: []}
        }
