class TooManyArgumentsError(ValueError):
    """`WalshPerm` can only have one argument."""


class NotWalshPermError(ValueError):
    """This is not a Walsh permutation."""


class NotEvenPermutationError(NotWalshPermError):
    """This is not even a permutation, let alone a Walsh permutation."""


class InvalidPermError(NotWalshPermError):
    """This permutation is not a Walsh permutation."""


class InvalidMatrixError(NotWalshPermError):
    """This matrix does not describe a Walsh permutation."""


class RequestedDegreeSmallerActualDegreeError(ValueError):
    """The requested degree (e.g. the vector length) must be >= the actual degree."""


class RedundantParametersError(ValueError):
    """Only one of these parameters should be chosen. (`length` or `degree`)"""


class NotPowerOfTwoError(ValueError):
    """The length of a Walsh permutation must be a power of two."""
