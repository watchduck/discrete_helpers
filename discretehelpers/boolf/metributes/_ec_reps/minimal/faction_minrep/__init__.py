from functools import cached_property

from discretehelpers.sig_perm import SigPerm
from discretehelpers.a import int_to_weight
from discretehelpers.boolf.a import flat_to_layered
from .schoute_wrapper import schoute_wrapper


@cached_property
def faction_minrep(self):

    if self.is_constant:
        return self

    arity = self.adicity

    is_symmetric = True
    twin_boolf = self.twin()
    layer_to_false_and_true_places = flat_to_layered(twin_boolf.tt(arity), True)
    layer_to_ratio = dict()
    for layer_index, (false_places, true_places) in layer_to_false_and_true_places.items():
        false_length, true_length = len(false_places), len(true_places)
        ratio = true_length / (false_length + true_length)
        layer_to_ratio[layer_index] = ratio
        if ratio not in [0, 1]:
            is_symmetric = False

    if is_symmetric:
        return self

    length = 1 << arity  # 2 ** arity

    # This will be a set, that will initially contain the row indices, where the rightmost nontrivial column is false.
    # When a row can not be the rep, its index gets removed from the candidates.
    # If the faction has the maximal size, there will be a unique element.
    # But there may be multiple elements, all denoting duplicate rows.
    all_candidates = None

    # go through green columns from right to left
    for right_index in range(1, length):
        left_index = length - right_index - 1
        layer_index = int_to_weight(left_index)
        layer_ratio = layer_to_ratio[layer_index]
        if layer_ratio in [0, 1]:
            continue

        step_candidates = schoute_wrapper(left_index, arity, layer_to_false_and_true_places, layer_index, layer_ratio)

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
        for c in all_candidates:
            rep_candidates.add(
                self.apply_sigperm(SigPerm(pair=(0, c)))
            )
            if len(rep_candidates) > 1:
                finished = False
                break

        if finished:
            return rep_candidates.pop()
