import numpy as np

from discretehelpers.walsh_perm import WalshPerm


def test_cyclic_group_15():

    # Was meant to be (15, 5, 11, 13), but this also gives a 15-cycle.

    wp = WalshPerm(vector=(15, 5, 11, 3))

    matrix = np.array([[1, 1, 1, 1],
                       [1, 0, 1, 1],
                       [1, 1, 0, 0],
                       [1, 0, 1, 0]])

    assert np.array_equal(
        np.array(wp.matrix(), dtype=int),
        matrix
    )

    cycle = dict()
    for i in range(16):
        power = wp ** i
        cycle[i] = {
            'vector': power.vector(4),
            'order': power.order,
            'cycles': power.cycles,
            'det': power.determinant
        }

    assert cycle == {
         0: {'vector': ( 1,  2,  4,  8), 'det':  1, 'order':  1, 'cycles': []},
         1: {'vector': (15,  5, 11,  3), 'det': -1, 'order': 15, 'cycles': [[1, 15, 2, 5, 4, 11, 9, 12, 8, 3, 10, 6, 14, 13, 7]]},
         2: {'vector': ( 2,  4,  9, 10), 'det':  1, 'order': 15, 'cycles': [[1, 2, 4, 9, 8, 10, 14, 7, 15, 5, 11, 12, 3, 6, 13]]},
         3: {'vector': ( 5, 11, 12,  6), 'det': -3, 'order':  5, 'cycles': [[1, 5, 9, 3, 14], [2, 11, 8, 6, 7], [4, 12, 10, 13, 15]]},
         4: {'vector': ( 4,  9,  8, 14), 'det': -1, 'order': 15, 'cycles': [[1, 4, 8, 14, 15, 11, 3, 13, 2, 9, 10, 7, 5, 12, 6]]},
         5: {'vector': (11, 12,  3, 13), 'det':  1, 'order':  3, 'cycles': [[1, 11, 10], [2, 12, 14], [3, 7, 4], [5, 8, 13], [6, 15, 9]]},
         6: {'vector': ( 9,  8, 10,  7), 'det':  1, 'order':  5, 'cycles': [[1, 9, 14, 5, 3], [2, 8, 7, 11, 6], [4, 10, 15, 12, 13]]},
         7: {'vector': (12,  3,  6,  1), 'det': -1, 'order': 15, 'cycles': [[1, 12, 7, 9, 13, 11, 14, 4, 6, 5, 10, 2, 3, 15, 8]]},
         8: {'vector': ( 8, 10, 14, 15), 'det': -1, 'order': 15, 'cycles': [[1, 8, 15, 3, 2, 10, 5, 6, 4, 14, 11, 13, 9, 7, 12]]},
         9: {'vector': ( 3,  6, 13,  2), 'det':  1, 'order':  5, 'cycles': [[1, 3, 5, 14, 9], [2, 6, 11, 7, 8], [4, 13, 12, 15, 10]]},
        10: {'vector': (10, 14,  7,  5), 'det':  1, 'order':  3, 'cycles': [[1, 10, 11], [2, 14, 12], [3, 4, 7], [5, 13, 8], [6, 9, 15]]},
        11: {'vector': ( 6, 13,  1,  4), 'det': -1, 'order': 15, 'cycles': [[1, 6, 12, 5, 7, 10, 9, 2, 13, 3, 11, 15, 14, 8, 4]]},
        12: {'vector': (14,  7, 15, 11), 'det': -1, 'order':  5, 'cycles': [[1, 14, 3, 9, 5], [2, 7, 6, 8, 11], [4, 15, 13, 10, 12]]},
        13: {'vector': (13,  1,  2,  9), 'det':  1, 'order': 15, 'cycles': [[1, 13, 6, 3, 12, 11, 5, 15, 7, 14, 10, 8, 9, 4, 2]]},
        14: {'vector': ( 7, 15,  5, 12), 'det': -1, 'order': 15, 'cycles': [[1, 7, 13, 14, 6, 10, 3, 8, 12, 9, 11, 4, 5, 2, 15]]},
        15: {'vector': ( 1,  2,  4,  8), 'det':  1, 'order':  1, 'cycles': []}
    }

    assert wp**-1 == wp.inverse == wp**14
