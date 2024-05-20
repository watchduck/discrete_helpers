from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf import Boolf

from discretehelpers.ex import ArgMismatchError, ArgComboError


def test():

    f = Boolf('0')
    assert Boolf(fullspots=[], arity=0) == f
    assert Boolf(fullspots=[], arity=1) == f
    assert Boolf(fullspots=[], arity=2) == f
    assert Boolf(fullspots=[], atomvals=[]) == f
    assert Boolf(fullspots=[], atomvals=[123]) == f
    assert Boolf(fullspots=[], atomvals=[123, 456]) == f

    t = Boolf('1')
    assert Boolf(fullspots=[0], atomvals=[]) == t
    assert Boolf(fullspots=[0, 1], atomvals=[1]) == t
    assert Boolf(fullspots=[0, 1, 2, 3], atomvals=[0, 1]) == t
    assert Boolf(fullspots=[0, 1, 2, 3, 4, 5, 6, 7], atomvals=[123, 456, 789]) == t

    root = '0101 0100'
    assert Boolf(fullspots={1, 3, 5}, atomvals=[0, 1, 2]) == Boolf(root)
    assert Boolf(fullspots={1, 3, 5}, arity=3) == Boolf(root)
    assert Boolf(fullspots={1, 3, 5}, atomvals=[77, 88, 99]) == Boolf(root, [77, 88, 99])

    root += '0000 0000'
    assert Boolf(fullspots={1, 3, 5}, arity=4) == Boolf(root)


def test_raise():

    abbrev(ArgComboError, [
        lambda: Boolf(fullspots=[123, 456], atomvals=[3, 4, 5], arity=12345)
    ])

    abbrev(ArgMismatchError, [
        lambda: Boolf(fullspots=[123], atomvals=[])
    ])
