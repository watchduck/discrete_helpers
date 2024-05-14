from numbers import Number


def type_like_int(arg):

    if not isinstance(arg, Number):
        return False

    return arg % 1 == 0
