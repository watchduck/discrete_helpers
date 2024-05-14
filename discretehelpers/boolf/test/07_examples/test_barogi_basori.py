from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples import barogi, basori, basori_fs


def test_barogi():
    assert barogi == Boolf('1110', [0, 3])
    assert barogi.fullspots == {0, 1, 2}
    assert barogi.inflated_fullspots([0, 1, 2, 3]) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14}


def test_basori():
    assert basori == Boolf('1110 0010', [0, 3, 4])
    assert basori.fullspots == {0, 1, 2, 6}
    assert basori.inflated_fullspots(list(range(5))) == basori_fs
