from discretehelpers.a import repeat_sequence, abbrev_testing as abbrev


def test():

    assert repeat_sequence(['a', 'b'], 6) == ['a', 'b', 'a', 'b', 'a', 'b']
    assert repeat_sequence([9, 99, 999], 6) == [9, 99, 999, 9, 99, 999]

    abbrev(AssertionError, [
        lambda: repeat_sequence([9, 99, 999], 5)
    ])
