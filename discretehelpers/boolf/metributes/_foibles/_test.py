from discretehelpers.boolf import Boolf
from discretehelpers.binv import Binv

from discretehelpers.a import int_to_weight


def test_odd():
    assert Boolf('0').is_odd == Boolf('01', [999]).is_odd == Boolf('0111', [88, 99]).is_odd == False
    assert Boolf('1').is_odd == Boolf('10', [999]).is_odd == Boolf('1001', [88, 99]).is_odd == True

    for i in range(256):
        boolf = Boolf(zhe=i)
        assert int(boolf.is_odd) == i % 2

        # The oddness of the Boolean function equals that of its Zhegalkin index.
        boolf = Boolf(Binv(intval=i, length=8))
        assert int(boolf.is_odd) == i % 2


def test_odious():
    assert Boolf('0').is_odious == Boolf('10', [999]).is_odious == Boolf('1110', [88, 99]).is_odious == False
    assert Boolf('1').is_odious == Boolf('01', [999]).is_odious == Boolf('1001', [88, 99]).is_odious == True

    for i in range(256):
        assert int(Boolf(zhe=i).is_odious) == int_to_weight(i) % 2


def test_ugly():
    assert not Boolf('0').is_ugly
    assert not Boolf('1').is_ugly
    assert Boolf('01').is_ugly
    assert not Boolf('0110').is_ugly
    assert Boolf('0001').is_ugly
    assert Boolf('0111').is_ugly


def test_dense_sharp():
    assert Boolf('0').dense_is_sharp == Boolf('1001', [88, 99]).dense_is_sharp == Boolf('0101 0011', [77, 88, 99]).dense_is_sharp == False
    assert Boolf('1').dense_is_sharp == Boolf('1011', [88, 99]).dense_is_sharp == Boolf('0101 0111', [77, 88, 99]).dense_is_sharp == True
