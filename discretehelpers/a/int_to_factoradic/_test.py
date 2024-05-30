from discretehelpers.a import int_to_factoradic


def test():

    assert int_to_factoradic(0)  == ()
    assert int_to_factoradic(1)  == (0, 1)
    assert int_to_factoradic(2)  == (0, 0, 1)
    assert int_to_factoradic(3)  == (0, 1, 1)
    assert int_to_factoradic(4)  == (0, 0, 2)
    assert int_to_factoradic(5)  == (0, 1, 2)
    assert int_to_factoradic(6)  == (0, 0, 0, 1)
    assert int_to_factoradic(7)  == (0, 1, 0, 1)
    assert int_to_factoradic(8)  == (0, 0, 1, 1)
    assert int_to_factoradic(9)  == (0, 1, 1, 1)
    assert int_to_factoradic(10) == (0, 0, 2, 1)
    assert int_to_factoradic(11) == (0, 1, 2, 1)
    assert int_to_factoradic(12) == (0, 0, 0, 2)
    assert int_to_factoradic(13) == (0, 1, 0, 2)
    assert int_to_factoradic(14) == (0, 0, 1, 2)
    assert int_to_factoradic(15) == (0, 1, 1, 2)
    assert int_to_factoradic(16) == (0, 0, 2, 2)
    assert int_to_factoradic(17) == (0, 1, 2, 2)
    assert int_to_factoradic(18) == (0, 0, 0, 3)
    assert int_to_factoradic(19) == (0, 1, 0, 3)
    assert int_to_factoradic(20) == (0, 0, 1, 3)
    assert int_to_factoradic(21) == (0, 1, 1, 3)
    assert int_to_factoradic(22) == (0, 0, 2, 3)
    assert int_to_factoradic(23) == (0, 1, 2, 3)

    assert int_to_factoradic(21686) == (0, 0, 1, 2, 3, 0, 2, 4)  # left
    assert int_to_factoradic(3989)  == (0, 1, 2, 0, 1, 3, 5)  # right
