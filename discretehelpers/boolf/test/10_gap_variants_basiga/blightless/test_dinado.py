from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import dinado, letters_a_to_h, t10_all_spot_degrees, t10_common_disjoint_pairs
from discretehelpers.boolf.examples import basiga_fs


def test_dinado():
    assert dinado.splits == [
        ({1, 7}, {0, 2, 8, 74, 106, 12, 138, 14, 202, 24, 26, 28}),  # a 0
        ({2, 7, 74, 106, 138, 202, 14, 26}, {0, 1, 8, 24, 12, 28}),  # b 1
        ({12, 28, 14, 7}, {0, 1, 2, 8, 74, 106, 138, 202, 24, 26}),  # c 2
        ({8, 74, 106, 12, 138, 14, 202, 24, 26, 28}, {0, 1, 2, 7}),  # d 3
        ({24, 26, 28}, {0, 1, 2, 7, 8, 74, 106, 12, 138, 14, 202}),  # e 4
        ({106}, {0, 1, 2, 7, 8, 74, 138, 12, 202, 14, 24, 26, 28}),  # f 5
        ({202, 74, 106}, {0, 1, 2, 7, 8, 138, 12, 14, 24, 26, 28}),  # g 6
        ({202, 138}, {0, 1, 2, 7, 8, 74, 106, 12, 14, 24, 26, 28})   # h 7
    ]

    assert dinado.filtrated_pairs_pretty(letters_a_to_h) == {
        'disjoint': t10_common_disjoint_pairs,
        'crossing': [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E'), ('G', 'H')],
        'subset': [('E', 'D'), ('F', 'B'), ('F', 'D'), ('F', 'G'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D')]
    }
