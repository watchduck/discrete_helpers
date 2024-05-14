from discretehelpers.a import true_except, is_natural

from .ex import *


def vector_zip_apart(vector, pattern):
    from discretehelpers.binv import Binv

    if type(vector) not in [list, tuple, Binv] or type(pattern) not in [list, tuple, Binv]:
        raise NotListLikeError

    length = len(vector)
    true_except(length == len(pattern), LengthError)

    for i in range(length):
        true_except(is_natural(pattern[i]), NotNaturalError)

    result_length = max(pattern) + 1
    result = [list() for _ in range(result_length)]  # list of empty lists

    for i in range(length):
        result[pattern[i]].append(vector[i])

    if type(vector) == Binv:
        return [Binv(_) for _ in result]
    else:
        return result
