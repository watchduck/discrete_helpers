import pytest

from discretehelpers.sig_perm import SigPerm

from discretehelpers.sig_perm.a import schoute_to_finite_inverse as f


def test():
    row_3_short = [0, 2, 4, 6,  1, 3, 5, 7]
    row_3_long = row_3_short + [_ + 8 for _ in row_3_short]
    assert f(row_3_short) == f(row_3_long) == [2, 0, 1]

    assert f([0, 2, 4, 6,  8, 10, 12, 14,  1, 3, 5, 7,  9, 11, 13, 15]) == [3, 0, 1, 2]  # row 9


@pytest.mark.parametrize('pair', [(0, 0), (0, 3), (5, 0), (6, 13)])
def test_pair(pair):
    sig_perm = SigPerm(pair=pair)
    inverse_sequence = sig_perm.inverse.sequence()
    schoute = sig_perm.schoute_perm
    schoute_sequence = schoute.sequence()
    assert f(schoute) == f(schoute_sequence) == inverse_sequence
    assert SigPerm(schoute_perm=schoute) == SigPerm(schoute_perm=schoute_sequence) == sig_perm
