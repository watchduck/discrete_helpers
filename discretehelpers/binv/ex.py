class ArgumentError(ValueError):
    """Either `vector`, `spotint` or `exposet` must be set. Optional `length` only makes sense for `spotint` and exposet`."""


class LengthError(ValueError):
    """`length` is too small for the provided `spotint` or `exposet`."""


class VectorTypeError(ValueError):
    """The vector must be of type `list`, `tuple` or `str`."""


class VectorEntryError(ValueError):
    """The vector entries must be binary."""


class IntvalError(ValueError):
    """Argument `spotint` must be positive integer."""


class IndicesTypeError(ValueError):
    """Argument `exposet` should be set. (List and tuple are allowed.)"""


class IndicesEntryError(ValueError):
    """Argument `exposet` must contain positive integers."""


class InsertPlaceError(ValueError):
    """The insert place must be in the closed interval 0..length."""


class InsertValueError(ValueError):
    """The inserted value must be boolean in nature (though not in type)."""
