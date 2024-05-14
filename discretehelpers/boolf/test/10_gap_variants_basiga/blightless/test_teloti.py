from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import teloti, letters_a_to_h, t10_all_spot_degrees, t10_filtrated_pairs_pretty_of_teloti_and_lenevu
from discretehelpers.boolf.examples import basiga_fs


def test_teloti():
    assert teloti.splits == [
        ({1, 3, 5}, {2, 4, 6, 8, 42, 74, 12, 138, 14, 24, 26, 28}),  # a 0
        ({2, 3, 6, 42, 74, 138, 14, 26}, {1, 4, 5, 8, 24, 12, 28}),  # b 1
        ({4, 5, 6, 12, 28, 14}, {1, 2, 3, 8, 42, 74, 138, 24, 26}),  # c 2
        ({8, 42, 74, 12, 138, 14, 24, 26, 28}, {1, 2, 3, 4, 5, 6}),  # d 3
        ({24, 26, 28}, {1, 2, 3, 4, 5, 6, 8, 42, 74, 12, 138, 14}),  # e 4
        ({42}, {1, 2, 3, 4, 5, 6, 8, 74, 138, 12, 14, 24, 26, 28}),  # f 5
        ({74}, {1, 2, 3, 4, 5, 6, 8, 42, 138, 12, 14, 24, 26, 28}),  # g 6
        ({138}, {1, 2, 3, 4, 5, 6, 8, 42, 74, 12, 14, 24, 26, 28})   # h 7
    ]
    assert teloti.filtrated_pairs_pretty(letters_a_to_h) == t10_filtrated_pairs_pretty_of_teloti_and_lenevu
