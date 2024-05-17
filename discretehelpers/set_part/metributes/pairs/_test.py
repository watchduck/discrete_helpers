from discretehelpers.set_part import SetPart


def test():
    a = SetPart([[1, 3, 5], [7, 9]])
    assert a.pairs == {(7, 9), (1, 3), (3, 5), (1, 5)}

    b = SetPart([[1, 3], [5, 7, 9]])
    assert b.pairs == {(7, 9), (5, 9), (1, 3), (5, 7)}

    c = a.join(b)
    assert c == SetPart([[1, 3, 5, 7, 9]])
    assert c.pairs == {(1, 5), (3, 7), (5, 7), (7, 9), (1, 7), (3, 9), (5, 9), (1, 3), (1, 9), (3, 5)}
    assert c.blocks_with_singletons() == [[0], [1, 3, 5, 7, 9], [2], [4], [6], [8]]
    assert c.blocks_with_singletons(elements={1, 3, 5, 7, 9, 99}) == [[1, 3, 5, 7, 9], [99]]

    d = a.meet(b)
    assert d == SetPart([[1, 3], [7, 9]])
    assert d.pairs == {(7, 9), (1, 3)}
    assert d.blocks_with_singletons()   == [[0], [1, 3], [2], [4], [5], [6], [7, 9], [8]]
    assert d.blocks_with_singletons(12) == [[0], [1, 3], [2], [4], [5], [6], [7, 9], [8], [10], [11]]
    assert d.blocks_with_singletons(elements={1, 3, 5, 7, 9}) == [[1, 3], [5], [7, 9]]
    assert d.blocks_with_singletons(elements={1, 3, 5, 7, 9, 99}) == [[1, 3], [5], [7, 9], [99]]
