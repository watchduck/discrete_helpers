from discretehelpers.boolf.examples import levana, seduki, sedofu, duvola, rudafi, megomi, todeda, damela, rotovo


def test_0():
    assert duvola.quadrant == 0
    assert rudafi.quadrant == 0
    assert megomi.quadrant == 0
    assert todeda.quadrant == 0

    assert levana.quadrant == 1
    assert seduki.quadrant == 1
    assert sedofu.quadrant == 1

    assert rotovo.quadrant == 2

    assert damela.quadrant == 3
