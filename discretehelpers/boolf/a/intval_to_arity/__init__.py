from discretehelpers.a import log_floor
from discretehelpers.a import true_except, is_natural
from discretehelpers.ex import ArgValueError


def intval_to_arity(x):

    true_except(is_natural(x), ArgValueError)

    if x in [0, 1]:
        return 0

    return log_floor(log_floor(x)) + 1


def intval_to_tt_length(x):

    exponent = intval_to_arity(x)

    return 1 << exponent  # 2 ** exponent
