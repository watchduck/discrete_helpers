from discretehelpers.a import abbrev_testing as abbrev

from . import reverse_cartesean_product


example_pairs = [(0, 0), (0, 1), (0, 6), (0, 7), (3, 0), (3, 1), (3, 6), (3, 7)]


def test():

    left = (0, 3)
    right = (0, 1, 6, 7)
    assert reverse_cartesean_product(example_pairs) == (left, right)

    assert reverse_cartesean_product([]) == ((), ())


def test_error():

    abbrev(AssertionError, [
        lambda: reverse_cartesean_product([(0, 1), (1, 0)]),
        lambda: reverse_cartesean_product(example_pairs + [(3, 8)])
    ])
