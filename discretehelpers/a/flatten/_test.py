from discretehelpers.a.flatten import flatten


def test():

    assert flatten((1,)) == (1,)

    assert flatten([[1, 2], [3, 4]]) == (1, 2, 3, 4)

    assert flatten([[1, 2], [3, [4, 5]]]) == (1, 2, 3, 4, 5)
