from discretehelpers.set_part import SetPart


def test():
    assert SetPart([[1, 2], [0, 3]]).intval == 12
    assert SetPart([[1, 2, 3]]).intval == 52
    assert SetPart([[0, 3], [1, 2, 4]]).intval == 396
