from discretehelpers.a import have, true_except

from .ex import *


def slice_to_range(s, stop=None):

    start = s.start if have(s.start) else 0
    stop = s.stop if have(s.stop) else stop
    step = s.step if have(s.step) else 1

    true_except(have(stop), StopMissingError)

    return range(start, stop, step)