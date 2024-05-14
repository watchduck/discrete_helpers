from discretehelpers.a import type_like_int


def type_clean_int(arg):

    assert type_like_int(arg)

    return int(arg)
