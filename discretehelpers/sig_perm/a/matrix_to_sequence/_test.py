from . import matrix_to_sequence


matrix = [[ 0,  0,  1],
          [-1,  0,  0],
          [ 0,  1,  0]]

sequence = [~1, 2, 0]
inverse_sequence = [2, ~0, 1]


def test():
    assert matrix_to_sequence(matrix) == matrix_to_sequence(matrix, inverse=False) == sequence
    assert matrix_to_sequence(matrix, inverse=True) == inverse_sequence
