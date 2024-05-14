from math import log

from discretehelpers.a import is_natural


def is_power_of_two(n):
    if n == 0:
        return False
    if not is_natural(n):
        return False
    log_n = log(n, 2)
    if not is_natural(log_n):
        return False
    return True
