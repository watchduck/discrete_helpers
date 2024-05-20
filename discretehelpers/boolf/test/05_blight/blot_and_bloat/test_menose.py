from discretehelpers.boolf import Boolf
from discretehelpers.binv import Binv
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples import menose


def test_menose():
    assert menose.root == Binv('0110 0000')
    assert menose.atomvals == [0, 1, 2]

    assert menose.blot == SetPartComp([], {(-1, 2)})  # C is empty
    assert menose.blot_boolf == Boolf('10', [2])

    assert menose.bloat == SetPartComp([], {(0, 1)})  # A and B are complements
    assert menose.bloat_boolf == Boolf('0110')
    assert menose.bloatless_boolf == Boolf('10', [2])

    assert menose.blight == SetPartComp([], {(0, 1), (-1, 2)})
    assert menose.blight_boolf == menose
    assert menose.blightless_boolf == Boolf('1')
