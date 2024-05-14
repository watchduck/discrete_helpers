from discretehelpers.boolf import Boolf


def test():

    assert Boolf(atom=123) == Boolf('01', [123])
    assert Boolf(atom=~123) == Boolf('10', [123])
