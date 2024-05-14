from discretehelpers.binv import Binv
from discretehelpers.a import int_to_weight, log_int


def flat_to_layered(vector, false_and_true_places=False):

    if type(vector) == Binv:
        vector = [int(_) for _ in vector]

    arity = log_int(len(vector))

    if not false_and_true_places:

        # Each entry is a list of truth values. Becomes tuple of tuples.
        result = [list() for _ in range(arity + 1)]

        for key, val in enumerate(vector):
            weight = int_to_weight(key)
            result[weight].append(val)

        return tuple(tuple(_) for _ in result)

    else:

        # Each entry is a pair of lists. The first contains the false, and the second the true keys.
        result = {_: ([], []) for _ in range(arity + 1)}

        for key, val in enumerate(vector):
            weight = int_to_weight(key)
            result[weight][int(val)].append(key)

        return result
