import numpy as np

from discretehelpers.a import true_except, sort_together
from discretehelpers.ex import ArgMismatchError


def sort_rows_together(*args):

    """
    Takes an arbitrary number of numpy arrays. Returns them sorted by rows.
    """

    height = args[0].shape[0]
    lists_of_rows = []
    for arg in args:
        true_except(arg.shape[0] == height, ArgMismatchError)
        lists_of_rows.append(arg.tolist())

    sorted_lists_of_rows = sort_together(*lists_of_rows)

    result_matrices = []
    for list_of_rows in sorted_lists_of_rows:
        result_matrices.append(np.array(list_of_rows))

    return tuple(result_matrices)
