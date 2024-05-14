from discretehelpers.a import is_natural


def repeat_sequence(short_sequence, target_length):

    assert type(short_sequence) in [list, tuple]
    assert is_natural(target_length)

    short_length = len(short_sequence)

    assert target_length % short_length == 0

    repeat = target_length // short_length

    result = list(short_sequence) * repeat

    if type(short_sequence) == tuple:
        return tuple(result)
    else:
        return result
