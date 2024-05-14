from discretehelpers.sig_perm import SigPerm
from discretehelpers.perm import Perm


def test_unsigned():
    p = Perm([3, 0, 1, 2])
    sp = SigPerm(pair=(0, 9))
    schoute_p = p.schoute_perm
    schoute_sp = sp.schoute_perm
    assert schoute_p == schoute_sp == Perm([[1, 8, 4, 2], [3, 9, 12, 6], [5, 10], [7, 11, 13, 14]], perilen=16)
    assert schoute_sp.sequence() == schoute_p.sequence() == [0, 8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]


def test_signed():
    sigperm = SigPerm(pair=(0, 9))
    schoute = sigperm.schoute_perm
    assert schoute == Perm([[1, 8, 4, 2], [3, 9, 12, 6], [5, 10], [7, 11, 13, 14]], perilen=16)
    assert schoute.sequence() == [0, 8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]

    sigperm = SigPerm(pair=(1, 3))
    schoute = sigperm.schoute_perm
    assert schoute == Perm([[0, 1, 5, 7, 6, 2], [3, 4]], perilen=8)
    assert schoute.sequence()   == [1, 5, 0, 4, 3, 7, 2, 6]
    assert schoute.sequence(16) == [1, 5, 0, 4, 3, 7, 2, 6, 9, 13, 8, 12, 11, 15, 10, 14]

    sigperm = SigPerm(pair=(3, 18))
    assert sigperm == SigPerm(sequence=[~1, 2, 3, ~0])
    schoute = sigperm.schoute_perm
    assert schoute.inverse.sequence() == [9, 1, 8, 0, 11, 3, 10, 2, 13, 5, 12, 4, 15, 7, 14, 6]
