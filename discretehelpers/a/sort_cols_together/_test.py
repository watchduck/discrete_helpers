import numpy as np

from . import sort_cols_together


a = np.array([
    [5, 1, 2],
    [3, 1, 5],
    [2, 2, 1]
])
b = np.array([
    [22, 11, 33],
    [99, 77, 44]
])


def test_top():

    a_sorted, b_sorted = sort_cols_together(a, b, small_on_top=True)

    assumed_a_sorted = np.array([
        [2, 1, 5],
        [5, 1, 3],
        [1, 2, 2]
    ])
    assumed_b_sorted = np.array([
        [33, 11, 22],
        [44, 77, 99]
    ])

    assert np.array_equal(a_sorted, assumed_a_sorted)
    assert np.array_equal(b_sorted, assumed_b_sorted)


def test_bottom():

    a_sorted, b_sorted = sort_cols_together(a, b, small_on_top=False)

    also_a_sorted, also_b_sorted = sort_cols_together(a, b)
    assert np.array_equal(also_a_sorted, a_sorted)
    assert np.array_equal(also_b_sorted, b_sorted)

    assumed_a_sorted = np.array([
        [1, 2, 5],
        [1, 5, 3],
        [2, 1, 2]
    ])
    assumed_b_sorted = np.array([
        [11, 33, 22],
        [77, 44, 99]
    ])

    assert np.array_equal(a_sorted, assumed_a_sorted)
    assert np.array_equal(b_sorted, assumed_b_sorted)
