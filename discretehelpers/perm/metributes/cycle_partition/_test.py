from discretehelpers.perm import Perm
from discretehelpers.set_part import SetPart


def test():

    assert Perm([[0, 2, 1]]).cycle_partition == Perm([[0, 1, 2]]).cycle_partition == SetPart([[0, 1, 2]])

    assert Perm([[3, 5, 9], [2, 7, 4]]).cycle_partition == Perm([[2, 4, 7], [3, 9, 5]]).cycle_partition == SetPart([[2, 4, 7], [3, 5, 9]])
