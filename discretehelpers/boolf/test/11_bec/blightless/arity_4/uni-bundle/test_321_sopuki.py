from discretehelpers.boolf.examples import sopuki as boolf


def test_sopuki():

    assert boolf.fullspots == {0, 1, 2, 3, 4, 5, 6, 7, 8, 15}

    assert {
        0: [(0, 1), (2, 3), (4, 5), (6, 7)],
        1: [(0, 2), (1, 3), (4, 6), (5, 7)],
        2: [(0, 4), (1, 5), (2, 6), (3, 7)],
        3: [(0, 8), (7, 15)]
    }

    assert boolf.hypersplits_detailed == {
        1: [
            {'atomkeys': [0], 'setpart': {'0': [0, 2, 4, 6, 8], '1': [1, 3, 5, 7, 15]}},
            {'atomkeys': [1], 'setpart': {'0': [0, 1, 4, 5, 8], '1': [2, 3, 6, 7, 15]}},
            {'atomkeys': [2], 'setpart': {'0': [0, 1, 2, 3, 8], '1': [4, 5, 6, 7, 15]}},
            {'atomkeys': [3], 'setpart': {'0': [0, 1, 2, 3, 4, 5, 6, 7], '1': [8, 15]}}
        ],
        2: [
            {'atomkeys': [0, 1], 'setpart': {'00': [0, 4, 8], '10': [1, 5], '01': [2, 6], '11': [3, 7, 15]}},
            {'atomkeys': [0, 2], 'setpart': {'00': [0, 2, 8], '10': [1, 3], '01': [4, 6], '11': [5, 7, 15]}},
            {'atomkeys': [0, 3], 'setpart': {'00': [0, 2, 4, 6], '10': [1, 3, 5, 7], '01': [8], '11': [15]}},
            {'atomkeys': [1, 2], 'setpart': {'00': [0, 1, 8], '10': [2, 3], '01': [4, 5], '11': [6, 7, 15]}},
            {'atomkeys': [1, 3], 'setpart': {'00': [0, 1, 4, 5], '10': [2, 3, 6, 7], '01': [8], '11': [15]}},
            {'atomkeys': [2, 3], 'setpart': {'00': [0, 1, 2, 3], '10': [4, 5, 6, 7], '01': [8], '11': [15]}}
        ],
        3: [
            {'atomkeys': [0, 1, 2], 'setpart': {'000': [0, 8], '100': [1], '010': [2], '110': [3], '001': [4], '101': [5], '011': [6], '111': [7, 15]}}
        ]
    }
