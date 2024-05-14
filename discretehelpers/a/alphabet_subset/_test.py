from . import alphabet_subset


def test():
    assert alphabet_subset([0, 1, 2]) == ['A', 'B', 'C']
    assert alphabet_subset([1, 3, 5, 7]) == ['B', 'D', 'F', 'H']
    assert alphabet_subset([0, 26]) == [0, 26]
