import numpy as np

from . import sort_rows_together


def test():
    a = np.array([
        [5, 1, 2],
        [3, 1, 5],
        [2, 2, 1]
    ])
    b = np.array([
        [1, 2],
        [1, 5],
        [2, 1]
    ])

    a, b = sort_rows_together(a, b)

    assumed_a = np.array([
        [2, 2, 1],
        [3, 1, 5],
        [5, 1, 2]
    ])
    assumed_b = np.array([
        [2, 1],
        [1, 5],
        [1, 2]
    ])

    assert np.array_equal(a, assumed_a)
    assert np.array_equal(b, assumed_b)
