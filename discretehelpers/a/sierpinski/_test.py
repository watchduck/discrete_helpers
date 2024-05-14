import numpy as np

from discretehelpers.a import sierpinski


def test():

    a = sierpinski('tr', 1)
    b = sierpinski('tr', degree=1)
    c = sierpinski('tr', size=2)
    assert np.array_equal(a, b)
    assert np.array_equal(b, c)
    assert np.array_equal(c, np.array([
        [1, 1],
        [0, 1]
    ]))

    assert np.array_equal(
        sierpinski('tl', size=4),
        np.array([
            [1, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0]
        ])
    )

    assert np.array_equal(
        sierpinski('br', 3),
        np.array([
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ])
    )
