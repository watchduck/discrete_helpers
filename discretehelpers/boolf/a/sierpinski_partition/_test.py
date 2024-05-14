from discretehelpers.boolf.a import atom_partition, sierpinski_partition
from discretehelpers.set_part import SetPart


def test():

    assert atom_partition(0, 3) == sierpinski_partition(1, 3) \
           == SetPart([[0, 1], [2, 3], [4, 5], [6, 7]])
    assert atom_partition(3, 4) == sierpinski_partition(8, 4) \
           == SetPart([[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]])

    assert sierpinski_partition(3, 4) == SetPart([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

    assert sierpinski_partition(7, 4) == SetPart([[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]])

    assert sierpinski_partition(15, 4) == SetPart([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]])
