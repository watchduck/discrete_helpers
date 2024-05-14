from . import is_multisubset, multiset_to_distri


def test_is_multisubset():

    assert is_multisubset(
        {'a': 123, 'b': 99},
        {'a': 123, 'b': 99}
    )

    assert is_multisubset(
        {'a': 123, 'b': 99},
        {'a': 123, 'b': 100}
    )

    assert not is_multisubset(
        {'a': 123, 'b': 100},
        {'a': 123, 'b': 99}
    )

    assert is_multisubset(
        {'a': 123},
        {'a': 123, 'b': 99}
    )

    assert not is_multisubset(
        {'a': 123, 'b': 99},
        {'a': 123}
    )


def test_multiset_to_distri():

    values = [5, 2, 1]
    assert multiset_to_distri({1: 4, 2: 3, 5: 1}, values) == [1, 3, 4]
    assert multiset_to_distri({5: 3}, values) == [3, 0, 0]
