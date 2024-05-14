import numpy as np
from math import factorial
from collections import defaultdict

from discretehelpers.sig_perm import SigPerm
from discretehelpers.boolf.a import sierpinski_twin, flat_to_layered
from discretehelpers.a import int_to_sierpinski_row, int_to_weight
from ..schoute_wrapper import schoute_wrapper


def clan_minrep_prototype(boolf):

    debug = True

    if boolf.is_constant:
        return boolf

    arity = boolf.adicity

    twin_boolf = boolf.twin()
    layer_to_false_and_true_places = flat_to_layered(twin_boolf.tt(arity), True)
    layer_to_ratio = dict()
    for layer_index, (false_places, true_places) in layer_to_false_and_true_places.items():
        false_length, true_length = len(false_places), len(true_places)
        layer_to_ratio[layer_index] = true_length / (false_length + true_length)

    height = 1 << arity  # 2 ** arity
    width = factorial(arity)

    # This will be a set, that will initially contain the row indices, where the rightmost nontrivial column is false.
    # When a row can not be the rep, its index gets removed from the candidates.
    # If the faction has the maximal size, there will be a unique element.
    # But there may be multiple elements, all denoting duplicate rows.
    matrix_of_candidates = np.ones([height, width], dtype=bool)

    # The relevant rows of every blue matrix are a subset of those of the first blue matrix (with left index 0).
    # Each needs to be calculated only once (and not all will necessarily be needed).
    dict_of_schoute_rows = dict()

    # go through green matrices from right to left
    for right_index in range(1, height):
        left_index = height - right_index - 1

        if debug:
            print('###', left_index)

        blue_row_indices = int_to_sierpinski_row(right_index)  # relevant row indices of the blue matrix (not grayed out)
        schoute_keys = [_ ^ left_index for _ in blue_row_indices]

        for schoute_key in schoute_keys:
            if schoute_key not in dict_of_schoute_rows:
                schoute_row = np.zeros([width], dtype=bool)
                for place in schoute_wrapper(schoute_key, arity, layer_to_false_and_true_places, layer_to_ratio):
                    schoute_row[place] = True
                dict_of_schoute_rows[schoute_key] = schoute_row

        # "small" refers to the relevant part of the blue columns, "big" to the corresponding green columns.
        # Potential candidates are the complements of the green matrix.
        # To complement all digits of the green column, the first digit of blue is complemented. (Zhegalkin twins)
        small_to_col_indices = defaultdict(set)
        small_to_big = dict()

        for col_index in range(width):
            raw_small = [dict_of_schoute_rows[_][col_index] for _ in schoute_keys]
            small = raw_small.copy()
            small[0] = not small[0]
            small = tuple(small)
            small_to_col_indices[small].add(col_index)
            if small not in small_to_big:
                small_to_big[small] = sierpinski_twin(small, left_index, arity)

        matrix_of_step_candidates = np.zeros([height, width], dtype=bool)
        for small, col_indices in small_to_col_indices.items():
            big = small_to_big[small]
            for col_index in col_indices:
                matrix_of_step_candidates[:, col_index] = big

        candidate_intersection = matrix_of_candidates & matrix_of_step_candidates
        if sum(sum(candidate_intersection)):  # not empty
            matrix_of_candidates = candidate_intersection

        else:
            continue  # Ignore the column, if it would leave no candidates.

        finished = True
        rep_candidates = set()  # This will be a set of Boolfs. One of them is the representative.
        for m, n in zip(*np.nonzero(matrix_of_candidates)):
            rep_candidates.add(
                boolf.apply_sigperm(SigPerm(pair=(int(m), int(n))))  # `m` and `n` are initially `numpy.int64`.
            )
            if len(rep_candidates) > 1:
                finished = False
                break

        if finished:
            return rep_candidates.pop()
