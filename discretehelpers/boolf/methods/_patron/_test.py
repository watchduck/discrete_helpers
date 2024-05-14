from discretehelpers.boolf import Boolf


def test_168():
    # These are the positions of 168 in row 3 of triangle Xi.
    zhes = [2, 28, 42, 52, 74, 84, 98, 124, 130, 156, 170, 180, 202, 212, 226, 252]
    for zhe in zhes:
        boolf = Boolf(zhe=zhe)
        assert boolf.patron_int(3) == 168

    boolf = Boolf(zhe=168)

    # The patron of a noble function is the contradiction.
    assert boolf.patron_int(3) == boolf.patron_index(3) == 0
    assert boolf.patron_boolf(3) == Boolf('0')
    assert boolf.patron_boolf(3).prefect_walsh_and_oddness == (0, 0)


def test():
    f, t = Boolf('0'), Boolf('1')
    for arity in range(5):
        assert f.patron_int(arity) == 0
        assert f.patron_boolf(arity) == f
        intval = 2 ** 2 ** arity - 2
        assert t.patron_int(arity) == intval
        assert t.patron_boolf(arity) == Boolf(intval, arity=arity)

    boolf = Boolf('0100 1100')
    assert boolf.patron_int(3) == 200
    assert boolf.patron_index(3) == 12
    assert boolf.patron_boolf(3) == Boolf('0001 0011')
    assert boolf.patron_royal(3) == 72
    assert boolf.patron_quadrant(3) == 2
    assert boolf.patron_boolf(3).prefect_walsh_and_oddness == (2, 0)

    assert boolf.patron_king_index_and_quadrant(3) == (2, 2)  # king index 2, quadrant 2

    assert boolf.patron_int(4) == 13000
    assert boolf.patron_index(4) == 50
    assert boolf.patron_boolf(4) == Boolf('0001 0011 0100 1100')
    assert boolf.patron_royal(4) == 13000
    assert boolf.patron_quadrant(4) == 0
    assert boolf.patron_boolf(4).prefect_walsh_and_oddness == (10, 0)
    assert boolf.patron_king_index_and_quadrant(4) == (14, 0)


def test_patron_prefect():

    perm = [0, 4, 6, 2, 5, 1, 3, 7]  # WP (4, 6, 5)
    for key, zhe in enumerate([0, 15, 10, 5, 12, 3, 6, 9, 8, 7, 2, 13, 4, 11, 14, 1]):  # WP (15, 10, 12, 8)

        key_boolf = Boolf(key, arity=2)
        is_odd, is_odious = key_boolf.is_odd, key_boolf.is_odious
        quadrant = key_boolf.quadrant

        boolf = Boolf(zhe=zhe)

        assert boolf.quadrant == quadrant
        assert boolf.patron_index(3) == key

        expected_walsh_index = perm[key] if not is_odious else 7 - perm[key - 8]
        assert boolf.patron_boolf(3).prefect_walsh_and_oddness == (expected_walsh_index, is_odd)

        expected_leader = expected_walsh_index >> 1
        assert boolf.patron_boolf(3).prefect_leader_and_quadrant == (expected_leader, quadrant)
