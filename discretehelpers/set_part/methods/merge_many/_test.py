from discretehelpers.set_part import SetPart


def test():
    a = SetPart()
    a.merge_many([1, 2, 3])
    assert a == SetPart([[1, 2, 3]])
    a.merge_many([3, 4, 5])
    assert a == SetPart([[1, 2, 3, 4, 5]])
    a.merge_many([6, 7, 8])
    assert a == SetPart([[1, 2, 3, 4, 5], [6, 7, 8]])
