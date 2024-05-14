from discretehelpers.a import abbrev_testing as abbrev, make_atompatterns
from discretehelpers.binv import Binv

from discretehelpers.a import make_linear_binv
from discretehelpers.ex import ArgValueError, ArgComboError, ArgTooBigError


def test():
    assert make_linear_binv(0, 1) == Binv('00')
    assert make_linear_binv(1, 1) == Binv('01')

    assert make_linear_binv(3, 2, False) == Binv('0110')
    assert make_linear_binv(3, 2, True) == Binv('1001')

    assert make_linear_binv(3, 3) == Binv('0110 0110')

    assert make_linear_binv(3, 4) == Binv('0110 0110 0110 0110')
    assert make_linear_binv(10, 4) == Binv('0011 0011 1100 1100')
    assert make_linear_binv(15, 4) == Binv('0110 1001 1001 0110')
    assert make_linear_binv(15, 4, True) == Binv('1001 0110 0110 1001')

    assert make_linear_binv(0, 4, False) == Binv('0000 0000 0000 0000')
    assert make_linear_binv(0, 4, True)  == Binv('1111 1111 1111 1111')

    assert make_linear_binv(7, 4, False) == Binv('0110 1001 0110 1001')
    assert make_linear_binv(7, 4, True)  == Binv('1001 0110 1001 0110')

    assert make_linear_binv(12, 4, False) == Binv('0000 1111 1111 0000')
    assert make_linear_binv(12, 4, True)  == Binv('1111 0000 0000 1111')


def test_leader_quadrant():
    assert make_linear_binv(leader=0, quadrant=0, arity=3) == Binv('0000 0000')
    assert make_linear_binv(leader=1, quadrant=0, arity=3) == Binv('0110 0110')
    assert make_linear_binv(leader=2, quadrant=0, arity=3) == Binv('0101 1010')
    assert make_linear_binv(leader=3, quadrant=0, arity=3) == Binv('0011 1100')

    assert make_linear_binv(leader=0, quadrant=1, arity=3) == Binv('1010 1010')
    assert make_linear_binv(leader=1, quadrant=1, arity=3) == Binv('1100 1100')
    assert make_linear_binv(leader=2, quadrant=1, arity=3) == Binv('1111 0000')
    assert make_linear_binv(leader=3, quadrant=1, arity=3) == Binv('1001 0110')

    assert make_linear_binv(leader=0, quadrant=2, arity=3) == Binv('0101 0101')
    assert make_linear_binv(leader=1, quadrant=2, arity=3) == Binv('0011 0011')
    assert make_linear_binv(leader=2, quadrant=2, arity=3) == Binv('0000 1111')
    assert make_linear_binv(leader=3, quadrant=2, arity=3) == Binv('0110 1001')

    assert make_linear_binv(leader=0, quadrant=3, arity=3) == Binv('1111 1111')
    assert make_linear_binv(leader=1, quadrant=3, arity=3) == Binv('1001 1001')
    assert make_linear_binv(leader=2, quadrant=3, arity=3) == Binv('1010 0101')
    assert make_linear_binv(leader=3, quadrant=3, arity=3) == Binv('1100 0011')


def test_raise():
    abbrev(ArgValueError, [
        lambda: make_linear_binv(0, 0),
        lambda: make_linear_binv(1, 0),
        lambda: make_linear_binv(14, 4, prefab_atom_patterns=make_atompatterns(3)),
        lambda: make_linear_binv(14, 4, prefab_atom_patterns=make_atompatterns(5))
    ])

    abbrev(ArgTooBigError, [
        lambda: make_linear_binv(2, 1),
        lambda: make_linear_binv(16, 4)
    ])

    abbrev(ArgComboError, [
        lambda: make_linear_binv(walsh=1),  # `arity` missing
        lambda: make_linear_binv(walsh=1, quadrant=1),  # `walsh` requires `parity`
        lambda: make_linear_binv(leader=1, parity=1),  # `leader` requires `quadrant`
    ])