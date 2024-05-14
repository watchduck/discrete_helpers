from discretehelpers.boolf import Boolf


def test_sapigi():  # `sapigi` with gapspots 11, 13, 15

    fullspots = {1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15}
    atomvals = [0, 1, 2, 3]
    boolf = Boolf(fullspots=fullspots, atomvals=atomvals, skip_deflation=True)
    assert boolf.fullspots == fullspots
    assert boolf.atomvals == atomvals
    assert boolf.is_blightless
    assert boolf.hypersplits_pretty() == {
        1: [
            {'−A': [8, 10, 12, 14], '+A': [1, 3, 5, 7, 9, 11, 13, 15]},
            {'−B': [1, 5, 8, 9, 12, 13], '+B': [3, 7, 10, 11, 14, 15]},
            {'−C': [1, 3, 8, 9, 10, 11], '+C': [5, 7, 12, 13, 14, 15]},
            {'−D': [1, 3, 5, 7], '+D': [8, 9, 10, 11, 12, 13, 14, 15]}
        ],
        2: [
            {'−A −B': [8, 12], '+A −B': [1, 5, 9, 13], '−A +B': [10, 14], '+A +B': [3, 7, 11, 15]},
            {'−A −C': [8, 10], '+A −C': [1, 3, 9, 11], '−A +C': [12, 14], '+A +C': [5, 7, 13, 15]},
            {'−B −C': [1, 8, 9], '+B −C': [3, 10, 11], '−B +C': [5, 12, 13], '+B +C': [7, 14, 15]},
            {'−B −D': [1, 5], '+B −D': [3, 7], '−B +D': [8, 9, 12, 13], '+B +D': [10, 11, 14, 15]},
            {'−C −D': [1, 3], '+C −D': [5, 7], '−C +D': [8, 9, 10, 11], '+C +D': [12, 13, 14, 15]}
        ],
        3: [
            {'−A −B −C': [8], '+A −B −C': [1, 9], '−A +B −C': [10], '+A +B −C': [3, 11], '−A −B +C': [12], '+A −B +C': [5, 13], '−A +B +C': [14], '+A +B +C': [7, 15]},
            {'−B −C −D': [1], '+B −C −D': [3], '−B +C −D': [5], '+B +C −D': [7], '−B −C +D': [8, 9], '+B −C +D': [10, 11], '−B +C +D': [12, 13], '+B +C +D': [14, 15]}
        ]
    }


def test_true():

    boolf = Boolf('1111 1111', skip_deflation=True)
    assert boolf.fullspots == {0, 1, 2, 3, 4, 5, 6, 7}
    assert boolf.atomvals == [0, 1, 2]
    assert boolf.hypersplits_pretty() == {
        1: [
            {'−A': [0, 2, 4, 6], '+A': [1, 3, 5, 7]},
            {'−B': [0, 1, 4, 5], '+B': [2, 3, 6, 7]},
            {'−C': [0, 1, 2, 3], '+C': [4, 5, 6, 7]}
        ],
        2: [
            {'−A −B': [0, 4], '+A −B': [1, 5], '−A +B': [2, 6], '+A +B': [3, 7]},
            {'−A −C': [0, 2], '+A −C': [1, 3], '−A +C': [4, 6], '+A +C': [5, 7]},
            {'−B −C': [0, 1], '+B −C': [2, 3], '−B +C': [4, 5], '+B +C': [6, 7]}
        ],
        3: [
            {'−A −B −C': [0], '+A −B −C': [1], '−A +B −C': [2], '+A +B −C': [3], '−A −B +C': [4], '+A −B +C': [5], '−A +B +C': [6], '+A +B +C': [7]}
        ]
    }


def test_false():

    boolf = Boolf('0000 0000', skip_deflation=True)
    assert boolf.fullspots == set()
    assert boolf.atomvals == [0, 1, 2]
    assert boolf.hypersplits_pretty() == {
        1: [
            {'−A': [], '+A': []},
            {'−B': [], '+B': []},
            {'−C': [], '+C': []}
        ]
    }


def test_atom():

    boolf = Boolf('0011 0011', skip_deflation=True)
    assert boolf.fullspots == {2, 3, 6, 7}
    assert boolf.atomvals == [0, 1, 2]
    assert boolf.splits == [
        ({3, 7}, {2, 6}),
        ({2, 3, 6, 7}, set()),
        ({6, 7}, {2, 3})
    ]