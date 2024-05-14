from functools import cached_property

from discretehelpers.a import int_to_sierpinski_row
from discretehelpers.boolf.a import sierpinski_twin
from discretehelpers.sig_perm import SigPerm


@cached_property
def family_minrep(self):

    if self.is_constant:
        return self

    arity = self.adicity

    # top row in the blue and green matrix
    base_row = self.twin().tt(arity)

    length = 1 << arity  # 2 ** arity

    # This will be a set, that will initially contain the row indices, where the rightmost nontrivial column is false.
    # When a green row can not be the rep, its index gets removed from the candidates.
    # If the family has the maximal size, there will be a unique element.
    # But there may be multiple elements, all denoting duplicate green rows.
    all_candidates = None

    snooze = True  # nothing to do until rightmost true entry in base row

    # go through blue columns from right to left
    for right_index in range(length):
        left_index = length - right_index - 1

        if snooze:
            if base_row[left_index]:
                snooze = False
            else:
                continue

        places = int_to_sierpinski_row(right_index)  # relevant places of the current blue column
        small_tt = [base_row[left_index + place] for place in places]  # blue column without grayed out places

        if not sum(small_tt[1::]):
            continue  # blue columns without true entries after place 0 can be ignored

        green_column = sierpinski_twin(small_tt, left_index, arity)
        step_candidates = {k for k, v in enumerate(green_column) if not v}

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
                self.apply_sigperm(SigPerm(pair=(c, 0)))
            )
            if len(rep_candidates) > 1:
                finished = False
                break

        if finished:
            return rep_candidates.pop()
