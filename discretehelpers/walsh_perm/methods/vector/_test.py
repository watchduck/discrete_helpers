from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.walsh_perm import WalshPerm

from discretehelpers.walsh_perm.ex import RequestedDegreeSmallerActualDegreeError

wp_neut = WalshPerm(vector=())
wp_137 = WalshPerm(vector=(1, 3, 7))
wp_764 = WalshPerm(vector=(7, 6, 4))


def test_results():

    assert wp_neut.vector()  == ()
    assert wp_neut.vector(0) == ()
    assert wp_neut.vector(1) == (1,)
    assert wp_neut.vector(2) == (1, 2)
    assert wp_neut.vector(3) == (1, 2, 4)
    assert wp_neut.vector(4) == (1, 2, 4, 8)

    assert wp_137.vector()  == (1, 3, 7)
    assert wp_137.vector(3) == (1, 3, 7)
    assert wp_137.vector(4) == (1, 3, 7, 8)


def test_exception():

    abbrev(RequestedDegreeSmallerActualDegreeError, [
        lambda: wp_137.vector(2),
        lambda: wp_137.vector(1),
        lambda: wp_137.vector(0),

        lambda: wp_764.matrix(2),
        lambda: wp_764.matrix(1),
        lambda: wp_764.matrix(0)
    ])
