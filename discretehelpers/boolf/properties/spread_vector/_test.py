from discretehelpers.boolf import Boolf


def test():

    assert Boolf('0').spread_vector == []
    assert Boolf('1').spread_vector == []

    assert Boolf('10').spread_vector == [0]
    assert Boolf('10', [1]).spread_vector == [1]
    assert Boolf('10', [2]).spread_vector == [2]

    assert Boolf('1000', [0, 2]).spread_vector == [0, 1]
    assert Boolf('1001', [10, 20]).spread_vector == [10, 19]
    assert Boolf('0101 1100', [10, 20, 30]).spread_vector == [10, 19, 28]

    assert Boolf(fullspots={3, 20, 5, 31}, atomvals=[0, 4, 5, 6, 7]).spread_vector == [0, 3, 3, 3, 3]
