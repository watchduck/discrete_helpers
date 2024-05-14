from math import log2
from discretehelpers.a import is_natural, true_except
from discretehelpers.ex import ArgValueError


def log_int(x):

    true_except(
        is_natural(x - 1),
        ArgValueError('not a natural number')
    )

    result = log2(x)
    if is_natural(result):
        return int(result)
    else:
        raise ArgValueError('not a power of two')
