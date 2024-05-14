from discretehelpers.boolf import Boolf


def test():
    nope = Boolf('0')
    yay = Boolf('1')
    assert nope.fullspots == set()
    assert yay.fullspots == {0}
    assert nope.splits == yay.splits == nope.splits_onesided == yay.splits_onesided == []
    assert nope.splits_overlap_counts == yay.splits_overlap_counts == nope.splits_equal == yay.splits_equal == dict()
    assert nope.splits_equality_blocks == yay.splits_equality_blocks == nope.splits_preferred_side == yay.splits_preferred_side == []
    assert nope.bloatless_boolf == nope
    assert yay.bloatless_boolf == yay

    pos = Boolf(atom=0)
    neg = Boolf(atom=~0)
    assert pos.splits == [({1}, set())]
    assert neg.splits == [(set(), {0})]
    assert pos.splits_overlap_counts == neg.splits_overlap_counts == pos.splits_equal == neg.splits_equal == dict()
    assert pos.splits_equality_blocks == neg.splits_equality_blocks == [[0]]

    a, b = Boolf('0111'), Boolf('0111', [33, 99])
    assert a.splits == b.splits == [({1, 3}, {2}), ({2, 3}, {1})]
