from discretehelpers.boolf import Boolf


def test():

    assert Boolf(walsh_spectrum=[0]) == Boolf('0')
    assert Boolf(walsh_spectrum=[1]) == Boolf('1')

    assert Boolf(walsh_spectrum=[2, 0, 2, 0]) == Boolf('1100')

    assert Boolf(walsh_spectrum=[5, -3, 1, 1, -1, -1, -1, -1]) == Boolf('0101 1101')
