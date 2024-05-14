from discretehelpers.binv import Binv
from discretehelpers.boolf.a import mod_tt_perm


def test():

    binv = Binv('1111 1010 1000 1000')  # zhe 11809 (dukeli)

    assert mod_tt_perm(binv, [3, 1, 0, 2]) == Binv('1110 1010 1110 0000')  # perm 11 (inverse of 19) --> zhe 12457

    assert mod_tt_perm(binv, [3, 2, 0, 1]) == Binv('1111 1000 1010 1000')  # perm 17 (inverse of 22) --> zhe 8929
