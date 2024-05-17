from discretehelpers.boolf import Boolf


def test():

    assert Boolf('0').reverse == Boolf('0')
    assert Boolf('1').reverse == Boolf('1')
    assert Boolf(atom=99).reverse == ~Boolf(atom=99)
    assert Boolf('0001').reverse == Boolf('1000')
    assert Boolf('0001', [88, 99]).reverse == Boolf('1000', [88, 99])
    assert Boolf('0011 0110', [77, 88, 99]).reverse == Boolf('0110 1100', [77, 88, 99])
