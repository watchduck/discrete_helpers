def is_multisubset(a, b):

    for element, count_a in a.items():
        if count_a > 0:
            try:
                count_b = b[element]
                if count_b < count_a:
                    return False
            except KeyError:
                return False
    return True


def multiset_to_distri(multiset, values):
    result = [0] * len(values)
    assert set(multiset.keys()).issubset(set(values))
    for i, value in enumerate(values):
        try:
            result[i] = multiset[value]
        except KeyError:
            pass
    return result