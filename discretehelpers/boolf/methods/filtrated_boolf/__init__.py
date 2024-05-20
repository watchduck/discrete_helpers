import numpy as np
from discretehelpers.a import make_atompattern, true_except

from discretehelpers.binv import Binv

from .ex import AtomvalsMismatchError


def filtrated_boolf(self, small_atomvals):
    from discretehelpers.boolf import Boolf

    big_atomvals = self.atomvals
    true_except(set(small_atomvals).issubset(big_atomvals), AtomvalsMismatchError)
    
    big_valency = self.valency
    big_length = 2 ** big_valency
    big_truthtable = self.root

    small_atomkeys = [big_atomvals.index(_) for _ in small_atomvals]
    small_valency = len(small_atomvals)
    small_length = 2 ** small_valency
    small_truthtable = [False] * small_length  # to be the main ingredient of the result

    patterns = []
    for small_atomkey in small_atomkeys:
        patterns.append(
            make_atompattern(small_atomkey, big_valency)
        )

    long_matrix = np.zeros([small_valency, big_length], dtype=bool)
    for m in range(small_valency):
        long_matrix[m, :] = patterns[m]
    long_sequence = [Binv(long_matrix[:, n]).intval for n in range(big_length)]  # sequence of length `big_length` with (repeating) values in `range(small_length)`

    for big_spotkey, small_spotkey in enumerate(long_sequence):
        small_truthtable[small_spotkey] |= big_truthtable[big_spotkey]

    return Boolf(small_truthtable, small_atomvals)
