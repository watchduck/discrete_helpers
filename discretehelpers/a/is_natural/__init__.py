def is_natural(candidate):
    try:
        behaves_like_integer = candidate % 1 == 0
    except TypeError:
        return False
    return behaves_like_integer and candidate >= 0
