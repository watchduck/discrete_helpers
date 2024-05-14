from discretehelpers.boolf.examples.e10_gap_variants_basiga import doguva, letters_a_to_h, t10_all_spot_degrees, t10_common_disjoint_pairs
from discretehelpers.boolf.examples import basiga, basiga_fs


def test_doguva():
    assert doguva.gapless_boolf == basiga
    assert doguva.splits == [
        ({1, 3, 5}, {0, 2, 4, 6, 8, 42, 74, 12, 106, 14, 138, 202, 24, 28, 30}),  # a 0
        ({2, 3, 6, 42, 74, 106, 138, 14, 202, 30}, {0, 1, 4, 5, 8, 12, 24, 28}),  # b 1
        ({4, 5, 6, 30, 12, 28, 14}, {0, 1, 2, 3, 8, 42, 74, 106, 138, 202, 24}),  # c 2
        ({8, 42, 74, 12, 106, 14, 138, 202, 24, 28, 30}, {0, 1, 2, 3, 4, 5, 6}),  # d 3
        ({24, 28, 30}, {0, 1, 2, 3, 4, 5, 6, 8, 42, 74, 12, 106, 14, 138, 202}),  # e 4
        ({42, 106}, {0, 1, 2, 3, 4, 5, 6, 8, 74, 138, 12, 202, 14, 24, 28, 30}),  # f 5
        ({202, 74, 106}, {0, 1, 2, 3, 4, 5, 6, 8, 42, 138, 12, 14, 24, 28, 30}),  # g 6
        ({202, 138}, {0, 1, 2, 3, 4, 5, 6, 8, 74, 12, 14, 24, 28, 30, 42, 106})   # h 7
    ]
    assert doguva.filtrated_pairs_pretty(letters_a_to_h) == {
        'crossing': [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E'), ('F', 'G'), ('G', 'H')],
        'disjoint': t10_common_disjoint_pairs,
        'subset': [('E', 'D'), ('F', 'B'), ('F', 'D'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D')]
    }
