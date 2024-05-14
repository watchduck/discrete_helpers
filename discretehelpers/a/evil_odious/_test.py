from discretehelpers.a import index_to_evil, index_to_odious, evil_to_index, odious_to_index, \
    abbrev_testing as abbrev

from discretehelpers.ex import ArgValueError


def test():
    evil_numbers = [0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29, 30]
    odious_numbers = [1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28, 31]

    for i, evil in enumerate(evil_numbers):
        assert index_to_evil(i) == evil
        assert evil_to_index(evil) == i

    for i, odious in enumerate(odious_numbers):
        assert index_to_odious(i) == odious
        assert odious_to_index(odious) == i


def test_raise():
    abbrev(ArgValueError, [
        lambda: odious_to_index(0),
        lambda: evil_to_index(1),
        lambda: evil_to_index(-3)
    ])

    abbrev(TypeError, [
        lambda: index_to_evil(.5),
        lambda: index_to_odious(.5),
        lambda: evil_to_index(.5),
        lambda: odious_to_index(.5)
    ])
