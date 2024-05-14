from discretehelpers.boolf.examples import kovane
from discretehelpers.binv import Binv


def test():

    assert kovane.hyperfission([1, 2]) == [
        Binv('0011'),
        Binv('0110'),
        Binv('0110'),
        Binv('1100')
    ]

    assert kovane.hyperfission_walsh_spectra([1, 2]) == [
        (2, 0, -2,  0),
        (2, 0,  0, -2),
        (2, 0,  0, -2),
        (2, 0,  2,  0)]

    assert kovane.hyperfission_walsh_spectra_abs([1, 2]) == [
        (2, 0, 2, 0),
        (2, 0, 0, 2),
        (2, 0, 0, 2),
        (2, 0, 2, 0)
    ]

    assert kovane.hyperfission_walsh_spectra_layered_abs([1, 2]) == [
        ((2,), (0, 2), (0,)),
        ((2,), (0, 0), (2,)),
        ((2,), (0, 0), (2,)),
        ((2,), (0, 2), (0,))
    ]

    ####################################################################################################################

    #                                                           0  1  2  3   4  5  6  7    8  9 10  11  12  13 14 15
    assert kovane.hyperfission_walsh_spectra_zipped([1, 2]) == (2, 0, 2, 0,  2, 0, 2, 0,  -2, 0, 0, -2,  0, -2, 2, 0)

    assert kovane.hyperfission_walsh_spectra_labeled([1, 2]) == {
        (0, 1,  8,  9): [2, 0, -2,  0],
        (2, 3, 10, 11): [2, 0,  0, -2],
        (4, 5, 12, 13): [2, 0,  0, -2],
        (6, 7, 14, 15): [2, 0,  2,  0]
    }
