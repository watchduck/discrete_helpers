from discretehelpers.a import schoute_coset_gen


def test():
    sc_4_2 = schoute_coset_gen(4, 2, 4)
    sc_11_13 = schoute_coset_gen(11, 13, 4)
    assert sorted(sc_4_2) == sorted(sc_11_13) == [2, 3, 8, 9, 22, 23]

    sc_6_12 = schoute_coset_gen(6, 12, 4)
    sc_9_3 = schoute_coset_gen(9, 3, 4)
    assert sorted(sc_6_12) == sorted(sc_9_3) == [12, 14, 18, 20]
