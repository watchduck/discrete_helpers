from discretehelpers.boolf.examples import miniri, sediri


def test_samples():
    assert miniri.apply(0, 4, 5, 3, 2) == miniri.apply(3, 4, 5, 0, 2) == sediri
    assert sediri.apply(0, 4, 3, 1, 2) == sediri.apply(3, 4, 0, 2, 1) == miniri
