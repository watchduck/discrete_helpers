from discretehelpers.boolf.examples import dagoro, darimi


def test_():
    # dagoro to darimi
    assert dagoro.apply(~3, 2, 1, 4) == darimi.apply(1, 2, 3, 4) == darimi
    assert dagoro.apply(~2, 1, 0, 3) == darimi.apply(0, 1, 2, 3)
    assert dagoro.vals(~2, 1, 0, 3) == darimi.root

    # darimi to dagoro
    assert darimi.apply(2, 1, ~0, 3) == dagoro
    assert darimi.vals(2, 1, ~0, 3) == dagoro.root
