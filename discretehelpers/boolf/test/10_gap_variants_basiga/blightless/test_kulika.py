from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import kulika, letters_a_to_h, t10_all_spot_degrees, t10_common_disjoint_pairs
from discretehelpers.boolf.examples import basiga_fs


def test_kulika():
    assert kulika.splits == [
        ({3, 5}, {0, 6, 10, 106, 12, 202, 24, 30}),  # a 0
        ({3, 6, 106, 202, 10, 30}, {0, 24, 12, 5}),  # b 1
        ({12, 5, 6, 30}, {0, 3, 106, 24, 202, 10}),  # c 2
        ({106, 24, 202, 10, 12, 30}, {0, 3, 5, 6}),  # d 3
        ({24, 30}, {0, 3, 5, 6, 10, 106, 12, 202}),  # e 4
        ({106}, {0, 3, 5, 6, 10, 202, 12, 24, 30}),  # f 5
        ({202, 106}, {0, 3, 5, 6, 10, 12, 24, 30}),  # g 6
        ({202}, {0, 3, 5, 6, 10, 106, 12, 24, 30})   # h 7
    ]
    assert kulika.filtrated_pairs_pretty(letters_a_to_h) == {
        'crossing': [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E')],
        'disjoint': t10_common_disjoint_pairs,
        'subset': [('E', 'D'), ('F', 'B'), ('F', 'D'), ('F', 'G'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D'), ('H', 'G')]
    }
