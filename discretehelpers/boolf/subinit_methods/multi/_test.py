from discretehelpers.boolf import Boolf


def test():

    assert Boolf(multi_and=[]) == Boolf(multi_xand=[]) == Boolf('1')
    assert Boolf(multi_or=[]) == Boolf(multi_xor=[]) == Boolf('0')

    assert Boolf(multi_and=[11, 22, 33, 44])  == Boolf('0000 0000 0000 0001', [11, 22, 33, 44])
    assert Boolf(multi_or=[11, 22, 33, 44])   == Boolf('0111 1111 1111 1111', [11, 22, 33, 44])
    assert Boolf(multi_xor=[11, 22, 33, 44])  == Boolf('0110 1001 1001 0110', [11, 22, 33, 44])
    assert Boolf(multi_xand=[11, 22, 33, 44]) == Boolf('1001 0110 0110 1001', [11, 22, 33, 44])

    assert Boolf(multi_and=[0, 1]) == Boolf('0001')
    assert Boolf(multi_and=[0, 1, ~2]) == Boolf('0001 0000')
    assert Boolf(multi_or=[5, 7]) == Boolf('0111', [5, 7])
    assert Boolf(multi_or=[5, 7, ~9]) == Boolf('1111 0111', [5, 7, 9])

    left = Boolf(multi_and=[~0, ~1, ~2])
    right = Boolf(multi_and=[0, 1, 2])
    assert left == Boolf('1000 0000')
    assert right == Boolf('0000 0001')
    assert Boolf(multi_or=[left, right]) == Boolf('1000 0001')
    assert Boolf(multi_or=[left, right, 3]) == Boolf('1000 0001 1111 1111')
