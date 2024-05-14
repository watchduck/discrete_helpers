from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.set_part import SetPart

from .ex import NotInDomainError, DomainNotFiniteError


def test_misc():
    a = SetPart([[2, 8], [1, 6, 3]])
    assert a == SetPart([[2, 8], [], [1, 6, 3], [88], [99]])
    assert a.blocks == [[1, 3, 6], [2, 8]]
    assert a.non_singleton_to_block_index == {1: 0, 3: 0, 6: 0, 2: 1, 8: 1}
    assert a.non_singletons == {1, 2, 3, 6, 8}
    assert a == SetPart([[3, 1, 6], [8, 2]])
    assert a.blocks_with_singletons() == [[0], [1, 3, 6], [2, 8], [4], [5], [7]]
    assert a.blocks_with_singletons(10) == [[0], [1, 3, 6], [2, 8], [4], [5], [7], [9]]

    assert a.pair_in_same_block(2, 8)
    assert a.pair_in_same_block(3, 1)
    assert not a.pair_in_same_block(1, 99)
    assert not a.pair_in_same_block(88, 99)

    assert a.non_singleton_to_block_index_or_none(6) == 0
    assert a.non_singleton_to_block_index_or_none(8) == 1
    assert a.non_singleton_to_block_index_or_none(99) is None

    assert a.element_to_block(3) == [1, 3, 6]
    assert a.element_to_block(8) == [2, 8]

    b = SetPart(a.blocks)
    b.merge_pair(1, 2)
    assert b == SetPart([[1, 3, 6, 2, 8]])

    c = SetPart(a.blocks)
    c.merge_pair(1, 9)
    assert c == SetPart([[1, 3, 6, 9], [2, 8]])
    c.merge_pair(8, 7)
    assert c == SetPart([[1, 3, 6, 9], [2, 7, 8]])
    c.merge_pair(88, 99)
    assert c == SetPart([[1, 3, 6, 9], [2, 7, 8], [88, 99]])

    d = SetPart()
    d.merge_pair(0, 1)
    assert d == SetPart([[0, 1]])
    d.merge_pair(0, 2)
    assert d == SetPart([[0, 1, 2]])
    d.merge_pair(1, 2)  # redundant
    assert d == SetPart([[0, 1, 2]])


def test_pairs():
    a = SetPart([[0, 1, 4, 5], [2, 3], [6, 7, 9]])
    assert a.pairs == {(0, 1), (6, 9), (6, 7), (4, 5), (1, 4), (1, 5), (0, 5), (2, 3), (0, 4), (7, 9)}
    b = SetPart()
    for pair in a.pairs:
        b.merge_pair(*pair)
    assert b == a


def test_domain_natural():
    p = SetPart([[2, 5], [3, 8]])  # implicitly domain N
    p.merge_pair(8, 9)
    assert p == SetPart([[2, 5], [3, 8, 9]])

    abbrev(NotInDomainError, [
        lambda: p.merge_pair(-1, 2),
        lambda: p.merge_many([-1, 1, 2])
    ])

    abbrev(DomainNotFiniteError, [
        lambda: p.singletons
    ])


def test_domain_integer():
    p = SetPart([[2, 5], [3, 8]], 'Z')
    p.merge_pair(8, 9)
    assert p == SetPart([[2, 5], [3, 8, 9]], 'Z')
    p.merge_pair(-1, 2)
    assert p == SetPart([[-1, 2, 5], [3, 8, 9]], 'Z')

    abbrev(NotInDomainError, [
        lambda: p.merge_pair(2, .5),
        lambda: p.merge_many([-1, 2, .5])
    ])


def test_domain_finite():
    domain = ['a', 'b', 'c', 'd', 'w', 'x', 'y', 'z']
    p = SetPart(blocks=[['a', 'c'], ['x', 'y']], domain=domain)
    assert p.blocks_with_singletons() == [['a', 'c'], ['b'], ['d'], ['w'], ['x', 'y'], ['z']]
    assert p.singletons == {'b', 'd', 'w', 'z'}
    p.merge_pair('a', 'b')
    assert p == SetPart(blocks=[['a', 'b', 'c'], ['x', 'y']], domain=domain)
    p.merge_many(['w', 'x', 'z'])
    assert p == SetPart(blocks=[['a', 'b', 'c'], ['w', 'x', 'y', 'z']], domain=domain)
    assert p.blocks_with_singletons() == [['a', 'b', 'c'], ['d'], ['w', 'x', 'y', 'z']]


def test_smaller():
    assert SetPart([[2, 4]]) < SetPart([[1, 3], [2, 4]])
    assert SetPart([[2, 4]]) < SetPart([[2, 3, 4]])
    assert SetPart() < SetPart([[2, 4]])
    assert SetPart([[2, 4], [5, 7]]) < SetPart([[2, 3, 4], [5, 6, 7]])
    assert not (SetPart([[1, 2]]) < SetPart())
    assert not (SetPart([[2, 3, 4]]) < SetPart([[2, 4]]))
