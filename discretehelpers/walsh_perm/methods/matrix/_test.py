import numpy as np

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.walsh_perm import WalshPerm

from discretehelpers.walsh_perm.ex import RequestedDegreeSmallerActualDegreeError


wp_neut = WalshPerm(vector=())
wp_137 = WalshPerm(vector=(1, 3, 7))
wp_764 = WalshPerm(vector=(7, 6, 4))

wp_137_matrix_3 = np.array([[1, 1, 1],
                            [0, 1, 1],
                            [0, 0, 1]])

wp_137_matrix_4 = np.array([[1, 1, 1, 0],
                            [0, 1, 1, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])


def test_results():

    for i in range(5):
        assert np.array_equal(wp_neut.matrix(i), np.eye(i, dtype=int))

    assert np.array_equal(wp_137.matrix(),  wp_137_matrix_3)
    assert np.array_equal(wp_137.matrix(3), wp_137_matrix_3)
    assert np.array_equal(wp_137.matrix(4), wp_137_matrix_4)


def test_exception():

    abbrev(RequestedDegreeSmallerActualDegreeError, [
        lambda: wp_137.matrix(2),
        lambda: wp_137.matrix(1),
        lambda: wp_137.matrix(0),

        lambda: wp_764.matrix(2),
        lambda: wp_764.matrix(1),
        lambda: wp_764.matrix(0)
    ])
