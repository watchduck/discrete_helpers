from discretehelpers.a import have, int_to_weight
from discretehelpers.binv import Binv


def consul_weight(self, arity):

    return int_to_weight(self.consul(arity))


def consul(self, arity=None):

    # bitwise XOR of the true places in the truth table, returns entries of A253315

    result = 0
    for key, val in enumerate(self.tt(arity)):
        if val:
            result ^= key
    return result


def consul_slow(self, arity, prefab_matrix=None):

    # inefficient, only used for testing

    import numpy as np
    from discretehelpers.a import arity_to_walsh_matrix, walsh_function_to_index
    from discretehelpers.a import log_int

    tt = [int(_) for _ in self.tt(arity)]
    assert log_int(len(tt)) == arity

    if have(prefab_matrix):
        matrix = prefab_matrix
        high, wide = matrix.shape
        assert high == wide == 2 ** arity
    else:
        matrix = arity_to_walsh_matrix(arity)

    walsh_tt = tuple([_ % 2 for _ in np.dot(tt, matrix)])

    return walsh_function_to_index(walsh_tt)
