import numpy as np

from . import matrix_to_vector


def test():

    mat = np.array([
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ])
    assert matrix_to_vector(mat) == [2, 3, 9, 15]

    mat = np.array([
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ])
    assert matrix_to_vector(mat) == [1, 2, 3, 4]  # not invertible
