from discretehelpers.boolf import Boolf


def test():
    nope = Boolf('0')
    yay = Boolf('1')
    inside = Boolf('01', [5])
    outside = Boolf('10', [5])
    boolf_and = Boolf('0001', [3, 5])
    boolf_or = Boolf('0111', [3, 5])
    boolf_xor = Boolf('0110', [3, 5])

    assert nope.splits_equal == {}
    assert yay.splits_equal == {}
    assert inside.splits_equal == {}
    assert outside.splits_equal == {}
    assert boolf_and.splits_equal == {(0, 1): True}
    assert boolf_or.splits_equal == {(0, 1): False}
    assert boolf_xor.splits_equal == {(0, 1): True}

    assert nope.splits_onesided == []
    assert yay.splits_onesided == []
    assert inside.splits_onesided == [True]
    assert outside.splits_onesided == [True]
    assert boolf_and.splits_onesided == [True, True]
    assert boolf_or.splits_onesided == [False, False]
    assert boolf_xor.splits_onesided == [False, False]
