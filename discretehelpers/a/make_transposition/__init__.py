from discretehelpers.a import true_except
from discretehelpers.ex import ArgValueError


def make_transposition(a, b, length):

    true_except(a != b, ArgValueError)
    true_except(a < length and b < length, ArgValueError)

    sequence = list(range(length))

    sequence[a] = b
    sequence[b] = a

    return sequence
