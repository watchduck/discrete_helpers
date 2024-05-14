from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.set_part import SetPart

from .ex import *


finest = SetPart()
setpart = SetPart([[1, 3], [5, 9]])


def test():
    assert finest.blocks_with_singletons() == []
    assert finest.blocks_with_singletons(4) == finest.blocks_with_singletons(length=4) \
           == finest.blocks_with_singletons(elements={0, 1, 2, 3}) == [[0], [1], [2], [3]]

    assert setpart.blocks_with_singletons()          == [[0], [1, 3], [2], [4], [5, 9], [6], [7], [8]            ]
    assert setpart.blocks_with_singletons(length=12) == [[0], [1, 3], [2], [4], [5, 9], [6], [7], [8], [10], [11]]

    assert setpart.blocks_with_singletons(elements=[1,    3, 5,    9]) == [[1, 3],      [5, 9]     ]
    assert setpart.blocks_with_singletons(elements=[1,    3, 5, 7, 9]) == [[1, 3],      [5, 9], [7]]
    assert setpart.blocks_with_singletons(elements=[1, 2, 3, 5, 7, 9]) == [[1, 3], [2], [5, 9], [7]]


def test_raise():
    abbrev(TooManyArgumentsError, [
        lambda: setpart.blocks_with_singletons(length=10, elements={123}),
        lambda: setpart.blocks_with_singletons(length=0, elements={123, 456})
    ])
    abbrev(LengthMismatchError, [
        lambda: setpart.blocks_with_singletons(length=9)
    ])
    abbrev(LengthWrongTypeError, [
        lambda: setpart.blocks_with_singletons(length={123}),
        lambda: setpart.blocks_with_singletons(length=123.456)
    ])
    abbrev(ElementsMismatchError, [
        lambda: setpart.blocks_with_singletons(elements={3, 5, 9}),
        lambda: setpart.blocks_with_singletons(elements={1, 3, 9}),
        lambda: setpart.blocks_with_singletons(elements={1, 3, 5})
    ])
    abbrev(ElementsWrongTypeError, [
        lambda: setpart.blocks_with_singletons(elements=123),
        lambda: setpart.blocks_with_singletons(elements=(1, 2, 3))
    ])
