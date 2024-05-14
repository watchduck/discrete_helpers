from discretehelpers.perm import Perm


def test():

    perm = Perm([0, 3, 5, 6, 4, 7, 1, 2])

    assert perm.left_rank == 28848
    assert perm.right_rank == 1888
