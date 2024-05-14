from itertools import product
import numpy as np


def balanced_ternary_walsh_matrix(n, with_vectors_matrix=False):

    vectors_list = product([-1, 0, 1], repeat=n)
    vectors_list = [_[::-1] for _ in vectors_list]
    vectors_matrix = np.zeros([3 ** n, n], dtype=int)
    for i, v in enumerate(vectors_list):
        vectors_matrix[i, :] = v

    result_matrix_natural = np.dot(vectors_matrix, vectors_matrix.T)

    result_matrix = result_matrix_natural % 3
    result_matrix[result_matrix == 2] = -1

    if with_vectors_matrix:
        return result_matrix, vectors_matrix
    else:
        return result_matrix
