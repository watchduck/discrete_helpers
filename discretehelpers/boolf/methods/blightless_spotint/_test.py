from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf.methods.bloatless_spotint.ex import BloatMismatchError, TooBigError
from .ex import BlightMismatchError

from discretehelpers.boolf.examples.e10_gap_variants_basiga import bitada


def test_results():
    assert [bitada.blightless_spotint(_) for _ in [2, 7, 10, 26, 74, 138]] == [0, 1, 2, 6, 10, 18]


def test_raise_bloat():
    abbrev(BloatMismatchError, [
        lambda: bitada.blightless_spotint(0),
        lambda: bitada.blightless_spotint(34),  # .b...f.. matches (a = c) but contradicts (b comp f)
        lambda: bitada.blightless_spotint(36),  # ..c..f.. matches (b comp f) but contradicts (a = c)
        lambda: bitada.blightless_spotint(255)
    ])
    abbrev(TooBigError, [
        lambda: bitada.blightless_spotint(256),
        lambda: bitada.blightless_spotint(999)
    ])


def test_raise_blight():
    # Both examples match `bloat`, because (a = c) and (b comp f). But `blight` requires (b = 1) and (f = 0).
    abbrev(BlightMismatchError, [
        lambda: bitada.blightless_spotint(32),  # .....f..
        lambda: bitada.blightless_spotint(37),  # a.c..f..
    ])
