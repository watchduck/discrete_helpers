from discretehelpers.a import true_except

from discretehelpers.binv import Binv

from .ex import *


def int_to_rcv(n, length=None):
    # integer to ring count vector (without the leading 1)
    old = [n]
    rcv = []
    while True:
        new = []
        for e in old:
            new += Binv(intval=e).exposet
        rcv.append(len(old))
        old = new
        if rcv[-1] == 0:
            break

    result = rcv[1:-1]  # remove leading 1 and trailing 0

    if length is None:
        return result
    else:
        nonzero_length = len(result)
        true_except(nonzero_length <= length, SpecifiedLengthTooShortError)
        result = result + [0] * (length - nonzero_length)
        return result
