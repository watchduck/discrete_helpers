from discretehelpers.boolf.examples import medusa, logota


def test_medusa():

    assert medusa.fullspots_by_weight == {
        0: {0: []},
        1: {1: [0], 2: [1], 4: [2], 8: [3]},
        2: {3: [0, 1], 5: [0, 2], 6: [1, 2], 9: [0, 3], 10: [1, 3], 12: [2, 3]},
        3: {7: [0, 1, 2], 14: [1, 2, 3]}
    }

    assert medusa.layered_fullspots == [[0], [1, 2, 4, 8], [3, 5, 6, 9, 10, 12], [7, 14], []]

    assert medusa.fullspot_weights == [0, 1, 2, 3]


def test_logota():

    assert logota.fullspots_by_weight == {
        1: {1: [0], 4: [2]},
        2: {3: [0, 1], 5: [0, 2], 10: [1, 3], 12: [2, 3]},
        3: {11: [0, 1, 3], 14: [1, 2, 3]}
    }

    assert logota.layered_fullspots == [[], [1, 4], [3, 5, 10, 12], [11, 14], []]

    assert logota.fullspot_weights == [1, 2, 3]
