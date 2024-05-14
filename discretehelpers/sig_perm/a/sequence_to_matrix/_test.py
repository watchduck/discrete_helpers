import numpy as np
from . import sequence_to_matrix


matrix = np.array([[ 0,  0,  1],
                   [-1,  0,  0],
                   [ 0,  1,  0]])

sequence = [~1, 2, 0]
inverse_sequence = [2, ~0, 1]


def test():
    assert np.array_equal(
        sequence_to_matrix(sequence),
        matrix
    )

    assert np.array_equal(
        sequence_to_matrix(sequence, inverse=False),
        matrix
    )

    assert np.array_equal(
        sequence_to_matrix(inverse_sequence, inverse=True),
        matrix
    )
