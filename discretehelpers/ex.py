class ArgComboError(ValueError):
    """The combination of arguments used is wrong. (Before even looking at their values.)"""


class ArgMismatchError(ValueError):
    """The values of arguments does not match. (E.g. because 2 lists are not of the same length.)"""


class ArgTypeError(TypeError):
    """The type of an argument is wrong. (E.g. an integer might be of type `numpy.int64` instead of `int`.)"""


class ArgValueError(ValueError):
    """The value of an argument is wrong. """


class ArgTooSmallError(ArgValueError):
    """An argument is too small. (E.g. because the requested arity is below the actual arity.)"""


class ArgTooBigError(ArgValueError):
    """An argument is too big."""


class ArgNotFeasibleError(ArgTooBigError):
    """Theoretically possible , but too big to calculate."""
