from discretehelpers.binv import Binv
from discretehelpers.boolf.examples import savona, dakota


def test():

    assert savona.fissions == [
        [Binv('0000 0111'), Binv('1000 1000')],
        [Binv('0100 0110'), Binv('0000 1010')],
        [Binv('0100 0110'), Binv('0000 1010')],
        [Binv('0100 0000'), Binv('0110 1010')]
    ]

    assert savona.fissions_layered == [
        [((0,), (0, 0, 0), (0, 1, 1), (1,)), ((1,), (0, 0, 1), (0, 0, 0), (0,))],
        [((0,), (1, 0, 0), (0, 1, 1), (0,)), ((0,), (0, 0, 1), (0, 0, 1), (0,))],
        [((0,), (1, 0, 0), (0, 1, 1), (0,)), ((0,), (0, 0, 1), (0, 0, 1), (0,))],
        [((0,), (1, 0, 0), (0, 0, 0), (0,)), ((0,), (1, 1, 1), (0, 0, 1), (0,))]
    ]

    ##########################################################################################

    assert dakota.fissions == [
        [Binv('1111 1000'), Binv('1101 1000')],
        [Binv('1110 1100'), Binv('1111 0000')],
        [Binv('1111 1100'), Binv('1011 0000')],
        [Binv('1111 1011'), Binv('1100 0000')]
    ]

    assert dakota.fissions_layered == [
        [((1,), (1, 1, 1), (1, 0, 0), (0,)), ((1,), (1, 0, 1), (1, 0, 0), (0,))],
        [((1,), (1, 1, 1), (0, 1, 0), (0,)), ((1,), (1, 1, 0), (1, 0, 0), (0,))],
        [((1,), (1, 1, 1), (1, 1, 0), (0,)), ((1,), (0, 1, 0), (1, 0, 0), (0,))],
        [((1,), (1, 1, 1), (1, 0, 1), (1,)), ((1,), (1, 0, 0), (0, 0, 0), (0,))]
    ]
