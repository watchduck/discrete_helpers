import pytest

from discretehelpers.walsh_perm import WalshPerm


vectors_to_results = {
    (3, 1): 2,

    (7, 11, 13, 14): 0,

    # upper triangular matrices
    (1,): 0,
    (1, 3): 1,
    (1, 3, 7): 3,
    (1, 3, 7, 15): 7,
    (1, 3, 7, 15, 31): 15,
    (1, 3, 7, 15, 31, 63): 31,

    # inverses of upper triangular matrices
    (1,): 0,
    (1, 3): 1,
    (1, 3, 6): 2,
    (1, 3, 6, 12): 5,
    (1, 3, 6, 12, 24): 10,
    (1, 3, 6, 12, 24, 48): 21
}


@pytest.mark.parametrize('vector', vectors_to_results.keys())
def test(vector):
    assert WalshPerm(vector=vector).complement_distance == vectors_to_results[vector]
