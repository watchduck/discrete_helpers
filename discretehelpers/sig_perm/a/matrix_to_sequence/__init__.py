import numpy as np

from discretehelpers.a import true_except


def matrix_to_sequence(matrix, inverse=False):

    mat = matrix if type(matrix) == np.ndarray else np.array(matrix)
    size, also_size = mat.shape
    true_except(size == also_size and type(size) == int, ValueError)

    if inverse:
        mat = mat.transpose()

    sequence = []
    for n in range(size):
        for m in range(size):
            if mat[m, n] == 1:
                sequence.append(m)
            elif mat[m, n] == -1:
                sequence.append(~m)

    return sequence
