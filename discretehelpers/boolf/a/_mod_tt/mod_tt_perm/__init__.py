from discretehelpers.walsh_perm import WalshPerm
from discretehelpers.binv import Binv


def mod_tt_perm(tt, perm):

    wp_vector = [2**i for i in perm]

    wp = WalshPerm(wp_vector).inverse

    mod_tt = wp.apply_on_vector(tt)

    return Binv(mod_tt)
