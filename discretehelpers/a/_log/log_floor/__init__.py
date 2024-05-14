from math import log2, floor
from discretehelpers.a import true_except, is_natural
from discretehelpers.ex import ArgValueError


def log_floor(x):

    true_except(is_natural(x - 1), ArgValueError)  # positive integers are allowed

    return floor(log2(x))
