from discretehelpers.boolf.a import hasse_matrix_coordinates_to_tt
from discretehelpers.binv import Binv


def test():
    assert hasse_matrix_coordinates_to_tt(1, 1, 3) == Binv('1000 0001')
    assert hasse_matrix_coordinates_to_tt(3, 3, 3) == Binv('1100 0011')
    assert hasse_matrix_coordinates_to_tt(3, 5, 3) == Binv('1100 0101')
