from discretehelpers.boolf.examples import barita, putuki, gepofu, miniri, \
    seduki as filtrate_seduki, sedofu as filtrate_sedofu, sediri as filtrate_sediri


def test_filtrates():
    assert filtrate_seduki == barita.filtrated_boolf([0, 2, 3, 5])  # A, C, D, F  (B and E removed)
    assert filtrate_sedofu == barita.filtrated_boolf([1, 2, 3, 4, 5])  # B, C, D, E, F  (A removed)
    assert filtrate_sediri == barita.filtrated_boolf([0, 2, 3, 4, 5])  # A, C, D, E, F  (B removed)

    assert filtrate_seduki.atomvals == [0, 2, 3, 5]
    assert filtrate_seduki.fullspots == {0, 1, 2, 3, 4, 6, 8, 9, 12}

    assert filtrate_sedofu.atomvals == [1, 2, 4, 5]
    assert filtrate_sedofu.fullspots == {0, 1, 2, 3, 4, 8, 12}

    assert filtrate_sediri.atomvals == [0, 2, 3, 4, 5]
    assert filtrate_sediri.fullspots == {0, 1, 2, 3, 4, 6, 8, 9, 12, 16, 17, 20, 24, 25, 28}


def test_conversion():
    assert putuki.apply(3, 0, 1, 2) == filtrate_seduki.apply(0, 1, 2, 3)
    assert putuki.apply(0, 1, 2, 3) == filtrate_seduki.apply(1, 2, 3, 0)

    assert gepofu.apply(0, 2, 3, 1) == filtrate_sedofu.apply(0, 1, 2, 3)
    assert gepofu.apply(0, 1, 2, 3) == filtrate_sedofu.apply(0, 3, 1, 2)

    assert miniri.apply(2, 3, 4, 0, 1) == filtrate_sediri.apply(0, 1, 2, 3, 4)
    assert miniri.apply(0, 1, 2, 3, 4) == filtrate_sediri.apply(3, 4, 0, 1, 2)
