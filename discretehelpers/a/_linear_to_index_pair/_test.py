from discretehelpers.binv import Binv
from discretehelpers.boolf import Boolf

from discretehelpers.a import (
    linear_to_walsh_and_oddness as f,
    linear_to_leader_and_quadrant as g,
    abbrev_testing as abbrev,
    int_to_weight,
    make_linear_boolf,
    make_linear_binv
)

from discretehelpers.ex import ArgValueError
from discretehelpers.binv.ex import VectorEntryError
from discretehelpers.a.walsh_function_to_index.ex import NotWalshRowError


def test():
    assert f('0') == f('00') == f(Binv('0')) == f(Boolf('0')) == (0, 0)
    assert f('1') == f('11') == f(Binv('1')) == f(Boolf('1')) == (0, 1)

    assert f('0110 0110') == f(Binv('0110 0110')) == f(Boolf('0110 0110')) == (3, 0)
    assert f('1001 1001') == f(Binv('1001 1001')) == f(Boolf('1001 1001')) == (3, 1)

    string = '1001 0110 0110 1001'
    binv = Binv(string)
    boolf = Boolf(string)
    list_bool = binv.vector
    list_int = [int(_) for _ in list_bool]
    tuple_bool = tuple(list_bool)
    tuple_int = tuple(list_int)
    assert f(string) == f(binv) == f(boolf) == f(list_bool) == f(list_int) == f(tuple_bool) == f(tuple_int) == (15, 1)


def test_leader_quadrant():
    for is_odd in range(2):
        for walsh_index in range(32):
            expected_leader = walsh_index >> 1
            walsh_index_is_odious = int_to_weight(walsh_index) % 2
            is_odious = walsh_index_is_odious ^ is_odd
            expected_quadrant = is_odd + 2 * is_odious
            linear_boolf = make_linear_boolf(walsh_index, is_odd)
            linear_binv = make_linear_binv(walsh_index, 5, is_odd)
            assert g(linear_binv) == g(linear_boolf) == (expected_leader, expected_quadrant)


def test_raise():

    abbrev(VectorEntryError, [
        lambda: f([1, 2, 3]),
        lambda: g([1, 2, 3]),
    ])

    abbrev(ArgValueError, [
        lambda: f({0, 1}),
        lambda: g({0, 1})
    ])

    abbrev(NotWalshRowError, [
        lambda: f('1011'),
        lambda: f('1000 0001'),
        lambda: g('1011'),
        lambda: g('1000 0001')
    ])
