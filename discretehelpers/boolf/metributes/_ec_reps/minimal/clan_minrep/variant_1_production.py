from functools import cached_property

from math import factorial
from collections import defaultdict

from discretehelpers.sig_perm import SigPerm
from discretehelpers.boolf.a import sierpinski_twin, flat_to_layered
from discretehelpers.a import int_to_sierpinski_row
from .schoute_wrapper import schoute_wrapper


@cached_property
def clan_minrep(self):

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

    # This will be a set of pairs representing the candidates. Initially that would be all, but None is used instead.
    # When a pair can not be the rep, it is removed from the set.
    # Iff the clan has the maximal size, only one pair will be left.
    set_of_candidates = None

    # The relevant rows of every blue matrix are a subset of those of the first blue matrix (with left index 0).
    # Each needs to be calculated only once (and some may not be needed).
    # Each row is saved as the set of true places.
    dict_of_blue_rows = dict()

    # go through green matrices from right to left
    for right_index in range(1, plenty):
        left_index = plenty - right_index - 1

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
        # Applicants (potential candidates) are the false entries of the green matrix.
        # To negate all digits of the green column, the first digit of blue is negated. (Zhegalkin twins)
        small_to_col_indices = defaultdict(set)
        small_to_big = dict()

        for col_index in range(galore):
            small = tuple([int(col_index in dict_of_blue_rows[_]) for _ in blue_keys])
            small_to_col_indices[small].add(col_index)
            if small not in small_to_big:
                comp_small = list(small)
                comp_small[0] = not small[0]  # negate first digit
                small_to_big[small] = sierpinski_twin(comp_small, left_index, arity)

        set_of_applicants = set()
        for small, col_indices in small_to_col_indices.items():
            big = small_to_big[small]
            for row_index, val in enumerate(big):
                if val:
                    set_of_applicants |= {(row_index, col_index) for col_index in col_indices}

        have_candidates = set_of_candidates is not None
        have_applicants = set_of_applicants != set()

        if not have_applicants:
            continue
        else:
            if not have_candidates:
                set_of_candidates = set_of_applicants
            else:
                candidate_intersection = set_of_candidates.intersection(set_of_applicants)
                if candidate_intersection:  # not empty
                    set_of_candidates = candidate_intersection
                else:
                    continue  # Ignore the column, if it would leave no candidates.

        finished = True
        rep_candidates = set()  # This will be a set of Boolfs. One of them is the representative.
        for pair in set_of_candidates:
            rep_candidates.add(
                self.apply_sigperm(SigPerm(pair=pair))
            )
            if len(rep_candidates) > 1:
                finished = False
                break

        if finished:
            return rep_candidates.pop()
