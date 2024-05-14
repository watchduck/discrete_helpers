from . import reduce_period, block_repeats


def test_block_repeats():

    assert block_repeats({0: 1, 1: 5, 5: 0}, 6, 2, True) == 'no1'
    assert block_repeats({0: 1, 1: 5, 5: 0}, 6, 3, True) == 'no2'

    assert block_repeats({0: 1, 1: 4, 4: 5, 5: 0}, 6, 2, True) == 'no2'
    assert block_repeats({0: 1, 1: 4, 4: 5, 5: 0}, 6, 3, True) == 'no1'

    assert block_repeats({0: 1, 1: 2, 2: 0,   3: 5, 5: 4, 4: 3}, 6, 3, True) == 'no3'

    assert block_repeats({0: 1, 1: 0,   3: 4, 4: 3}, 6, 2, True) == 'yes'
    assert block_repeats({0: 1, 1: 0,   2: 3, 3: 2,   4: 5, 5: 4}, 6, 3, True) == 'yes'
    assert block_repeats({0: 1, 1: 0,   2: 3, 3: 2,   5: 4, 4: 5}, 6, 3, True) == 'yes'
    assert block_repeats({1: 2, 2: 3, 3: 1,   51: 52, 52: 53, 53: 51}, 100, 2, True) == 'yes'
    assert block_repeats({1: 2, 2: 3, 3: 1,   51: 53, 53: 52, 52: 51}, 100, 2, True) == 'no3'


def test_reduce_period():

    assert reduce_period({0: 1, 1: 0, 2: 3, 3: 2}, 4) == ({0: 1, 1: 0}, 2)
    assert reduce_period({0: 1, 1: 2, 2: 3, 3: 0}, 4) == ({0: 1, 1: 2, 2: 3, 3: 0}, 4)
    assert reduce_period({1: 2, 2: 1, 4: 5, 5: 7, 7: 5,   51: 52, 52: 51, 54: 55, 55: 57, 57: 55}, 100) == ({1: 2, 2: 1, 4: 5, 5: 7, 7: 5}, 50)
