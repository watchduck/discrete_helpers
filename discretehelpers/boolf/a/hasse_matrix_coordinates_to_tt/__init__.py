from discretehelpers.binv import Binv


def hasse_matrix_coordinates_to_tt(i, j, arity=None):

    length = 1 << arity  # 2 ** arity
    half_length = length // 2

    left = Binv(intval=i, length=half_length).vector
    right = Binv(intval=j, length=half_length).vector[::-1]

    return Binv(left + right)
