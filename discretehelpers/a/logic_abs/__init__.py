def logic_abs(n):
    if n < 0:
        return ~n
    else:
        return n


def logic_abs_vector(vector):
    return [logic_abs(_) for _ in vector]
