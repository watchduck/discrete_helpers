from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf.examples.e05_blight import tokosi

from .ex import *


tokosi_bloated_to_bloatless = {
    2: 2,
    3: 3,
    6: 6,
    7: 7,

    24: 0,
    25: 1,
    28: 4,
    29: 5
}


def test_tokosi():
    for bloated, bloatless in tokosi_bloated_to_bloatless.items():
        assert tokosi.bloatless_spotint(bloated) == bloatless

    abbrev(BloatMismatchError, [
        lambda: tokosi.bloatless_spotint(10),
        lambda: tokosi.bloatless_spotint(12),
        lambda: tokosi.bloatless_spotint(23),
        lambda: tokosi.bloatless_spotint(31)
    ])

    abbrev(TooBigError, [
        lambda: tokosi.bloatless_spotint(32)
    ])
