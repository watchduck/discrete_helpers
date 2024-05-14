import numpy as np
from discretehelpers.a import make_linear_binv, make_atompatterns, is_natural


def arity_to_walsh_matrix(arity, negate=False):
    assert is_natural(arity)

    if arity == 0:
        if negate:
            return np.ones([1, 1], dtype=int)
        else:
            return np.zeros([1, 1], dtype=int)

    size = 1 << arity  # 2 ** arity

    prefab_atom_patterns = make_atompatterns(arity)

    result = np.zeros([size, size], dtype=int)
    for i in range(size):
        result[i, :] = make_linear_binv(i, arity, negate, prefab_atom_patterns=prefab_atom_patterns)
    return result
