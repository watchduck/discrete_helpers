from discretehelpers.boolf.examples.e10_gap_variants_basiga import sarina, letters_a_to_h
from discretehelpers.boolf.examples import basiga_fs


def test_sarina():
    assert sarina.splits == [
        ({1, 3}, {0, 2, 4, 6, 8, 10, 106, 202, 24, 26}),  # a 0
        ({2, 3, 26, 6, 106, 202, 10}, {0, 1, 4, 8, 24}),  # b 1
        ({4, 6}, {0, 1, 2, 3, 8, 10, 106, 202, 24, 26}),  # c 2
        ({26, 106, 8, 202, 10, 24}, {0, 1, 2, 3, 4, 6}),  # d 3
        ({24, 26}, {0, 1, 2, 3, 4, 6, 8, 10, 106, 202}),  # e 4
        ({106}, {0, 1, 2, 3, 4, 6, 8, 10, 202, 24, 26}),  # f 5
        ({202, 106}, {0, 1, 2, 3, 4, 6, 8, 10, 24, 26}),  # g 6
        ({202}, {0, 1, 2, 3, 4, 6, 8, 10, 106, 24, 26})   # h 7
    ]
    assert sarina.filtrated_pairs_pretty(letters_a_to_h) == {
        'crossing': [('A', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E')],
        'disjoint': [('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('C', 'D'), ('C', 'E'), ('C', 'F'), ('C', 'G'), ('C', 'H'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'H')],
        'subset': [('E', 'D'), ('F', 'B'), ('F', 'D'), ('F', 'G'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D'), ('H', 'G')]
    }
