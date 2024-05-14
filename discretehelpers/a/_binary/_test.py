from discretehelpers.a import int_to_exposet, exposet_to_int, vector_to_int, int_to_weight


example_int = 123456789
example_exposet = [0, 2, 4, 8, 10, 11, 14, 15, 16, 17, 19, 20, 22, 24, 25, 26]


def test():
    assert int_to_exposet(example_int) == example_exposet

    assert exposet_to_int(example_exposet) == example_int

    assert vector_to_int([1, 1, 0, 0, 0, 0, 0, 1]) == 131  # 1 + 2 + 128

    assert int_to_weight(example_int) == len(example_exposet)
    assert [int_to_weight(_) for _ in range(16)] == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

