class SetEqualComplementsError(ValueError):
    """Complementary elements can not be made equal."""


class SetCompEqualsError(ValueError):
    """Equal elements can not be made complements."""


class CompWithoutPartError(ValueError):
    """The argument `complement` makes only sense when `part` is also set."""


class PartCompMismatchError(ValueError):
    """Elements are defined as equal in `part` but as complementary in `complement`."""
