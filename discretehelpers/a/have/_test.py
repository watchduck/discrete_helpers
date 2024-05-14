import numpy

from . import have


def test():
    assert not have(None)  # `None` is the only argument for which `have` should return `False`.
    assert have([])
    assert have(0)
    assert have(1)
    assert have(-1)
    assert have('')
    assert have("""""")
    assert have(' ')
    assert have(False)
    assert have(True)
    assert have('None')
    assert have(numpy.nan)
