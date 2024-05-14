import numpy as np

from discretehelpers.a import have, true_except, int_to_exposet, log_int

from discretehelpers.ex import ArgValueError, ArgComboError, ArgTooSmallError


def sierpinski(orientation, degree=None, size=None):

    from discretehelpers.boolf.a import atoms_to_and_gen  # would lead to ImportError

    true_except(orientation in ['tl', 'tr', 'bl', 'br'], ArgValueError)

    true_except(
        (have(degree) and not have(size)) or (not have(degree) and have(size)),
        ArgComboError
    )

    if have(degree):
        true_except(degree > 0, ArgValueError)
        size = 1 << degree  # 2 ** degree
    else:
        true_except(size >= 2, ArgTooSmallError)
        degree = log_int(size)

    max_index = size - 1

    result = np.zeros([size, size], dtype=int)

    for i in range(size):

        row_exposet = int_to_exposet(i)

        row_gen = atoms_to_and_gen(row_exposet, degree)

        if orientation == 'tr':
            result[i, :] = list(row_gen)
        elif orientation == 'tl':
            result[i, :] = list(row_gen)[::-1]
        elif orientation == 'br':
            result[max_index - i, :] = list(row_gen)
        elif orientation == 'bl':
            result[max_index - i, :] = list(row_gen)[::-1]

    return result
