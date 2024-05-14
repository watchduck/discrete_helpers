from discretehelpers.a import abbrev_testing as abbrev

from . import sort_together
from .ex import *


def test_2_args():

    natural = [0, 1, 2]
    assert sort_together([2, 0, 1], natural) == (natural, [1, 2, 0])


def test_3_args():

    a = [ 2,   3,   2,   3,   3 ]
    b = ['x', 'x', 'x', 'z', 'y']
    c = [33,  33,  22,  11,  22 ]
    a, b, c = sort_together(a, b, c)
    assert a == [ 2,   2,   3,   3,   3 ]
    assert b == ['x', 'x', 'x', 'y', 'z']
    assert c == [22,  33,  33,  22,  11 ]
