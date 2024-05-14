from discretehelpers.binv import Binv

from discretehelpers.a import true_except
from discretehelpers.ex import ArgTooBigError, ArgValueError


def symmetric_to_index(symmetric_int, arity):

    if arity == 0:
        true_except(symmetric_int in [0, 1], ArgTooBigError)
        return symmetric_int

    length = 1 << arity  # 2 ** arity  (e.g. 8 for arity 3)
    too_big = 1 << length  # 2 ** length  (e.g. 256 for arity 3)
    half_length = length // 2

    true_except(symmetric_int < too_big, ArgTooBigError)

    symmetric_vector = Binv(intval=symmetric_int, length=length).vector
    left = symmetric_vector[0:half_length]
    right = symmetric_vector[half_length:]
    true_except(left == right[::-1], ArgValueError)  # not symmetric

    return Binv(right).intval
