from sympy import primefactors


def reduce_period(mapping, perilen):

    primes = primefactors(perilen)

    found = False
    for prime in primes:
        if block_repeats(mapping, perilen, prime):
            found = True
            break

    if found:
        perilen = perilen // prime
        mapping = dict((k, mapping[k]) for k in mapping.keys() if k < perilen)
        return reduce_period(mapping, perilen)
    else:
        return mapping, perilen


def block_repeats(mapping, perilen, prime, testing=False):

    blocklen = perilen // prime
    moved = sorted(mapping.keys())
    movlen = len(moved)

    # If the number of moved elements is not even divisible by the prime, there can be no repeating pattern.
    if not movlen % prime == 0:
        return False if not testing else 'no1'

    # A repeating pattern in the permutation requires a repeating pattern in the moved elements.
    movblocklen = movlen // prime
    for key in range(movblocklen):
        for i in range(1, prime):
            if moved[i * movblocklen + key] != i * blocklen + moved[key]:
                return False if not testing else 'no2'

    # actual check for repeating patterns
    for key in [k for k in mapping.keys() if k < blocklen]:
        for i in range(1, prime):
            length = i * blocklen
            if mapping[length + key] != length + mapping[key]:
                return False if not testing else 'no3'

    return True if not testing else 'yes'
