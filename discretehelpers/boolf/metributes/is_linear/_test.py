from discretehelpers.boolf import Boolf


def test():
    assert Boolf('0').is_linear
    assert Boolf('1').is_linear
    assert Boolf('01').is_linear
    assert Boolf('10').is_linear
    assert Boolf('0110', [123, 456]).is_linear
    assert Boolf('1001').is_linear
    assert Boolf('0101 1010', [123, 456, 789]).is_linear
    assert Boolf('1010 0101').is_linear
    assert Boolf('0110 1001 1001 0110').is_linear

    assert not Boolf('0100').is_linear
    assert not Boolf('1011', [12, 34]).is_linear
    assert not Boolf('0011 0101').is_linear
