import pytest

from discretehelpers.walsh_perm import WalshPerm


vectors_to_results = {
    (3, 1): 1,
    (3, 1, 4): 5,
    (3, 1, 4, 8): 13,

    (7, 11, 13, 14): 15,
    (7, 11, 13, 14, 16): 31,

    # upper triangular matrices
    (1,): 1,
    (1, 3): 2,
    (1, 3, 7): 4,
    (1, 3, 7, 15): 8,
    (1, 3, 7, 15, 31): 16,
    (1, 3, 7, 15, 31, 63): 32,
    (1, 3, 7, 15, 31, 63, 127): 64,
    (1, 3, 7, 15, 31, 63, 127, 255): 128,

    # inverses of upper triangular matrices
    (1,): 1,
    (1, 3): 2,
    (1, 3, 6): 5,
    (1, 3, 6, 12): 10,
    (1, 3, 6, 12, 24): 21,
    (1, 3, 6, 12, 24, 48): 42,
    (1, 3, 6, 12, 24, 48, 96): 85,
    (1, 3, 6, 12, 24, 48, 96, 192): 170
    # 1, 5, 21, 85... is 1, 101, 10101, 1010101... in binary format (OEIS A002450)

}


@pytest.mark.parametrize('vector', vectors_to_results.keys())
def test(vector):
    degree = len(vector)
    wp = WalshPerm(vector)
    assert wp.complement_pattern(degree) == vectors_to_results[vector]


inverse_vectors_to_results = {
    (2, 4, 7): 1,
    (1, 4, 7): 2,
    (1, 4, 6): 3,
    (1, 2, 7): 4,
    (1, 2, 6): 5,
    (1, 2, 5): 6,
    (1, 2, 4): 7
}


@pytest.mark.parametrize('vector', inverse_vectors_to_results.keys())
def test_inverse(vector):
    wp = WalshPerm(vector)
    assert wp.inverse.complement_pattern(3) == inverse_vectors_to_results[vector]
