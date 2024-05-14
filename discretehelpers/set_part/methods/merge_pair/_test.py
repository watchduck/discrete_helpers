from discretehelpers.set_part import SetPart


def test():
    a = SetPart()
    a.merge_pair(10, 20)
    a.merge_pair(20, 30)
    a.merge_pair(40, 50)
    assert a == SetPart([[10, 20, 30], [40, 50]])
