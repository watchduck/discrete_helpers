from discretehelpers.a import true_except
from discretehelpers.ex import ArgMismatchError


def swap_matrix_rows(matrix, a, b):

    """
    Swap rows `a` and `b` of NumPy array `matrix`.
    """

    height = matrix.shape[0]
    true_except(a < height and b < height, ArgMismatchError)

    result_matrix = matrix.copy()

    result_matrix[a, :] = matrix[b, :]
    result_matrix[b, :] = matrix[a, :]

    return result_matrix
