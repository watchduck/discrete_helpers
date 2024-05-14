from discretehelpers.ex import ArgValueError, ArgComboError, ArgTooBigError


# The first three arguments can be used without keywords. `arity` is required, `parity` defaults to 0.

def make_linear_binv(walsh=None, arity=None, parity=None, leader=None, quadrant=None, prefab_atom_patterns=None):

    from discretehelpers.a import true_except, have, is_natural, make_atompatterns, index_to_evil, index_to_odious

    from discretehelpers.binv import Binv

    true_except(have(arity), ArgComboError)
    true_except(is_natural(arity) and arity > 0, ArgValueError)

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

    length = 2 ** arity

    true_except(walsh_index < length, ArgTooBigError)

    if have(prefab_atom_patterns):
        true_except(len(prefab_atom_patterns[0]) == length, ArgValueError)
        atom_patterns = prefab_atom_patterns
    else:
        atom_patterns = make_atompatterns(arity)

    binv = Binv([0] * length)
    for n in range(arity):
        if (2 ** n) & walsh_index:  # if the n-th digit of `walsh_index` in binary is 1
            binv = binv ^ atom_patterns[n]

    if not is_odd:
        return binv
    else:
        return ~binv
