from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import torova, letters_a_to_h, t10_all_spot_degrees, t10_filtrated_pairs_pretty_of_teloti_and_lenevu
from discretehelpers.boolf.examples import basiga_fs


def test_lenevu():
    assert torova.splits == [
        ({1, 7}, {2, 4, 8, 42, 74, 138, 14, 26, 28}),  # a 0
        ({2, 26, 138, 74, 7, 42, 14}, {8, 1, 4, 28}),  # b 1
        ({4, 28, 14, 7}, {1, 2, 26, 74, 138, 8, 42}),  # c 2
        ({26, 74, 138, 8, 42, 28, 14}, {1, 2, 4, 7}),  # d 3
        ({26, 28}, {1, 2, 4, 7, 8, 42, 74, 138, 14}),  # e 4
        ({42}, {1, 2, 4, 7, 8, 74, 138, 14, 26, 28}),  # f 5
        ({74}, {1, 2, 4, 7, 8, 42, 138, 14, 26, 28}),  # g 6
        ({138}, {1, 2, 4, 7, 8, 42, 74, 14, 26, 28})   # h 7
    ]
    assert torova.filtrated_pairs_pretty(letters_a_to_h) == t10_filtrated_pairs_pretty_of_teloti_and_lenevu
