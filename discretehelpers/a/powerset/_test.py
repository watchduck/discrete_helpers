from . import powerset


def test():

    chain_object = powerset(['a', 'b', 'c'])
    assert list(chain_object) == [(), ('a',), ('b',), ('c',), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]
