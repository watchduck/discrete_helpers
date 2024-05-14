from discretehelpers.a import abbrev_testing as abbrev
from discretehelpers.boolf.a import symmetric_to_index

from discretehelpers.ex import ArgTooBigError, ArgValueError


sym_0 = [
    0,  # 0
    1,  # 1
]

sym_1 = [
    0,  # 00
    3,  # 11
]

sym_2 = [
    0,   # 0000
    6,   # 0110
    9,   # 1001
    15,  # 1111
]

sym_3 = [
    0,    # 0000 0000
    24,   # 0001 1000
    36,   # 0010 0100
    60,   # 0011 1100
    66,   # 0100 0010
    90,   # 0101 1010
    102,  # 0110 0110
    126,  # 0111 1110
    129,  # 1000 0001
    153,  # 1001 1001
    165,  # 1010 0101
    189,  # 1011 1101
    195,  # 1100 0011
    219,  # 1101 1011
    231,  # 1110 0111
    255,  # 1111 1111
]


def test():

    for arity in range(4):
        symmetric_integers = {0: sym_0, 1: sym_1, 2: sym_2, 3: sym_3}[arity]
        for i, n in enumerate(symmetric_integers):
            assert symmetric_to_index(n, arity) == i


def test_raise():

    # too big for arity
    abbrev(ArgTooBigError, [
        lambda: symmetric_to_index(2, 0),
        lambda: symmetric_to_index(4, 1),
        lambda: symmetric_to_index(16, 2),
        lambda: symmetric_to_index(256, 3)
    ])

    # not symmetric
    abbrev(ArgValueError, [
        lambda: symmetric_to_index(1, 1),
        lambda: symmetric_to_index(12, 2),
        lambda: symmetric_to_index(123, 3)
    ])
