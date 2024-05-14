from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import pamoda, letters_a_to_h, t10_all_spot_degrees, t10_common_disjoint_pairs
from discretehelpers.boolf.examples import basiga_fs


def test_pamoda():
    assert pamoda.splits == [
        ({1, 5}, {0, 2, 4, 6, 8, 74, 106, 138, 26, 28, 30}),  # a 0
        ({2, 26, 138, 6, 106, 74, 30}, {0, 1, 4, 5, 8, 28}),  # b 1
        ({4, 5, 6, 28, 30}, {0, 1, 2, 8, 74, 106, 138, 26}),  # c 2
        ({26, 106, 138, 8, 74, 28, 30}, {0, 1, 2, 4, 5, 6}),  # d 3
        ({26, 28, 30}, {0, 1, 2, 4, 5, 6, 8, 74, 106, 138}),  # e 4
        ({106}, {0, 1, 2, 4, 5, 6, 8, 74, 138, 26, 28, 30}),  # f 5
        ({74, 106}, {0, 1, 2, 4, 5, 6, 8, 138, 26, 28, 30}),  # g 6
        ({138}, {0, 1, 2, 4, 5, 6, 8, 74, 106, 26, 28, 30})   # h 7
    ]
    assert pamoda.filtrated_pairs_pretty(letters_a_to_h) == {
        'disjoint': [('A', 'B')] + t10_common_disjoint_pairs + [('G', 'H')],
        'crossing': [('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E')],
        'subset': [('E', 'D'), ('F', 'B'), ('F', 'D'), ('F', 'G'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D')]
    }
