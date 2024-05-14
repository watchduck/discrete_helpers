import numpy as np
from discretehelpers.a import abbrev_testing as abbrev
from discretehelpers.walsh_perm import WalshPerm
from discretehelpers.walsh_perm.ex import NotEvenPermutationError, InvalidPermError, InvalidMatrixError


invalid_matrix_6_5_3 = np.array([[0, 1, 1],
                                 [1, 0, 1],
                                 [1, 1, 0]])  # det 2

invalid_matrix_1_2_3_4 = np.array([[1, 0, 1, 0],
                                   [0, 1, 1, 0],
                                   [0, 0, 0, 1],
                                   [0, 0, 0, 0]])  # det 0

invalid_matrix_9_2_5_12 = np.array([[1, 0, 1, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 1],
                                    [1, 0, 0, 1]])  # det 2

invalid_matrix_13_12_7_10 = np.array([[1, 0, 1, 0],
                                      [0, 0, 1, 1],
                                      [1, 1, 1, 0],
                                      [1, 1, 0, 1]])  # det -2


def test_matrix():
    abbrev(InvalidMatrixError, [
        lambda: WalshPerm(matrix=invalid_matrix_6_5_3),
        lambda: WalshPerm(vector=(6, 5, 3)),

        lambda: WalshPerm(matrix=invalid_matrix_1_2_3_4),
        lambda: WalshPerm(vector=(1, 2, 3, 4)),

        lambda: WalshPerm(matrix=invalid_matrix_9_2_5_12),
        lambda: WalshPerm(vector=(9, 2, 5, 12)),

        lambda: WalshPerm(matrix=invalid_matrix_13_12_7_10),
        lambda: WalshPerm(vector=(13, 12, 7, 10)),
    ])


def test_perm():

    # These are not even valid permutations, let alone Walsh permutations.
    abbrev(NotEvenPermutationError, [
        lambda: WalshPerm(perm=[0, 1, 3, 5]),
        lambda: WalshPerm(perm=[0, 5, 6, 3, 8, 13, 14, 11, 0, 5, 6, 3, 8, 13, 14, 11])
    ])

    # These are permutations, but they are not Walsh.
    abbrev(InvalidPermError, [
        lambda: WalshPerm(perm=[3, 2, 1, 0]),  # If the first position is not fixed, it can not be a Walsh permutation.
        lambda: WalshPerm(perm=[0, 7, 6, 5, 4, 3, 2, 1])
    ])


def test_trust():

    # Invalid permutations are accepted, when `trust` is true.

    wp = WalshPerm(perm=[3, 2, 1, 0], trust=True)
    assert wp.sequence() == [0, 2, 1, 3]

    wp = WalshPerm(perm=[0, 7, 6, 5, 4, 3, 2, 1], trust=True)
    assert wp.sequence() == [0, 7, 6, 1, 4, 3, 2, 5]

    wp = WalshPerm(matrix=invalid_matrix_13_12_7_10, trust=True)
    assert wp.vector() == (13, 12, 7, 10)
    assert wp.determinant == -2

    abbrev(InvalidMatrixError, [
        lambda: wp.sequence(),
        lambda: wp.cycles()
    ])
