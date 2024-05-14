from discretehelpers.a import inventory_dict


def test_list():
    assert inventory_dict([2, 1, 2, 30, 2, 7, 30]) == {1: 1, 2: 3, 7: 1, 30: 2}
    assert inventory_dict(['b', 'a', 'a']) == {'a': 2, 'b': 1}


def test_dict():
    arg = {
        55: 5,
        77: 7,
        555: 5,
        777: 7,
        7777: 7
    }
    assert inventory_dict(arg) == {
        5: 2,
        7: 3
    }
