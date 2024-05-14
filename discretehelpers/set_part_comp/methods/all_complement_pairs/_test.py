from ... import SetPartComp


def test():
    a = SetPartComp([[0, 1], [2, 3]], {(0, 3)})
    assert a.all_complement_pairs() == {(0, 2), (0, 3), (1, 2), (1, 3)}

    b = SetPartComp([[0, 2], [1, 3]], {(0, 3)})
    assert b.all_complement_pairs() == {(0, 1), (0, 3), (1, 2), (2, 3)}
