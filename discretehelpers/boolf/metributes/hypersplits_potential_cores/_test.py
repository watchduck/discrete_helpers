from discretehelpers.boolf.examples import godogi


def test():

    assert godogi.hypersplits_potential_cores == {
        1: [
            {'fixed': [0], 'free': [1, 2], 'determined': {3: -1}, 'vectors': [[0, -1, -1, -1], [0, -1, 1, -1], [0, 1, -1, -1], [0, 1, 1, -1]]},
            {'fixed': [1], 'free': [0, 2, 3], 'determined': {}, 'vectors': [[-1, 0, -1, -1], [-1, 0, -1, 1], [-1, 0, 1, -1], [-1, 0, 1, 1], [1, 0, -1, -1], [1, 0, -1, 1], [1, 0, 1, -1], [1, 0, 1, 1]]},
            {'fixed': [2], 'free': [0, 1, 3], 'determined': {}, 'vectors': [[-1, -1, 0, -1], [-1, -1, 0, 1], [-1, 1, 0, -1], [-1, 1, 0, 1], [1, -1, 0, -1], [1, -1, 0, 1], [1, 1, 0, -1], [1, 1, 0, 1]]},
            {'fixed': [3], 'free': [1, 2], 'determined': {0: -1}, 'vectors': [[-1, -1, -1, 0], [-1, -1, 1, 0], [-1, 1, -1, 0], [-1, 1, 1, 0]]}
        ],
        2: [
            {'fixed': [0, 1], 'free': [2], 'determined': {3: -1}, 'vectors': [[0, 0, -1, -1], [0, 0, 1, -1]]},
            {'fixed': [0, 2], 'free': [1], 'determined': {3: -1}, 'vectors': [[0, -1, 0, -1], [0, 1, 0, -1]]},
            {'fixed': [1, 2], 'free': [0, 3], 'determined': {}, 'vectors': [[-1, 0, 0, -1], [-1, 0, 0, 1], [1, 0, 0, -1], [1, 0, 0, 1]]},
            {'fixed': [1, 3], 'free': [2], 'determined': {0: -1}, 'vectors': [[-1, 0, -1, 0], [-1, 0, 1, 0]]},
            {'fixed': [2, 3], 'free': [1], 'determined': {0: -1}, 'vectors': [[-1, -1, 0, 0], [-1, 1, 0, 0]]}
        ],
        3: [
            {'fixed': [1, 2, 3], 'free': [], 'determined': {0: -1}, 'vectors': [[-1, 0, 0, 0]]}
        ]
    }
