from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import kokabi, letters_a_to_h, t10_all_spot_degrees, t10_common_disjoint_pairs
from discretehelpers.boolf.examples import basiga_fs


def test_kokabi():
    assert kokabi.splits == [
        ({5, 7}, {0, 2, 6, 42, 74, 202, 14, 26, 28, 30}),  # a 0
        ({2, 6, 7, 42, 74, 202, 14, 26, 30}, {0, 28, 5}),  # b 1
        ({30, 5, 6, 7, 28, 14}, {0, 2, 26, 74, 202, 42}),  # c 2
        ({26, 74, 30, 202, 42, 28, 14}, {0, 2, 5, 6, 7}),  # d 3
        ({26, 28, 30}, {0, 2, 5, 6, 7, 42, 74, 202, 14}),  # e 4
        ({42}, {0, 2, 5, 6, 7, 74, 202, 14, 26, 28, 30}),  # f 5
        ({202, 74}, {0, 2, 5, 6, 7, 42, 14, 26, 28, 30}),  # g 6
        ({202}, {0, 2, 5, 6, 7, 42, 74, 14, 26, 28, 30})   # h 7
    ]
    assert kokabi.filtrated_pairs_pretty(letters_a_to_h) == {
        'disjoint': sorted(t10_common_disjoint_pairs + [('F', 'G')]),
        'crossing': [('A', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E')],
        'subset': [('A', 'C'), ('E', 'D'), ('F', 'B'), ('F', 'D'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D'), ('H', 'G')]
    }
