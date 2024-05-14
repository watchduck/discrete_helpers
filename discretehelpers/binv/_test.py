import pytest

from discretehelpers.set_part import SetPart
from discretehelpers.a import abbrev_testing as abbrev

from .a.to_pretty_string.ex import PrettyLengthError
from . import Binv
from .ex import *


@pytest.mark.parametrize(
    'candidate',
    [[0, 1], (0, 1), [False, True], (False, True), '01', '0 1', Binv('01')],
    ids=str
)
def test_vector_variants(candidate):
    binv = Binv(vector=candidate)
    assert binv.vector == [False, True]
    assert binv.string == binv.pretty == '01'
    assert binv.exposet == {1}
    assert binv.intval == 2
    assert binv.complement == ~binv == Binv('10')
    assert binv.length == 2
    assert binv.weight == 1
    assert binv[0] is False
    assert binv[1] is True
    assert sum(binv) == 1
    assert len(binv) == 2
    assert [binv.has_index(_) for _ in range(3)] == [False, True, False]
    assert Binv('0001').reverse == Binv('1000')


def test_methods():
    binv = Binv('0101')
    assert binv.intval == 10
    assert binv.exposet == {1, 3}

    assert binv.complement == ~binv == Binv('1010')
    assert binv.length == 4
    assert binv.weight == 2

    assert sum(binv) == 2
    assert len(binv) == 4

    assert [binv.has_index(_) for _ in range(6)] == [False, True, False, True, False, False]

    assert Binv('0001').flip_bit(1) == Binv('0101')

    assert Binv('01') + Binv('10') == Binv('0110')


def test_raise():
    abbrev(ArgumentError, [
        lambda: Binv(vector=(0, 1), length=2),  # `length` is useless here (even if correct)
        lambda: Binv('0 1', length=2),
        lambda: Binv('0 1', intval=1),
        lambda: Binv()
    ])
    abbrev(LengthError, [
        lambda: Binv(intval=10, length=3),
        lambda: Binv(intval=1, length=0),
        lambda: Binv(exposet={0, 1, 2}, length=2)
    ])
    abbrev(VectorTypeError, [
        lambda: Binv(0),
        lambda: Binv(1),
    ])
    abbrev(VectorEntryError, [
        lambda: Binv([0, 1, 2]),
        lambda: Binv([-1]),
        lambda: Binv('012'),
        lambda: Binv('-')
    ])
    abbrev(IntvalError, [
        lambda: Binv(intval='5'),
        lambda: Binv(intval=-5),
        lambda: Binv(intval=5.0),
    ])
    abbrev(IndicesTypeError, [
        lambda: Binv(exposet='123'),
        lambda: Binv(exposet={'a': 1, 'b': 2, 'c': 3}),
        lambda: Binv(exposet=123)
    ])
    abbrev(IndicesEntryError, [
        lambda: Binv(exposet=['1', '2', '3']),
        lambda: Binv(exposet={'1', '2', '3'}),
        lambda: Binv(exposet=[[1], [2], [3]])
    ])


def test_intval_to_vector():
    abbrev('0101', [
        Binv(intval=10).string,
        Binv(intval=10, length=4).string
    ])

    assert Binv(intval=10, length=6).string == '010100'
    assert Binv(intval=10, minimal_length=3).string == '0101'
    assert Binv(intval=3, minimal_length=3).string == '110'


def test_to_exposet():  # 0,   1,   2,   3,      4,   5,      6,      7,         8,   9,      10,     11,        12,     13,        14,        15,           16
    expected_results = [set(), {0}, {1}, {0, 1}, {2}, {0, 2}, {1, 2}, {0, 1, 2}, {3}, {0, 3}, {1, 3}, {0, 1, 3}, {2, 3}, {0, 2, 3}, {1, 2, 3}, {0, 1, 2, 3}, {4}]
    for i, expected_result in enumerate(expected_results):
        binv = Binv(intval=i)
        assert binv.intval == i
        assert binv.exposet == expected_results[i]


def test_from_exposet():
    assert Binv(exposet={0, 2, 3}) == Binv(exposet=[0, 2, 3]) == Binv(intval=13)
    assert Binv(exposet={0, 2, 3}, length=6).string == '101100'
    assert Binv(exposet=[]).string == ''
    assert Binv(exposet=[], length=5).string == '00000'

    assert Binv(exposet=[1, 3], length=6).string == '010100'
    assert Binv(exposet=[1, 3], minimal_length=3).string == '0101'
    assert Binv(exposet=[0, 1], minimal_length=3).string == '110'


def test_eq():
    assert Binv('01') == Binv([False, True])
    assert Binv(intval=0) == Binv([]) == Binv('')
    assert Binv(intval=13) == Binv('1011')
    assert Binv(intval=13, length=6) == Binv('101100')


def test_pretty():
    abbrev(PrettyLengthError, [
        lambda: Binv([True, False, True]).pretty,
        lambda: Binv('10101').pretty
    ])
    abbrev('0101', [
        Binv(intval=10, length=4).pretty,
        Binv('0101').pretty
    ])
    abbrev('0000 0001', [
        Binv(intval=128, length=8).pretty,
        Binv(' 00 00 00 01 ').pretty
    ])


def test_changes():
    assert Binv('0011001').changes == 3
    assert Binv([False, True]).changes == 1


def test_bitwise():
    assert Binv('0101') & Binv('0011') == Binv('0001')
    assert Binv('0101') | Binv('0011') == Binv('0111')
    assert Binv('0101') ^ Binv('0011') == Binv('0110')

    assert Binv('0').bitwise_smaller(Binv('1'))
    assert not Binv('0').bitwise_smaller(Binv('0'))


@pytest.mark.parametrize('s', ['', '0', '1', '01', '0110101', '0000111100001111'])
def test_str_short(s):
    assert Binv(s).string == s
    assert str(Binv(s)) == f"Binv('{s}')"


@pytest.mark.parametrize('pair', [
    ('00000 01010 00011 10000', 16),
    ('0110 0000 0000 1111  1111 0000 0100 0000', 26),
    ('0110 0000 0000 1111  1111 0000 0100 0000  0000 1111 0000 0000  1010 0101 1010 0000', 59)
])
def test_str_long(pair):
    string_with_gaps, required_length = pair
    binv = Binv(string_with_gaps)
    length = binv.length
    assert binv.string == string_with_gaps.replace(' ', '')
    assert binv.required_length == required_length
    assert str(binv) == f"Binv(exposet={sorted(binv.exposet)}, length={length})"
    assert str(~binv) == f"~Binv(exposet={sorted(binv.exposet)}, length={length})"


def test_str_explicit():
    binv = Binv('0000 1111 1111 0000  0000 0000 0000 1111')
    assert str( binv) ==  'Binv(exposet=[4, 5, 6, 7, 8, 9, 10, 11, 28, 29, 30, 31], length=32)'
    assert str(~binv) == '~Binv(exposet=[4, 5, 6, 7, 8, 9, 10, 11, 28, 29, 30, 31], length=32)'


def test_set_part():
    assert Binv('0101').set_part == Binv('1010').set_part == SetPart([[0, 2], [1, 3]])
    assert Binv('01010').set_part == Binv('10101').set_part == SetPart([[0, 2, 4], [1, 3]])
