from functools import cached_property
from discretehelpers.boolf.metributes._ec_reps.minimal.clan_minrep.prototype import clan_minrep_prototype

from math import factorial
from collections import defaultdict

from discretehelpers.sig_perm import SigPerm
from discretehelpers.boolf.a import sierpinski_twin, flat_to_layered
from discretehelpers.a import int_to_sierpinski_row
from .schoute_wrapper import schoute_wrapper


@cached_property
def clan_minrep(self):

    debug = True

    if self.is_constant:
        return self

    arity = self.adicity

    twin_boolf = self.twin()
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
    all_candidates = None

    # The relevant rows of every blue matrix are a subset of those of the first blue matrix (with left index 0).
    # Each needs to be calculated only once (and some may not be needed).
    # Each row is saved as the set of true places.
    dict_of_blue_rows = dict()

    # go through green matrices from right to left
    for right_index in range(1, height):
        left_index = height - right_index - 1

        if debug:
            print('###', left_index)

        # The indices denote the relevant rows of this particular blue matrix (which are not grayed out).
        # The keys refer to `dict_of_blue_rows`. The values are the rows, which appear in all blue matrices.
        blue_indices = int_to_sierpinski_row(right_index)
        blue_keys = [_ ^ left_index for _ in blue_indices]
        assert blue_keys == sorted(blue_keys)
        blue_keys_set = set(blue_keys)

        for new_blue_key in blue_keys_set.difference(set(dict_of_blue_rows.keys())):
            dict_of_blue_rows[new_blue_key] = schoute_wrapper(
                new_blue_key, arity, layer_to_false_and_true_places, layer_to_ratio
            )

        # "small" refers to the relevant part of the blue columns, "big" to the corresponding green columns.
        # Potential candidates are the complements of the green matrix.
        # To complement all digits of big green, the first digit of blue small is complemented. (Zhegalkin twins)
        small_to_col_indices = defaultdict(set)
        small_to_big = dict()
        for col_index in range(width):
            small = tuple([int(col_index in dict_of_blue_rows[_]) for _ in blue_keys])
            small_to_col_indices[small].add(col_index)
            if small not in small_to_big:
                comp_small = list(small)
                comp_small[0] = not small[0]
                small_to_big[small] = sierpinski_twin(comp_small, left_index, arity)

        step_candidates = set()
        for small, col_indices in small_to_col_indices.items():
            big = small_to_big[small]
            for row_index, val in enumerate(big):
                if val:
                    step_candidates |= {(row_index, col_index) for col_index in col_indices}

        if all_candidates is not None:
            candidate_intersection = all_candidates.intersection(step_candidates)
            if candidate_intersection:  # not empty
                all_candidates = candidate_intersection
            else:
                continue  # Ignore the column, if it would leave no candidates.
        else:
            all_candidates = step_candidates

        finished = True
        rep_candidates = set()  # This will be a set of Boolfs. One of them is the representative.
        for pair in all_candidates:
            rep_candidates.add(
                self.apply_sigperm(SigPerm(pair=pair))
            )
            if len(rep_candidates) > 1:
                finished = False
                break

        if finished:
            return rep_candidates.pop()
