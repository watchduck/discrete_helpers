from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.binv import Binv

from . import deflate


def test():
    assert deflate(Binv('1'), []) == (Binv('1'), [])
    assert deflate(Binv('1111'), [77, 99]) == (Binv('1'), [])
    assert deflate(Binv('0000 0000'), [1, 3, 5]) == (Binv('0'), [])

    assert deflate(Binv('1010'), [0, 1]) == (Binv('10'), [0])
    assert deflate(Binv('1100'), [0, 1]) == (Binv('10'), [1])

    assert deflate(Binv('0101 1010'), [0, 1, 2]) == (Binv('0110'), [0, 2])
    assert deflate(Binv('0011 0011'), [1000, 3000, 5000]) == (Binv('01'), [3000])

    assert deflate(Binv('0000 0000 0000 1111'), [0, 1, 2, 3]) == (Binv('0001'), [2, 3])
    assert deflate(Binv('0001 1000 0001 1000'), [2, 5, 8, 99]) == (Binv('0001 1000'), [2, 5, 8])


def test_raise():
    abbrev(ValueError, [
        lambda: deflate([0, 1, 0, 0], [0, 1])
    ])


def test_inflate_and_deflate():
    from discretehelpers.boolf import Boolf

    binv = Binv('0110 1101')
    atomvals = [3, 7, 9]
    boolf = Boolf(binv, atomvals)

    inflated_atomvals = [1, 3, 5, 7, 9]  # add atomvals 1 and 5
    inflated_exposet = boolf.inflated_fullspots(inflated_atomvals)
    assert inflated_exposet == {2, 3, 6, 7, 8, 9, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 26, 27, 30, 31}
    inflated_binv = Binv(exposet=inflated_exposet, length=32)  # double length for each new atomval
    assert inflated_binv == Binv('0011 0011 1100 1100  1111 1111 0011 0011')

    assert deflate(inflated_binv, inflated_atomvals) == (binv, atomvals)
