from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e09_gap_variants_grids import temapi, temapi_fs


def test_temapi():
    assert temapi.fullspots == temapi_fs
    assert temapi.splits == [
        (set(), {8, 24, 56, 120}),  # a 0 0
        (set(), {8, 24, 56, 120}),  # b 1 1
        (set(), {8, 24, 56, 120}),  # d 3 2
        ({8, 24, 56, 120}, set()),  # e 4 3
        ({24, 56, 120}, {8}),       # f 5 4
        ({56, 120}, {8, 24}),       # g 6 5
        ({120}, {8, 24, 56})        # h 7 6
    ]
    assert temapi.bloat == SetPartComp([[0, 1, 2]], {(0, 3)})
    assert temapi.blight == SetPartComp([[-1, 3], [0, 1, 2]], {(-1, 0)})
    assert temapi.bloat_boolf == Boolf('0000 0001 1000 0000', [0, 1, 3, 4])
    assert temapi.blight_boolf == Boolf('0000 0000 1000 0000', [0, 1, 3, 4])  # a, b, d, e
    assert temapi.bloatless_boolf == Boolf('0101 0001 0000 0001', [4, 5, 6, 7])
    assert temapi.blightless_boolf == Boolf('1101 0001', [5, 6, 7])  # f, g, h  (fullspots 0, 1, 3, 7)
    assert temapi == temapi.bloat_boolf & temapi.bloatless_boolf == temapi.blight_boolf & temapi.blightless_boolf
    assert temapi.onesided_atomkeys == [0, 1, 2, 3]
    assert temapi.onesided_is_universe == {0: False, 1: False, 2: False, 3: True}
