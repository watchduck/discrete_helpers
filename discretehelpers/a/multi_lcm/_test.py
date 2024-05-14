from . import multi_lcm


def test():
    assert multi_lcm([2, 5]) == 10
    assert multi_lcm([2, 7, 5]) == multi_lcm([2, 14, 5]) == multi_lcm([14, 5]) == 70
    assert multi_lcm([2, 4, 3]) == 12
