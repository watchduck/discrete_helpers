import numpy as np
from . import arity_to_walsh_matrix


def test():
    assert np.array_equal(arity_to_walsh_matrix(1), np.array([
        [0, 0],
        [0, 1]
    ]))

    assert np.array_equal(arity_to_walsh_matrix(2), np.array([
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 0]
    ]))

    assert np.array_equal(arity_to_walsh_matrix(3), np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 1]
    ]))
