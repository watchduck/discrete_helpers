from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples.e09_gap_variants_grids import tinefa, tinefa_fs


def test_tinefa():
    assert tinefa.fullspots == tinefa_fs
    assert tinefa.splits == [
        ({115, 51, 19}, {16, 48, 18, 112, 52, 114}),       # a 0
        ({18, 115, 51, 19, 114}, {16, 48, 52, 112}),       # b 1
        ({52}, {16, 48, 18, 19, 51, 112, 114, 115}),       # c 2
        (set(), {16, 48, 18, 19, 51, 52, 112, 114, 115}),  # d 3
        ({16, 48, 18, 19, 51, 52, 112, 114, 115}, set()),  # e 4
        ({48, 112, 114, 51, 52, 115}, {16, 18, 19}),       # f 5
        ({112, 114, 115}, {16, 48, 18, 19, 51, 52}),       # g 6
        (set(), {16, 48, 18, 19, 51, 52, 112, 114, 115})   # h 7
    ]
    assert tinefa.bloat == SetPartComp([[3, 7]], {(3, 4)})  # 3 = 7 (= empty) ;  3 (= 7) comp 4 (= univ)
    assert tinefa.blight == SetPartComp([[-1, 4], [3, 7]], {(-1, 3)})  # univ -1 = 4 ;  3 = 7 (= empty) ;  univ -1 (= 4) comp 3 (= 7 = empty)
    assert tinefa.bloat_boolf == Boolf('0010 0100', [3, 4, 7])
    assert tinefa.blight_boolf == Boolf('0010 0000', [3, 4, 7])
    assert tinefa.bloatless_boolf == Boolf(fullspots={8, 10, 11, 24, 27, 28, 56, 58, 59}, atomvals=[0, 1, 2, 4, 5, 6])  # a, b, c, e, f, g
    assert tinefa.blightless_boolf == Boolf(fullspots={0, 2, 3, 8, 11, 12, 24, 26, 27}, atomvals=[0, 1, 2, 5, 6])  # a, b, c, f, g
    assert tinefa == tinefa.bloat_boolf & tinefa.bloatless_boolf == tinefa.blight_boolf & tinefa.blightless_boolf
    assert tinefa.onesided_atomkeys == [3, 4, 7]  # d, e, h
    assert tinefa.onesided_is_universe == {3: False, 4: True, 7: False}  # d empty, e univ, h empty
