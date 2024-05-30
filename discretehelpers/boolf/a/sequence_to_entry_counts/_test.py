from discretehelpers.boolf.a import sequence_to_entry_counts


def test():

    assert sequence_to_entry_counts([0, 1, 2, 0, 1, 2, 0, 1, 2]) == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    assert sequence_to_entry_counts(['a', 'b', 'a', 'c', 'a', 'a']) == [0, 0, 1, 0, 2, 3]
