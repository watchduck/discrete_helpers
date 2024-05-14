from discretehelpers.a import true_except, have, is_natural

from .ex import *
from discretehelpers.ex import ArgComboError


def int_to_sierpinski_row(intval=None, exposet=None):
    from discretehelpers.binv import Binv

    case_intval = have(intval) and not have(exposet)
    case_exposet = not have(intval) and have(exposet)
    true_except(case_intval or case_exposet, ArgComboError)

    if case_intval:
        true_except(is_natural(intval), NotNaturalError)
        if not intval:  # zero
            return [0]
        exposet = Binv(intval=intval).exposet

    if case_exposet:
        if not exposet:  # empty list
            return [0]

    addends = [1 << i for i in exposet]
    short = len(addends)
    long = 2**short
    result = [0] * long
    for i in range(long):
        i_bin = Binv(intval=i, length=short).vector
        for j in range(short):
            if i_bin[j]:
                result[i] += addends[j]
    return result


