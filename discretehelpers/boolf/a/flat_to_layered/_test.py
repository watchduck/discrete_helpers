from discretehelpers.boolf.a import flat_to_layered
from discretehelpers.boolf.examples import kagusi, subaru


def test_usual():
    # The optional argument `false_and_true_places` is false by default.
    # This allows general entries, which is used to create layered Walsh spectra.
    assert flat_to_layered([0, 1, 1, 1]) == ((0,), (1, 1), (1,))
    assert flat_to_layered(range(16)) == ((0,), (1, 2, 4, 8), (3, 5, 6, 9, 10, 12), (7, 11, 13, 14), (15,))


def test_sides():
    # The optional argument `false_and_true_places` is set to true.

    assert flat_to_layered([0, 1, 1, 1], True) == {
        0: ([0], []),
        1: ([], [1, 2]),
        2: ([], [3])
    }

    assert flat_to_layered(kagusi.tt(), True) == {
        0: ([0], []),
        1: ([4], [1, 2, 8]),
        2: ([5, 6, 9, 10], [3, 12]),
        3: ([7, 11, 14], [13]),
        4: ([15], [])
    }

    assert flat_to_layered(subaru.tt(), True) == {
        0: ([], [0]),
        1: ([1], [2, 4, 8]),
        2: ([9], [3, 5, 6, 10, 12]),
        3: ([14], [7, 11, 13]),
        4: ([15], [])
    }
