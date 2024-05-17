from discretehelpers.boolf import Boolf


def test():

    boolf = Boolf('0000 0001', [1, 2, 3])
    assert boolf.atomvals_sierpinski == [0, 2, 4, 6, 8, 10, 12, 14]
