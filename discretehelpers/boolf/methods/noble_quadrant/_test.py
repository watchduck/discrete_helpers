from discretehelpers.boolf import Boolf


def test():

    assert Boolf('0000 0001 0001 0000').noble_quadrant() == 0
    assert Boolf('0111 1110 1110 1111').noble_quadrant() == 3
    assert Boolf('0111 1110 1110 1110').noble_quadrant() == 1
    assert Boolf('0000 0001 0001 0001').noble_quadrant() == 2
