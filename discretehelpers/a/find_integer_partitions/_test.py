from . import find_integer_partitions


def test():
    assert find_integer_partitions(4) == {(4,), (1, 1, 2), (2, 2), (1, 3), (1, 1, 1, 1)}
    assert find_integer_partitions(5) == {(5,), (1, 1, 3), (1, 4), (2, 3), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)}
