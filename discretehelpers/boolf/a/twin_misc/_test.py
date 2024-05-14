from discretehelpers.boolf.a import vector_to_twin_gen, \
    exposet_to_twin_gen, twin_int, \
    zhe_vector_to_prefect_gen, zhe_exposet_to_prefect_gen, \
    zhe_to_prefect


green_tt = [1, 1, 0, 1, 1, 1, 1, 0]  #
red_tt = [1, 0, 1, 1, 0, 0, 1, 0]

green_exposet = {0, 1, 3, 4, 5, 6}
red_exposet = {0, 2, 3, 6}

green_int = 123
red_int = 77


def test_tt_zhe():
    assert list(  vector_to_twin_gen(green_tt, 3)  ) \
           ==  list(  vector_to_twin_gen('1101 1110', 3)  )  ==  red_tt
    assert list(  vector_to_twin_gen('0000', 2)  )  ==  [0, 0, 0, 0]
    assert list(  vector_to_twin_gen('1000', 2)  )  ==  [1, 1, 1, 1]


def test_exposet_zhe():
    assert set(  exposet_to_twin_gen(green_exposet, 3)  )  ==  red_exposet
    assert set(  exposet_to_twin_gen(set(), 2)  )  ==  set()
    assert set(  exposet_to_twin_gen({0}, 2)  )  ==  {0, 1, 2, 3}


def test_int_zhe():
    assert twin_int(red_int, 3) == green_int
    assert twin_int(green_int, 3) == red_int

    assert [twin_int(_, 1) for _ in range(4)] == [0, 3, 2, 1]
    assert [twin_int(_, 2) for _ in range(16)] == [0, 15, 10, 5, 12, 3, 6, 9, 8, 7, 2, 13, 4, 11, 14, 1]


########################################################################################################################


def test_tt_prefect():
    assert list(  zhe_vector_to_prefect_gen(green_tt, 3)  )  ==  [0, 1, 0, 1, 1, 0, 1, 0]
    assert list(  zhe_vector_to_prefect_gen('0000', 2)  )  ==  [0, 0, 0, 0]
    assert list(  zhe_vector_to_prefect_gen('1000', 2)  )  ==  [1, 1, 1, 1]


def test_exposet_prefect():
    assert set(  zhe_exposet_to_prefect_gen(green_exposet, 3)  )  ==  {1, 3, 4, 6}
    assert set(  zhe_exposet_to_prefect_gen(set(), 2)  )  ==  set()
    assert set(  zhe_exposet_to_prefect_gen({0}, 2)  )  ==  {0, 1, 2, 3}


def test_int_prefect():
    assert zhe_to_prefect(green_int, 3) == (5, False)

    assert [zhe_to_prefect(_, 1) for _ in range(4)] == [
        (0, False),
        (0, True),
        (1, False),
        (1, True)
    ]
    assert [zhe_to_prefect(_, 2) for _ in range(16)] == [
        (0, False),
        (0, True),
        (1, False),
        (1, True),
        (2, False),
        (2, True),
        (3, False),
        (3, True),
        (3, True),
        (3, False),
        (2, True),
        (2, False),
        (1, True),
        (1, False),
        (0, True),
        (0, False)
    ]
