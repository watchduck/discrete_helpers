from ... import SetPartComp


def test():
    equal_list = [0, 3, 4, 7, 8, 11, 12, 15]  # The two least-significant binary digits are equal.
    diff_list = [1, 2, 5, 6, 9, 10, 13, 14]  # The two least-significant binary digits are different.

    equal_spc = SetPartComp([[0, 1]])
    diff_spc = SetPartComp([], {(0, 1)})

    for n in equal_list:
        assert equal_spc.int_matches(n)
        assert not diff_spc.int_matches(n)

    for n in diff_list:
        assert diff_spc.int_matches(n)
        assert not equal_spc.int_matches(n)
