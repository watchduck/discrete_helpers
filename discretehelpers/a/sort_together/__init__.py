from discretehelpers.a import true_except

from .ex import *


def sort_together(*args):

    length = len(args[0])
    for arg in args:
        true_except(len(arg) == length, LengthMismatchError)

    zipped = zip(*args)
    sorted_zipped = sorted(zipped)
    unzipped = zip(*sorted_zipped)
    return tuple([list(_) for _ in unzipped])
