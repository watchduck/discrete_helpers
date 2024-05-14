class ArgTypeError(TypeError):
    """The first argument of `Perm` must be a list (of integers or lists) or a dict."""


class SequenceError(ValueError):
    """A sequence of length n must contain all integers from 0 to n-1."""


class CyclesError(ValueError):
    """The cycles must be lists of integers."""


class DictError(ValueError):
    """Keys and values of the dict must be from the same set of integers."""


class PeriodLengthNotNaturalError(TypeError):
    """The period must be an integer >= 0."""


class PerilenTooSmallError(ValueError):
    """The period must be >= 2 and > the greatest element moved by the permutation."""


class OtherNotPermError(TypeError):
    """If `a` is of type Perm, these expressions make only sense if `b` is as well: `a * b`, `a == b`"""


class OtherPerilenMismatchError(ValueError):
    """This method can only concatenate permutations that are both finite or both periodic."""


class LengthMismatchPerilenError(ValueError):
    """When a periodic permutation is represented as a sequence, its length must be a multiple of the period length."""


class LengthTooSmallError(ValueError):
    """When a finite permutation is represented as a sequence, its length must be greater than the moved elements."""


class IsNeutralFail(Exception):
    """used for control flow"""


class NotPeriodicError(ValueError):
    """This method is only for periodic permutations."""
