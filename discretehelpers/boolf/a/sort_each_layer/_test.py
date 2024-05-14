from discretehelpers.boolf.a import sort_each_layer


def test():

    a = ((3, 2, 1), (2, 4, 2))
    b = ((1, 2, 3), (2, 2, 4))
    assert sort_each_layer(a) == b
