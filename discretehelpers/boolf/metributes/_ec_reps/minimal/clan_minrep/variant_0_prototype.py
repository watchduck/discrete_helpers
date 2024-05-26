import numpy as np
from math import factorial
from collections import defaultdict

from discretehelpers.sig_perm import SigPerm
from discretehelpers.boolf.a import sierpinski_twin, flat_to_layered
from discretehelpers.a import int_to_sierpinski_row, int_to_weight
from .schoute_wrapper import schoute_wrapper


@property
def _clan_minrep_prototype(self):

    if self.is_constant:
        return self

    arity = self.adicity
    plenty = 1 << arity  # 2 ** arity
    galore = factorial(arity)
    
    twin_boolf = self.twin()
    layer_to_false_and_true_places = flat_to_layered(twin_boolf.tt(arity), True)
    layer_to_ratio = dict()
    for layer_index, (false_places, true_places) in layer_to_false_and_true_places.items():
        false_length, true_length = len(false_places), len(true_places)
        layer_to_ratio[layer_index] = true_length / (false_length + true_length)
        
    # The true entries in this matrix denote the candidates. Initially all pairs are candidates.
    # When a pair can not be the rep, the respective entry becomes false.
    # Iff the clan has the maximal size, only one true entry will be left.
    matrix_of_candidates = np.ones([plenty, galore], dtype=bool)

    # The relevant (not grayed out) rows of every blue matrix are a subset of those of the first one (from left).
    # Each needs to be calculated only once. (And only if it is needed.)
    dict_of_blue_rows = dict()

    # go through green matrices from right to left
    for right_index in range(1, plenty):
        left_index = plenty - right_index - 1

        blue_row_indices = int_to_sierpinski_row(right_index)  # relevant (not grayed out) row indices of blue matrix
        blue_keys = [_ ^ left_index for _ in blue_row_indices]

        for blue_key in blue_keys:
            if blue_key not in dict_of_blue_rows:  # create if needed
                blue_row = np.zeros([galore], dtype=bool)
                for place in schoute_wrapper(blue_key, arity, layer_to_false_and_true_places, layer_to_ratio):
                    blue_row[place] = True
                dict_of_blue_rows[blue_key] = blue_row

        # "small" refers to the relevant part of the blue columns, "big" to the corresponding green columns.
        # Applicants (potential candidates) are the false entries of the green matrix.
        # To negate all digits of the green column, the first digit of blue is negated. (Zhegalkin twins)
        small_to_col_indices = defaultdict(set)
        small_to_big = dict()

        for col_index in range(galore):
            raw_small = [dict_of_blue_rows[_][col_index] for _ in blue_keys]
            small = raw_small.copy()
            small[0] = not small[0]  # negate first digit
            small = tuple(small)
            small_to_col_indices[small].add(col_index)
            if small not in small_to_big:
                small_to_big[small] = sierpinski_twin(small, left_index, arity)

        matrix_of_applicants = np.zeros([plenty, galore], dtype=bool)
        for small, col_indices in small_to_col_indices.items():
            big = small_to_big[small]
            for col_index in col_indices:
                matrix_of_applicants[:, col_index] = big

        candidate_intersection = matrix_of_candidates & matrix_of_applicants

        if sum(sum(candidate_intersection)):  # not empty
            matrix_of_candidates = candidate_intersection
        else:
            continue  # Ignore the column, if it would leave no candidates.

        finished = True
        rep_candidates = set()  # This will be a set of Boolfs. One of them is the representative.
        for m, n in zip(*np.nonzero(matrix_of_candidates)):
            rep_candidates.add(
                self.apply_sigperm(SigPerm(pair=(int(m), int(n))))  # `m` and `n` are initially `numpy.int64`.
            )
            if len(rep_candidates) > 1:
                finished = False
                break

        if finished:
            return rep_candidates.pop()
