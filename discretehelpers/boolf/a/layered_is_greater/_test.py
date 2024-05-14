from discretehelpers.boolf.a import layered_is_greater


def test():

    assert layered_is_greater(
        [[2, 0], [0, 2]],  # [2, 2]   4
        [[0, 1], [0, 3]]   # [1, 3]   4
    )

    assert layered_is_greater(
        [[0, 2], [0, 1]],  # [2, 1]   3
        [[0, 1], [0, 2]]   # [1, 2]   3
    )

    assert not layered_is_greater(
        [[0, 2], [0, 1]],  # [2, 1]   3
        [[0, 1], [0, 3]]   # [1, 3]   4
    )

    assert not layered_is_greater(
        [[1], [1]],  # [1, 2]   2
        [[0], [3]]   # [0, 3]   3
    )

    assert layered_is_greater(
        [[1, 0], [0, 2]],  # [1, 2]   3
        [[0, 1], [1, 1]]   # [1, 2]   3
    )

    assert not layered_is_greater(
        [[1, 0], [0, 2]],  # [1, 2]   3
        [[0, 1], [1, 2]]   # [1, 3]   4
    )
