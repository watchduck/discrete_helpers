from discretehelpers.boolf import Boolf


def test():
    boolf = Boolf('0100 1101')
    assert boolf.walsh_distances() == (4, 2, 6, 4, 2, 4, 4, 2)
    assert boolf.walsh_distances(4) == (8, 4, 12, 8, 4, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8, 8)

