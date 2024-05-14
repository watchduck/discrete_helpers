from discretehelpers.a import abbrev_testing as abbrev
from discretehelpers.binv import Binv

from . import vector_zip_apart
from .ex import *


def test_results():

    assert vector_zip_apart([10, 11, 12, 13, 14, 15], [0, 1, 0, 1, 0, 2]) == [[10, 12, 14], [11, 13], [15]]
    assert vector_zip_apart(['a', 'b', 'c'], [0, 1, 0]) == [['a', 'c'], ['b']]
    assert vector_zip_apart(Binv('0110 0101'), Binv('0000 1111')) == [Binv('0110'), Binv('0101')]


def test_raise():

    abbrev(NotListLikeError, [
        lambda: vector_zip_apart([10, 11], '01'),
        lambda: vector_zip_apart([10], {0, 1})
    ])

    abbrev(LengthError, [
        lambda: vector_zip_apart([10], (0, 1)),
        lambda: vector_zip_apart([10, 11], [0]),
        lambda: vector_zip_apart([10], []),
        lambda: vector_zip_apart([10], [0, 1])
    ])

    abbrev(NotNaturalError, [
        lambda: vector_zip_apart([10, 11], ['0', '1']),
    ])
