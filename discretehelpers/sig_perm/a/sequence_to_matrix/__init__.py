import numpy as np

from discretehelpers.a import true_except, have, logic_abs, logic_negate_vector


def sequence_to_matrix(sequence, inverse=False):

    size = len(sequence)

    mat = np.zeros([size, size], dtype=int)

    for colnum, signed_entry in enumerate(sequence):
        natural_entry = logic_abs(signed_entry)
        mat[natural_entry, colnum] = -1 if signed_entry < 0 else 1

    if inverse:
        mat = mat.transpose()

    return mat
