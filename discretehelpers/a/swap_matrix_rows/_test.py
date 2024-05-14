import numpy as np

from . import swap_matrix_rows


def test():

    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    mod_matrix = swap_matrix_rows(matrix, 1, 2)

    assumed_mod_matrix = np.array([
        [1, 2, 3],
        [7, 8, 9],
        [4, 5, 6]
    ])

    assert np.array_equal(mod_matrix, assumed_mod_matrix)
