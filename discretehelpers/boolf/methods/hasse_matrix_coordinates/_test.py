from discretehelpers.boolf import Boolf


def test():
    assert Boolf('1010 0110').hasse_matrix_coordinates() == (5, 6)
    assert Boolf('1110 1101').hasse_matrix_coordinates() == (7, 13)

    assert Boolf('1').hasse_matrix_coordinates(3) == (15, 15)
    assert Boolf('1').hasse_matrix_coordinates(4) == (255, 255)
