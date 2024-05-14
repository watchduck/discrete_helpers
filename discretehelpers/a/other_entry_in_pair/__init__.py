from discretehelpers.a import true_except

from .ex import *


def other_entry_in_pair(pair, entry):

    true_except(type(pair) in [list, tuple, set], WrongTypeError)
    true_except(len(pair) == 2, WrongLengthError)

    return list(
        set(pair).difference({entry})
    )[0]
