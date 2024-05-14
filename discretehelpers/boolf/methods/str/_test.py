from discretehelpers.boolf import Boolf


def test():

    assert str(Boolf('0110 1100')) == "Boolf('0110 1100')"

    boolf = Boolf('0110 1100 0000 0000  0011 0011 1100 1100')
    boolf_string = 'Boolf(fullspots=[1, 2, 4, 5, 18, 19, 22, 23, 24, 25, 28, 29], arity=5)'

    assert str(boolf) == boolf_string
    assert str(~boolf) == '~'  + boolf_string

    assert str(Boolf(fullspots={1, 2, 3}, arity=5)) == 'Boolf(fullspots=[1, 2, 3], arity=5)'
    assert str(Boolf(fullspots={1, 2, 3}, atomvals=[77, 88, 99])) == "Boolf('0111 0000', [77, 88, 99])"
    assert str(Boolf(fullspots={1, 2, 3}, atomvals=[55, 66, 77, 88, 99])) \
        == 'Boolf(fullspots=[1, 2, 3], atomvals=[55, 66, 77, 88, 99])'
