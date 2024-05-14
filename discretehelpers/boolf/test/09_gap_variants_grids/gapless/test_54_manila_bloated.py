from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e09_gap_variants_grids import manila_bloated, manila_bloated_fs


def test_manila_bloated():
    assert manila_bloated.fullspots == manila_bloated_fs
    assert manila_bloated.splits == [
        ({3, 19, 51, 115, 243}, {2, 4, 12, 60, 124, 18, 50, 20, 52, 114, 116, 242, 244, 252, 28}),  # a 0
        ({2, 3, 18, 19, 50, 51, 114, 115, 242, 243}, {4, 12, 60, 124, 20, 52, 116, 244, 252, 28}),  # b 1
        ({4, 12, 60, 124, 20, 52, 116, 244, 252, 28}, {2, 3, 18, 19, 50, 51, 114, 115, 242, 243}),  # c 2
        ({124, 252, 12, 28, 60}, {2, 3, 4, 18, 19, 20, 50, 51, 52, 114, 115, 116, 242, 243, 244}),  # d 3
        ({18, 19, 20, 28, 60, 124, 50, 243, 51, 52, 114, 115, 116, 242, 244, 252}, {2, 3, 4, 12}),  # e 4
        ({124, 50, 51, 52, 114, 115, 116, 242, 243, 244, 252, 60}, {2, 3, 4, 12, 18, 19, 20, 28}),  # f 5
        ({242, 114, 115, 116, 243, 244, 252, 124}, {2, 3, 4, 12, 60, 18, 19, 20, 50, 51, 52, 28}),  # g 6
        ({242, 243, 244, 252}, {2, 3, 4, 12, 18, 19, 20, 28, 124, 50, 51, 52, 114, 115, 116, 60})   # h 7
    ]
    assert manila_bloated.atomvals == [0, 1, 2, 3, 4, 5, 6, 7]
    assert manila_bloated.bloatless_atomkeys_undeflated == [0, 1, 3, 4, 5, 6, 7]  # without c
    assert manila_bloated.bloat == SetPartComp([], {(1, 2)})  # b comp c
    assert manila_bloated.bloat_boolf == Boolf('0110', [1, 2])
