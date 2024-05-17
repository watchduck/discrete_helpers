from discretehelpers.boolf import Boolf


def test():
    a = Boolf('0111')
    assert a.gapless_boolf == a

    b = Boolf('0111 1111')
    assert b.gapless_boolf == Boolf('1')
