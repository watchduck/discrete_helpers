from discretehelpers.a import subdict

from discretehelpers.boolf.examples.e10_gap_variants_basiga import vumali, letters_a_to_h, t10_all_spot_degrees, t10_common_disjoint_pairs
from discretehelpers.boolf.examples import basiga_fs


def test_vumali():
    assert vumali.splits == [
        ({3, 5, 7}, {2, 42, 106, 202, 10, 28, 30}),  # a 0
        ({2, 3, 7, 10, 42, 106, 202, 30}, {28, 5}),  # b 1
        ({28, 5, 30, 7}, {2, 3, 42, 106, 202, 10}),  # c 2
        ({42, 106, 202, 10, 28, 30}, {2, 3, 5, 7}),  # d 3
        ({28, 30}, {2, 3, 5, 7, 10, 42, 106, 202}),  # e 4
        ({42, 106}, {2, 3, 5, 7, 10, 202, 28, 30}),  # f 5
        ({202, 106}, {2, 3, 5, 7, 10, 42, 28, 30}),  # g 6
        ({202}, {2, 3, 5, 7, 10, 42, 106, 28, 30})   # h 7
    ]
