from discretehelpers.boolf import Boolf
from discretehelpers.set_part_comp import SetPartComp

from discretehelpers.boolf.examples import bareto, barogi as bareto_bloatless


def test_():

    assert bareto.bloat == SetPartComp([], {(1, 2)})
    assert bareto.bloat_boolf == Boolf('0110', [1, 2])  # b, c

    assert bareto.splits == [
        ({3, 5}, {2, 10, 4, 12}),  # a 0
        ({10, 2, 3}, {12, 4, 5}),  # b 1
        ({12, 4, 5}, {10, 2, 3}),  # c 2
        ({10, 12}, {2, 3, 4, 5})   # d 3
    ]

    assert bareto.splits_equality_blocks        == [ [0], [1, 2],  [3]]
    assert bareto.splits_preferred_side         == [None,      1, None]
    assert bareto.bloatless_atomkeys_undeflated == [   0,      1,    3]

    assert bareto.bloatless_atomkeys_deflated == [0, 3]  # a, d

    bareto_bloatless_inflated = Boolf(fullspots={0, 1, 2, 3, 4, 6}, atomvals=[0, 1, 3])

    assert bareto.bloatless_boolf == bareto_bloatless == bareto_bloatless_inflated
