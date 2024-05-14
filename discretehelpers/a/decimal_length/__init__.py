from math import floor, log

from discretehelpers.a import true_except, is_natural


def decimal_length(n):

    true_except(is_natural(n), NotNaturalError)

    if n == 0:
        return 0

    return floor(log(n, 10)) + 1


class NotNaturalError(ValueError):
    """The argument must be a positive integer."""
