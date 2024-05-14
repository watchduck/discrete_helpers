from discretehelpers.boolf import Boolf


def test():

    assert Boolf(zhe=0) == Boolf('0')
    assert Boolf(zhe=1) == Boolf('1')
    assert Boolf(zhe=2) == Boolf('01')
    assert Boolf(zhe=3) == Boolf('10')
    assert Boolf(zhe=4) == Boolf('01', [1])
    assert Boolf(zhe=5) == Boolf('10', [1])

    assert Boolf(zhe=123) == Boolf('1011 0010')
