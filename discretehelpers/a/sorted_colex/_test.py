from itertools import product

from . import sorted_colex


def test_words():
    words = [''.join(_) for _ in product(['a', 'b', 'c'], repeat=3)]
    assert sorted_colex(words) == [
        'aaa',
        'baa',
        'caa',
        'aba',
        'bba',
        'cba',
        'aca',
        'bca',
        'cca',
        'aab',
        'bab',
        'cab',
        'abb',
        'bbb',
        'cbb',
        'acb',
        'bcb',
        'ccb',
        'aac',
        'bac',
        'cac',
        'abc',
        'bbc',
        'cbc',
        'acc',
        'bcc',
        'ccc'
    ]


def test_binary():
    # colexicographic order of binary vectors
    assert sorted_colex(product([0, 1], repeat=4)) == [
        (0, 0, 0, 0),   # 0
        (1, 0, 0, 0),   # 1
        (0, 1, 0, 0),   # 2
        (1, 1, 0, 0),   # 3
        (0, 0, 1, 0),   # 4
        (1, 0, 1, 0),   # 5
        (0, 1, 1, 0),   # 6
        (1, 1, 1, 0),   # 7
        (0, 0, 0, 1),   # 8
        (1, 0, 0, 1),   # 9
        (0, 1, 0, 1),  # 10
        (1, 1, 0, 1),  # 11
        (0, 0, 1, 1),  # 12
        (1, 0, 1, 1),  # 13
        (0, 1, 1, 1),  # 14
        (1, 1, 1, 1)   # 15
    ]
