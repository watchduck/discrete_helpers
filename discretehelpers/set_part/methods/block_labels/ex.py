class UnknownBlockError(ValueError):
    """This block is not among the canonical blocks and singletons."""


class UnknownElementError(ValueError):
    """This element is not in the domain."""


class LabelContradictionError(ValueError):
    """There is already a different label for this block."""
