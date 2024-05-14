from discretehelpers.boolf import Boolf

from discretehelpers.a import abbrev_testing as abbrev, make_linear_boolf

from discretehelpers.ex import ArgValueError, ArgComboError


def test():
    assert make_linear_boolf(0, False) == Boolf('0') == make_linear_boolf(0)
    assert make_linear_boolf(0, True)  == Boolf('1')

    assert make_linear_boolf(7, False) == Boolf('0110 1001') == make_linear_boolf(7)
    assert make_linear_boolf(7, True)  == Boolf('1001 0110')

    assert make_linear_boolf(12, False) == Boolf('0110', [2, 3]) == make_linear_boolf(12)
    assert make_linear_boolf(12, True)  == Boolf('1001', [2, 3])


def test_leader_quadrant():
    assert make_linear_boolf(leader=0, quadrant=0) == Boolf('0')
    assert make_linear_boolf(leader=1, quadrant=0) == Boolf('0110')
    assert make_linear_boolf(leader=2, quadrant=0) == Boolf('0101 1010')
    assert make_linear_boolf(leader=3, quadrant=0) == Boolf('0011 1100')

    assert make_linear_boolf(leader=0, quadrant=1) == Boolf('1010')
    assert make_linear_boolf(leader=1, quadrant=1) == Boolf('1100')
    assert make_linear_boolf(leader=2, quadrant=1) == Boolf('1111 0000')
    assert make_linear_boolf(leader=3, quadrant=1) == Boolf('1001 0110')

    assert make_linear_boolf(leader=0, quadrant=2) == Boolf('0101')
    assert make_linear_boolf(leader=1, quadrant=2) == Boolf('0011')
    assert make_linear_boolf(leader=2, quadrant=2) == Boolf('0000 1111')
    assert make_linear_boolf(leader=3, quadrant=2) == Boolf('0110 1001')

    assert make_linear_boolf(leader=0, quadrant=3) == Boolf('1')
    assert make_linear_boolf(leader=1, quadrant=3) == Boolf('1001')
    assert make_linear_boolf(leader=2, quadrant=3) == Boolf('1010 0101')
    assert make_linear_boolf(leader=3, quadrant=3) == Boolf('1100 0011')


def test_raise():
    abbrev(ArgValueError, [
        lambda: make_linear_boolf(leader=1, quadrant=4),  # quadrant not in range(4)
    ])

    abbrev(ArgComboError, [
        lambda: make_linear_boolf(walsh=1, quadrant=1),  # `walsh` requires `parity`
        lambda: make_linear_boolf(leader=1, parity=1),  # `leader` requires `quadrant`
        lambda: make_linear_boolf(leader=1),  # `leader` requires `quadrant`
    ])
