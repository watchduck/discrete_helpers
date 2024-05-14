from . import subdict


def test():
    foo = {1: 11, 2: 22, 4: 44}
    bar = subdict(original=foo, drop=[1], fresh={2: 222, 6: 666})
    assert bar == {2: 222, 4: 44, 6: 666}
