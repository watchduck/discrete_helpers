from discretehelpers.ex import ArgValueError, ArgComboError


def make_linear_boolf(walsh=None, parity=None, leader=None, quadrant=None):

    from discretehelpers.binv import Binv
    from discretehelpers.boolf import Boolf
    from discretehelpers.a import true_except, have, index_to_evil, index_to_odious

    if have(walsh):
        is_odd = parity if have(parity) else 0
        true_except(not have(leader) and not have(quadrant), ArgComboError)
        true_except(is_odd in [0, 1, False, True], ArgValueError)
        walsh_index = walsh
    elif have(leader) and have(quadrant):
        true_except(quadrant in range(4), ArgValueError)
        true_except(not have(walsh) and not have(parity), ArgComboError)
        walsh_index = index_to_evil(leader) if quadrant in [0, 3] else index_to_odious(leader)
        is_odd = quadrant in [1, 3]
    else:
        raise ArgComboError

    exposet = Binv(intval=walsh_index).exposet

    boolf = Boolf(multi_xor=exposet)

    if not is_odd:
        return boolf
    else:
        return ~boolf
