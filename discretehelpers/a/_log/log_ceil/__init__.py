from math import log2, ceil
from discretehelpers.a import true_except, is_natural
from discretehelpers.ex import ArgValueError


def log_ceil(x):

    true_except(is_natural(x - 1), ArgValueError)  # positive integers are allowed

    return ceil(log2(x))
