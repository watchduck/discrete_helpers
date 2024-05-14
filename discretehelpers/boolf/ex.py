class SarityVectorMismatchError(ValueError):
    """Vector length and number of atomvals do not match."""


class AtomvalsNotUniqueError(ValueError):
    """The argument `atomvals` must be a list of integers without duplicates."""


class AtomvalNegativeError(ValueError):
    """The atomvals must be non-negative integers. (They can be permuted, but not negated.)"""


class BoolfNotBlightlessError(ValueError):
    """At this point a blightless Boolf is required."""


class FullspotsWithoutAtomvalsError(ValueError):
    """The argument `fullspots` requires also the argument `atomvals`."""


class NotBundleError(Exception):
    """Some operations work only for Boolfs that are bundles."""


class NotPairOfAtomKeysError(ValueError):
    """A pair of atoms must be two different positive integers smaller than the valency."""


class NotSpreadlessError(ValueError):
    pass
