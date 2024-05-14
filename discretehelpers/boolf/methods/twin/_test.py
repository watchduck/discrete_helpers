from discretehelpers.boolf import Boolf


def test():

    assert Boolf('0') == Boolf('0')

    boolf = Boolf('1')
    assert boolf.twin() == boolf.twin(0) == Boolf('1')
    assert boolf.twin(1) == Boolf('10')
    assert boolf.twin(2) == Boolf('1000')
    assert boolf.twin(3) == Boolf('1000 0000')

    boolf = Boolf('1000 1001')
    assert boolf.twin() == boolf.twin(3) == Boolf('1111 0001')
    assert boolf.twin(4) == Boolf('1111 0001 0000 0000')

    boolf = Boolf('1001')
    assert boolf.twin() == boolf.twin(2) == Boolf('1110')
    assert boolf.twin(3) == Boolf('1110 0000')
    assert boolf.twin(4) == Boolf('1110 0000 0000 0000')
