import pytest
from discretehelpers.a import abbrev_testing as abbrev

from . import key_tuples

from .ex import ItemNotContainerFail, ArgNotContainerError


# example stuff

class SomeClass:
    def __init__(self):
        self.something = 999


def some_function():
    return 'something'


some_set = {1, 2, 3}
some_tuple = (1, 2, 3)

non_containers = [0, 123, 'abc', '', True, False, SomeClass, SomeClass(), some_set, some_tuple, some_function]

example1 = [
    [1, 2, 3, 4, 5],
    [1, 2, 3],
    [
        [10, 11, 12, 13],
        [10, 11, 12],
        [
            [123, 123, 123],
            [123, 123]
        ]
    ]
]
expected1 = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 1), (1, 2),
    (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 0, 3),
    (2, 1, 0), (2, 1, 1), (2, 1, 2),
    (2, 2, 0, 0), (2, 2, 0, 1), (2, 2, 0, 2),
    (2, 2, 1, 0), (2, 2, 1, 1)
]

example2 = {
    'a': ['a', 'a', 'a'],
    'b': {
        'x': 123,
        'y': 123,
        'z': ['foo', 'bar'],
        'nope': [list(), dict()],
    }
}
expected2 = [
    ('a', 0), ('a', 1), ('a', 2),
    ('b', 'x'), ('b', 'y'),
    ('b', 'z', 0), ('b', 'z', 1),
    ('b', 'nope', 0), ('b', 'nope', 1)
]

example3 = example1 + [example2]
expected3 = expected1 + [tuple([3] + list(_)) for _ in expected2]


# direct tests

def test_containers():
    assert key_tuples(list()) == key_tuples(dict()) == list()
    assert key_tuples([123, []]) == [(0,), (1,)]
    assert key_tuples([10, 11, 12]) == key_tuples({0: 'a', 1: 'b', 2: 'c'}) == [(0,), (1,), (2,)]
    assert key_tuples({'a': 123, 'b': list(), 'c': dict(), 'd': set(), 'e': {'x': [1, 2, 3], 'y': some_set, 'z': some_tuple}}) \
           == [('a',), ('b',), ('c',), ('d',), ('e', 'x', 0), ('e', 'x', 1), ('e', 'x', 2), ('e', 'y'), ('e', 'z')]
    assert key_tuples([[10, 11, 12], [200, 300]]) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
    assert key_tuples([[1, 2, 3], {'a': 1, 'b': {'x': 123, 'y': 234}}]) == [(0, 0), (0, 1), (0, 2), (1, 'a'), (1, 'b', 'x'), (1, 'b', 'y')]
    assert key_tuples(non_containers) == [(i,) for i in range(len(non_containers))]
    assert key_tuples(list()) == key_tuples(dict()) == []
    assert key_tuples(example1) == expected1
    assert key_tuples(example2) == expected2
    assert key_tuples(example3) == expected3


@pytest.mark.parametrize('candidate', non_containers)
def test_raise(candidate):
    with pytest.raises(ArgNotContainerError):
        key_tuples(candidate)


# test as use case (compare README)

primes_to_multiples = {
    3: [9, 33, 300],
    5: [10, 25, 50],
    7: [14, 49]
}
key_pairs = key_tuples(primes_to_multiples)


def test_key_pairs():
    assert key_pairs == [
        (3, 0), (3, 1), (3, 2),
        (5, 0), (5, 1), (5, 2),
        (7, 0), (7, 1)
    ]


@pytest.mark.parametrize('pair', key_pairs)
def test_use_case(pair):
    prime, key_to_multiple = pair
    multiple = primes_to_multiples[prime][key_to_multiple]
    assert multiple % prime == 0
