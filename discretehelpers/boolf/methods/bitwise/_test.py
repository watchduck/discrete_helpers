from discretehelpers.boolf import Boolf


def test():
    a = Boolf('01')
    b = Boolf('0011')
    c = Boolf('0000 1111')

    assert a & b == Boolf('0001')
    assert a | b == Boolf('0111')
    assert a ^ b == Boolf('0110')

    assert a & b & c == Boolf('0000 0001')
    assert a & b & c.complement == Boolf('0001 0000')
    assert a | b | c == Boolf('0111 1111')
    assert a ^ b ^ c == Boolf('0110 1001')

    assert (a ^ b ^ c).bitwise_lt(a | b | c)

    a_lt_b = a.bitwise_lt(b)
    a_gt_b = a.bitwise_gt(b)
    a_le_b = a.bitwise_le(b)
    a_ge_b = a.bitwise_ge(b)
    assert not a_lt_b or a_gt_b or a_le_b or a_ge_b or a == b

    assert Boolf('0100').bitwise_lt(Boolf('0110'))
    assert Boolf('1110').bitwise_gt(Boolf('0110'))

    assert ~a == Boolf('10')
    assert ~b == Boolf('1100')
    assert ~Boolf('0110') == Boolf('1001')

    yay = Boolf('1')
    assert not (yay.bitwise_lt(yay)) or (yay.bitwise_gt(yay))
    assert (yay.bitwise_le(yay)) and (yay.bitwise_ge(yay)) and (yay == yay)
    assert ~yay == Boolf('0')
