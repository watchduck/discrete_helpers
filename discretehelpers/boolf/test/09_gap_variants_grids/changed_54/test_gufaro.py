from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e09_gap_variants_grids import gufaro, gufaro_fs


def test_gufaro():
    assert gufaro.fullspots == gufaro_fs
    assert gufaro.splits == [
        ({27, 59, 11}, {2, 10, 56, 24, 58, 12, 28}),       # a 0 0
        ({2, 58, 11, 27, 10, 59}, {24, 56, 12, 28}),       # b 1 1
        ({12, 28}, {2, 58, 59, 10, 11, 24, 56, 27}),       # d 3 2
        ({58, 59, 10, 11, 12, 24, 56, 27, 28}, {2}),       # e 4 3
        ({56, 24, 27, 58, 59, 28}, {11, 2, 10, 12}),       # f 5 4
        ({56, 58, 59}, {2, 24, 27, 10, 11, 12, 28}),       # g 6 5
        (set(), {2, 58, 59, 10, 11, 12, 24, 56, 27, 28})   # h 7 6
    ]
    assert gufaro.bloat == SetPartComp([])
    assert gufaro.blight == SetPartComp([], {(-1, 6)})
    assert gufaro.bloat_boolf == Boolf('1')
    assert gufaro.blight_boolf == Boolf('10', [7])
    assert gufaro.bloatless_boolf == Boolf(fullspots={2, 58, 59, 10, 11, 12, 24, 56, 27, 28}, atomvals=[0, 1, 3, 4, 5, 6, 7]) == gufaro
    assert gufaro.blightless_boolf == Boolf(fullspots={2, 58, 59, 10, 11, 12, 24, 56, 27, 28}, atomvals=[0, 1, 3, 4, 5, 6])
    assert gufaro == gufaro.blight_boolf & gufaro.blightless_boolf
    assert gufaro.onesided_atomkeys == [6]
    assert gufaro.onesided_is_universe == {6: False}
