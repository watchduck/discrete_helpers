from itertools import permutations


def rev_colex_perms(n):

    result = []

    for p in permutations(range(n)):
        result = [tuple(p[::-1])] + result

    return result
