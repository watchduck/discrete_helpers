from discretehelpers.set_part import SetPart
from discretehelpers.a import inventory_partition


def test_list():

    result = inventory_partition([2, 1, 2, 30, 2, 7, 30])
    assert result == SetPart([[0, 2, 4], [3, 6]], {0, 1, 2, 3, 4, 5, 6})
    assert result.block_labels == {
        (1,): 1,
        (0, 2, 4): 2,
        (5,): 7,
        (3, 6): 30
    }

    result = inventory_partition(['b', 'a', 'a'])
    assert result == SetPart([[1, 2]], {0, 1, 2})
    assert result.block_labels == {
        (0,): 'b',
        (1, 2): 'a'
    }


def test_dict():
    arg = {
        55: 5,
        77: 7,
        555: 5,
        777: 7,
        7777: 7
    }
    result = inventory_partition(arg)
    assert result == SetPart([[55, 555], [77, 777, 7777]], {55, 77, 555, 777, 7777})
    assert result.block_labels == {
        (55, 555): 5,
        (77, 777, 7777): 7
    }
