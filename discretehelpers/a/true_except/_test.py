import pytest

from . import true_except


def test():
    with pytest.raises(FooError):
        true_except(False, FooError)


class FooError(Exception):
    """Foo."""
