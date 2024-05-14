import numpy as np
from discretehelpers.a import balanced_ternary_walsh_matrix


def test():

    assert np.array_equal(
        balanced_ternary_walsh_matrix(2),
        np.array([
            [-1,  1,  0,  1,  0, -1,  0, -1,  1],
            [ 1,  1,  1,  0,  0,  0, -1, -1, -1],
            [ 0,  1, -1, -1,  0,  1,  1, -1,  0],
            [ 1,  0, -1,  1,  0, -1,  1,  0, -1],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
            [-1,  0,  1, -1,  0,  1, -1,  0,  1],
            [ 0, -1,  1,  1,  0, -1, -1,  1,  0],
            [-1, -1, -1,  0,  0,  0,  1,  1,  1],
            [ 1, -1,  0, -1,  0,  1,  0,  1, -1]
        ])
    )

    expected_result_matrix = np.array([
       [ 0, -1,  1, -1,  1,  0,  1,  0, -1, -1,  1,  0,  1,  0, -1,  0, -1,  1,  1,  0, -1,  0, -1,  1, -1,  1,  0],
       [-1, -1, -1,  1,  1,  1,  0,  0,  0,  1,  1,  1,  0,  0,  0, -1, -1, -1,  0,  0,  0, -1, -1, -1,  1,  1,  1],
       [ 1, -1,  0,  0,  1, -1, -1,  0,  1,  0,  1, -1, -1,  0,  1,  1, -1,  0, -1,  0,  1,  1, -1,  0,  0,  1, -1],
       [-1,  1,  0, -1,  1,  0, -1,  1,  0,  1,  0, -1,  1,  0, -1,  1,  0, -1,  0, -1,  1,  0, -1,  1,  0, -1,  1],
       [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [ 0,  1, -1,  0,  1, -1,  0,  1, -1, -1,  0,  1, -1,  0,  1, -1,  0,  1,  1, -1,  0,  1, -1,  0,  1, -1,  0],
       [ 1,  0, -1, -1,  1,  0,  0, -1,  1,  0, -1,  1,  1,  0, -1, -1,  1,  0, -1,  1,  0,  0, -1,  1,  1,  0, -1],
       [ 0,  0,  0,  1,  1,  1, -1, -1, -1, -1, -1, -1,  0,  0,  0,  1,  1,  1,  1,  1,  1, -1, -1, -1,  0,  0,  0],
       [-1,  0,  1,  0,  1, -1,  1, -1,  0,  1, -1,  0, -1,  0,  1,  0,  1, -1,  0,  1, -1,  1, -1,  0, -1,  0,  1],
       [-1,  1,  0,  1,  0, -1,  0, -1,  1, -1,  1,  0,  1,  0, -1,  0, -1,  1, -1,  1,  0,  1,  0, -1,  0, -1,  1],
       [ 1,  1,  1,  0,  0,  0, -1, -1, -1,  1,  1,  1,  0,  0,  0, -1, -1, -1,  1,  1,  1,  0,  0,  0, -1, -1, -1],
       [ 0,  1, -1, -1,  0,  1,  1, -1,  0,  0,  1, -1, -1,  0,  1,  1, -1,  0,  0,  1, -1, -1,  0,  1,  1, -1,  0],
       [ 1,  0, -1,  1,  0, -1,  1,  0, -1,  1,  0, -1,  1,  0, -1,  1,  0, -1,  1,  0, -1,  1,  0, -1,  1,  0, -1],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
       [-1,  0,  1, -1,  0,  1, -1,  0,  1, -1,  0,  1, -1,  0,  1, -1,  0,  1, -1,  0,  1, -1,  0,  1, -1,  0,  1],
       [ 0, -1,  1,  1,  0, -1, -1,  1,  0,  0, -1,  1,  1,  0, -1, -1,  1,  0,  0, -1,  1,  1,  0, -1, -1,  1,  0],
       [-1, -1, -1,  0,  0,  0,  1,  1,  1, -1, -1, -1,  0,  0,  0,  1,  1,  1, -1, -1, -1,  0,  0,  0,  1,  1,  1],
       [ 1, -1,  0, -1,  0,  1,  0,  1, -1,  1, -1,  0, -1,  0,  1,  0,  1, -1,  1, -1,  0, -1,  0,  1,  0,  1, -1],
       [ 1,  0, -1,  0, -1,  1, -1,  1,  0, -1,  1,  0,  1,  0, -1,  0, -1,  1,  0, -1,  1, -1,  1,  0,  1,  0, -1],
       [ 0,  0,  0, -1, -1, -1,  1,  1,  1,  1,  1,  1,  0,  0,  0, -1, -1, -1, -1, -1, -1,  1,  1,  1,  0,  0,  0],
       [-1,  0,  1,  1, -1,  0,  0,  1, -1,  0,  1, -1, -1,  0,  1,  1, -1,  0,  1, -1,  0,  0,  1, -1, -1,  0,  1],
       [ 0, -1,  1,  0, -1,  1,  0, -1,  1,  1,  0, -1,  1,  0, -1,  1,  0, -1, -1,  1,  0, -1,  1,  0, -1,  1,  0],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1],
       [ 1, -1,  0,  1, -1,  0,  1, -1,  0, -1,  0,  1, -1,  0,  1, -1,  0,  1,  0,  1, -1,  0,  1, -1,  0,  1, -1],
       [-1,  1,  0,  0, -1,  1,  1,  0, -1,  0, -1,  1,  1,  0, -1, -1,  1,  0,  1,  0, -1, -1,  1,  0,  0, -1,  1],
       [ 1,  1,  1, -1, -1, -1,  0,  0,  0, -1, -1, -1,  0,  0,  0,  1,  1,  1,  0,  0,  0,  1,  1,  1, -1, -1, -1],
       [ 0,  1, -1,  1, -1,  0, -1,  0,  1,  1, -1,  0, -1,  0,  1,  0,  1, -1, -1,  0,  1,  0,  1, -1,  1, -1,  0]
    ])

    expected_vectors_matrix = np.array([
        [-1, -1, -1],
        [ 0, -1, -1],
        [ 1, -1, -1],
        [-1,  0, -1],
        [ 0,  0, -1],
        [ 1,  0, -1],
        [-1,  1, -1],
        [ 0,  1, -1],
        [ 1,  1, -1],
        [-1, -1,  0],
        [ 0, -1,  0],
        [ 1, -1,  0],
        [-1,  0,  0],
        [ 0,  0,  0],
        [ 1,  0,  0],
        [-1,  1,  0],
        [ 0,  1,  0],
        [ 1,  1,  0],
        [-1, -1,  1],
        [ 0, -1,  1],
        [ 1, -1,  1],
        [-1,  0,  1],
        [ 0,  0,  1],
        [ 1,  0,  1],
        [-1,  1,  1],
        [ 0,  1,  1],
        [ 1,  1,  1]
    ])

    result_matrix, vectors_matrix = balanced_ternary_walsh_matrix(3, with_vectors_matrix=True)

    assert np.array_equal(result_matrix, expected_result_matrix)
    assert np.array_equal(vectors_matrix, expected_vectors_matrix)