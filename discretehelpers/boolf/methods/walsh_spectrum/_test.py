from discretehelpers.a import abbrev_testing as abbr

from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import gilipi, dukeli

from discretehelpers.ex import ArgTooSmallError


def test_gilipi():

    assert gilipi.walsh_spectrum() == (4, 2, 0, -2, 0, 2, 0, 2)
    assert gilipi.walsh_spectrum_abs() == (4, 2, 0, 2, 0, 2, 0, 2)
    assert gilipi.walsh_spectrum_layered() == ((4,), (2, 0, 0), (-2, 2, 0), (2,))
    assert gilipi.walsh_spectrum_abs_layered() == ((4,), (2, 0, 0), (2, 2, 0), (2,))

    assert gilipi.walsh_spectrum(4) == (8, 4, 0, -4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0)
    assert gilipi.walsh_spectrum_layered(4) == ((8,), (4, 0, 0, 0), (-4, 4, 0, 0, 0, 0), (4, 0, 0, 0), (0,))

    abbr(ArgTooSmallError, [
        lambda: gilipi.walsh_spectrum(2),
        lambda: gilipi.walsh_spectrum_layered(2),
    ])


def test_dukeli():

    assert dukeli.walsh_spectrum() == (8, 4, 2, 2, 2, -2, 0, 0, 4, 0, -2, -2, 2, -2, 0, 0)
    assert dukeli.walsh_spectrum_layered() == ((8,), (4, 2, 2, 4), (2, -2, 0, 0, -2, 2), (0, -2, -2, 0), (0,))
    assert dukeli.walsh_spectrum_abs() == (8, 4, 2, 2, 2, 2, 0, 0, 4, 0, 2, 2, 2, 2, 0, 0)
    assert dukeli.walsh_spectrum_abs_layered() == ((8,), (4, 2, 2, 4), (2, 2, 0, 0, 2, 2), (0, 2, 2, 0), (0,))


def test_misc():
    assert Boolf(False).walsh_spectrum() == (0,)
    assert Boolf(True).walsh_spectrum() == (1,)

    assert Boolf(atom=1).walsh_spectrum() == (2, 0, -2, 0)
    assert Boolf(atom=2).walsh_spectrum() == (4, 0, 0, 0, -4, 0, 0, 0)
    assert Boolf(atom=3).walsh_spectrum() == (8, 0, 0, 0, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0)
