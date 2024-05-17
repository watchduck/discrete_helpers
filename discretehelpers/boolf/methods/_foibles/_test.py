from discretehelpers.boolf import Boolf


def test_acute():

    assert Boolf('0000 0011').is_acute(3)  # 192
    assert Boolf('1100').is_acute(3)  # 51


def test_sharp():

    assert not Boolf('0110').is_sharp(2)

    assert Boolf('0001').is_sharp(2)
    assert not Boolf('0001').is_sharp(3)
