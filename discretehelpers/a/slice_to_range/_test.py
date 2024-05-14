from discretehelpers.a import abbrev_testing as abbrev

from . import slice_to_range
from .ex import *


def test_foo():
    foo = Foo()
    assert foo[:10] == list(range(10))
    assert foo[3:10] == list(range(3, 10))
    assert foo[3:10:2] == [3, 5, 7, 9]
    abbrev(StopMissingError, [
        lambda: foo[:],
        lambda: foo[::]
    ])


def test_bar():
    bar = Bar()
    assert bar[:] == list(range(20))
    assert bar[::] == list(range(20))
    assert bar[::5] == [0, 5, 10, 15]
    assert bar[:10] == list(range(10))
    assert bar[3:10] == list(range(3, 10))
    assert bar[3:10:2] == [3, 5, 7, 9]


class Foo(object):
    def __getitem__(self, arg):
        if isinstance(arg, slice):
            return [i for i in slice_to_range(arg)]


class Bar(object):
    def __getitem__(self, arg):
        if isinstance(arg, slice):
            return [i for i in slice_to_range(arg, 20)]