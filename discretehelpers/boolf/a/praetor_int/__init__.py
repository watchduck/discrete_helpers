from discretehelpers.binv import Binv

from discretehelpers.a import true_except

from discretehelpers.ex import ArgTooSmallError, ArgTooBigError


def praetor_int(intval, arity):

    true_except(arity > 0, ArgTooSmallError)

    length = 1 << arity  # 2 ** arity

    too_big = 1 << length  # 2 ** length
    true_except(intval < too_big, ArgTooBigError)


    half_length = length // 2

    tt = Binv(intval=intval, length=length)

    left = Binv(tt[0:half_length]).intval
    right = Binv(tt[half_length:length]).intval

    return left ^ right
