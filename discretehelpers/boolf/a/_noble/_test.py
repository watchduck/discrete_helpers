from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf.a import (
    index_to_noble, noble_to_index,
    noble_to_royal, noble_to_quadrant, noble_to_royal_and_quadrant as n2rq, noble_to_king_index_and_quadrant as n2kq
)
from discretehelpers.ex import ArgTooBigError, ArgValueError


arity_to_nobles = {
    0: [0],
    1: [0, 2],
    2: [0, 6, 8, 14],
    3: [0, 30, 40, 54, 72, 86, 96, 126, 128, 158, 168, 182, 200, 214, 224, 254]
}


def test_index():

    for arity in [0, 1, 2, 3]:

        nobles = arity_to_nobles[arity]

        for i, noble in enumerate(nobles):
            assert index_to_noble(i, arity) == noble
            assert noble_to_index(noble, arity) == i


def test_royal_king_quadrant():

    assert [(n2rq(_, 0), n2kq(_, 0)) for _ in arity_to_nobles[0]] == [
        ((0, 0), (0, 0))
    ]

    assert [(n2rq(_, 1), n2kq(_, 1)) for _ in arity_to_nobles[1]] == [
        ((0, 0), (0, 0)),
        ((0, 3), (0, 3))
    ]

    assert [(n2rq(_, 2), n2kq(_, 2)) for _ in arity_to_nobles[2]] == [
        ((0, 0), (0, 0)),
        ((0, 1), (0, 1)),
        ((0, 2), (0, 2)),
        ((0, 3), (0, 3))
    ]

    assert [(n2rq(_, 3), n2kq(_, 3)) for _ in arity_to_nobles[3]] == [
        ((0, 0), (0, 0)),
        ((96, 1), (2, 1)),
        ((40, 0), (2, 0)),
        ((72, 1), (2, 1)),

        ((72, 0), (2, 0)),
        ((40, 1), (2, 1)),
        ((96, 0), (2, 0)),
        ((0, 1), (0, 1)),

        ((0, 2), (0, 2)),
        ((96, 3), (2, 3)),
        ((40, 2), (2, 2)),
        ((72, 3), (2, 3)),

        ((72, 2), (2, 2)),
        ((40, 3), (2, 3)),
        ((96, 2), (2, 2)),
        ((0, 3), (0, 3))
    ]


def test_raise():

    abbrev(ArgTooBigError, [
        # index too big
        lambda: index_to_noble(2, 1),
        lambda: index_to_noble(4, 2),
        lambda: index_to_noble(16, 3),

        # alleged noble too big
        lambda: noble_to_index(3, 1),
        lambda: noble_to_index(15, 2),
        lambda: noble_to_index(255, 3),

        lambda: noble_to_royal(15, 2),
        lambda: noble_to_quadrant(15, 2),
        lambda: noble_to_royal(255, 3),
        lambda: noble_to_quadrant(255, 3)
    ])

    # not noble
    abbrev(ArgValueError, [
        lambda: noble_to_index(1, 1),
        lambda: noble_to_index(12, 2),
        lambda: noble_to_index(123, 3),

        lambda: noble_to_royal(1, 1),
        lambda: noble_to_royal(12, 2),
        lambda: noble_to_royal(123, 3),

        lambda: noble_to_quadrant(1, 1),
        lambda: noble_to_quadrant(12, 2),
        lambda: noble_to_quadrant(123, 3)
    ])
