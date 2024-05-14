from math import log

from discretehelpers.a import true_except, is_power_of_two

from .ex import NotWalshRowError


def walsh_function_to_index(vector, trust=False):

    from discretehelpers.binv import Binv

    binv = Binv(vector)

    ####################################################################################################################

    if binv == Binv('0'):
        return 0  # undefined would be correct, but 0 is more useful

    ####################################################################################################################

    length = binv.length
    true_except(is_power_of_two(length), ValueError)
    degree = int(log(length, 2))

    if trust:
        powers_of_two = [2 ** _ for _ in range(degree)]
        short_vector = [binv[_] for _ in powers_of_two]
        return Binv(short_vector).intval

    ####################################################################################################################

    from discretehelpers.walsh_perm import WalshPerm
    from .. import make_linear_binv

    wp_vector = [2 ** (degree - 1)] + [2**(degree-i-1) * 3 for i in range(1, degree)]  # e.g. [8, 12, 6, 3] for degree 4
    wp = WalshPerm(wp_vector)

    row_index = wp[binv.changes]

    true_except(
        binv == make_linear_binv(row_index, degree),
        NotWalshRowError
    )

    return row_index
