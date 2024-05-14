from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf import Boolf
from discretehelpers.binv import Binv

from discretehelpers.ex import ArgValueError, ArgTypeError, ArgComboError


def test():

    assert Boolf(False) == Boolf('0')
    assert Boolf(True) == Boolf('1')

    assert Boolf('0000') == Boolf('0')
    assert Boolf('1111') == Boolf('1')

    assert Boolf('0011 0011', [77, 88, 99]) == Boolf('01', [88])
    assert Boolf(Binv('0110 0110')) == Boolf('0110')


def test_int():
    assert Boolf(1, arity=0) == Boolf('1')
    assert Boolf(1, arity=1) == Boolf('10')
    assert Boolf(1, arity=2) == Boolf('1000')
    assert Boolf(1, arity=3) == Boolf('1000 0000')

    assert Boolf(6, arity=2) == Boolf(102, arity=3) == Boolf('0110')

    assert Boolf(123, arity=3) == Boolf('1101 1110')


def test_skip():
    boolf = Boolf('1111', skip_deflation=True)
    assert boolf.atomvals == [0, 1]
    assert boolf.dense_tt == Binv('1111')
    assert boolf.fullspots == {0, 1, 2, 3}
    assert boolf.is_inflated
    assert not boolf.is_constant  # not quite true, but acceptable

    boolf = Boolf('0110 0110', skip_deflation=True)
    assert boolf.dense_tt == Binv('0110 0110')
    assert boolf.atomvals == [0, 1, 2]
    assert boolf.is_inflated

    boolf = Boolf('0110 0110', atomvals=[77, 88, 99], skip_deflation=True)
    assert boolf.atomvals == [77, 88, 99]
    assert boolf.is_inflated


def test_raise():
    abbrev(ArgTypeError, [
        lambda: Boolf(123)  # tt int requires arity
    ])

    abbrev(ArgValueError, [
        lambda: Boolf(''),
        lambda: Boolf([]),
        lambda: Boolf(Binv(''))
    ])

    abbrev(ArgComboError, [
        lambda: Boolf()
    ])
