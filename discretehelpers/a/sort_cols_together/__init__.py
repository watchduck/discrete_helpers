import numpy as np

from discretehelpers.a import true_except, sort_rows_together
from discretehelpers.ex import ArgMismatchError


def sort_cols_together(*args, small_on_top=False):

    """
    Takes an arbitrary number of numpy arrays. Returns them sorted by columns.
    If `small_on_top` is true, the least significant position is on top, if false on the bottom.
    """

    width = args[0].shape[1]
    turned_matrices = []
    for arg in args:
        true_except(arg.shape[1] == width, ArgMismatchError)
        turned_matrix = np.fliplr(arg.T) if small_on_top else arg.T
        turned_matrices.append(turned_matrix)

    sorted_turned_matrices = sort_rows_together(*turned_matrices)

    result_matrices = []
    for matrix in sorted_turned_matrices:
        result_matrix = np.fliplr(matrix).T if small_on_top else matrix.T
        result_matrices.append(result_matrix)

    return tuple(result_matrices)
