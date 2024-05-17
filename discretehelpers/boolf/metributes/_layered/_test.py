from discretehelpers.binv import Binv
from discretehelpers.boolf.examples import medusa, sapigi, sarina


def test_tt():

    assert medusa.layered_tt == (
        (1,),
        (1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1),
        (1, 0, 0, 1),
        (0,)
    )

    assert sapigi.layered_tt == (
        (0,),
        (1, 0, 0, 1),
        (1, 1, 0, 1, 1, 1),
        (1, 0, 0, 1),
        (0,)
    )

    assert [Binv(_) for _ in sarina.layered_tt] == [
        Binv('1'),
        Binv('11110000'),
        Binv('1010100001000000000000000000'),
        Binv('00000000100000000000000000000000000000000000000000000000'),
        Binv('0000000000000000000000000000010000000000000000000000000000010000000000'),
        Binv('00000000000000000000000000000000000000000000000000000000'),
        Binv('0000000000000000000000000000'),
        Binv('00000000'),
        Binv('0')
    ]


def test_weight():

    assert medusa.layered_weight == (1, 4, 6, 2, 0)

    assert sapigi.layered_weight == (0, 2, 5, 2, 0)

    assert sarina.layered_weight    == (1, 4,  4,  1,  2,  0,  0, 0, 0)
    assert (~sarina).layered_weight == (0, 4, 24, 55, 68, 56, 28, 8, 1)
    # row 8 of Pascal's triangle:      (1, 8, 28, 56, 70, 56, 28, 8, 1)
