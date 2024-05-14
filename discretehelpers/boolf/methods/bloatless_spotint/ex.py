class BloatMismatchError(ValueError):
    """The `spotint` entered in `bloatless_spotint()` does not match `bloat`."""


class TooBigError(ValueError):
    """The `spotint` entered in `bloatless_spotint()` is supposed to denote a spot of the Boolf, so it should be smaller than 2**valency."""
