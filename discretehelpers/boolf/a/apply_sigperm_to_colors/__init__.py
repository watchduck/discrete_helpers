from discretehelpers.a import have
from collections import defaultdict


def apply_sigperm_to_colors(color_to_fullspots, arity, sigperm):

    if type(sigperm) in [list, tuple]:
        from discretehelpers.sig_perm import SigPerm
        sigperm = SigPerm(sequence=sigperm)

    vector = [None for _ in range(2**arity)]

    for color, fullspots in color_to_fullspots.items():
        for fullspot in fullspots:
            vector[fullspot] = color

    result_vector = sigperm.schoute_perm.apply_on_vector(vector)

    result_dict = defaultdict(list)
    for key, val in enumerate(result_vector):
        if have(val):
            result_dict[val].append(key)

    return dict(result_dict)
