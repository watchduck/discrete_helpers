from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import giteli, letters_a_to_h, t10_all_spot_degrees
from discretehelpers.boolf.examples import basiga_fs


def test_giteli():
    assert giteli.splits == [
        ({1, 3, 5}, {0, 2, 4, 8, 10, 42, 12, 74, 106, 138, 202, 24, 26, 28}),  # a 0
        ({2, 3, 10, 42, 74, 106, 138, 202, 26}, {0, 1, 4, 5, 8, 12, 24, 28}),  # b 1
        ({12, 28, 4, 5}, {0, 1, 2, 3, 8, 10, 42, 74, 106, 138, 202, 24, 26}),  # c 2
        ({8, 10, 42, 12, 74, 106, 138, 202, 24, 26, 28}, {0, 1, 2, 3, 4, 5}),  # d 3
        ({24, 26, 28}, {0, 1, 2, 3, 4, 5, 8, 10, 42, 12, 74, 106, 138, 202}),  # e 4
        ({42, 106}, {0, 1, 2, 3, 4, 5, 8, 10, 74, 12, 138, 202, 24, 26, 28}),  # f 5
        ({202, 74, 106}, {0, 1, 2, 3, 4, 5, 8, 10, 42, 12, 138, 24, 26, 28}),  # g 6
        ({202, 138}, {0, 1, 2, 3, 4, 5, 8, 10, 42, 12, 74, 106, 24, 26, 28})   # h 7
    ]
    assert giteli.filtrated_pairs_pretty(letters_a_to_h) == {
        'crossing': [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E'), ('F', 'G'), ('G', 'H')],
        'disjoint': [('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('B', 'C'), ('C', 'F'), ('C', 'G'), ('C', 'H'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'H')],
        'subset': [('E', 'D'), ('F', 'B'), ('F', 'D'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D')]
    }
