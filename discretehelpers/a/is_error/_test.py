from . import is_error


def test():

    assert is_error(ValueError)
    assert is_error(FooError)

    assert not is_error('123')
    assert not is_error(SomethingElse)


class FooError(ZeroDivisionError):
    """Whatever."""


class SomethingElse(object):
    pass