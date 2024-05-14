from itertools import chain, combinations


def powerset(iterable):
    # https://stackoverflow.com/questions/1482308
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
