from itertools import permutations, product
from discretehelpers.a import int_to_exposet
from discretehelpers.perm.a import left_inversion_count
from factoradic import from_factoradic


def schoute_coset_gen(key_int, val_int, arity):

    pow_arity = 1 << arity  # 2 ** arity
    assert key_int < pow_arity
    assert val_int < pow_arity

    universe = set(range(arity))

    recto_keys = int_to_exposet(key_int)
    verso_keys = sorted(universe.difference(set(recto_keys)))

    recto_vals = int_to_exposet(val_int)
    verso_vals = sorted(universe.difference(set(recto_vals)))

    recto_perms = permutations(recto_vals)
    verso_perms = permutations(verso_vals)

    for recto_perm, reverse_perm in product(recto_perms, verso_perms):
        perm = [0] * arity
        for i, val in enumerate(recto_perm):
            key = recto_keys[i]
            perm[key] = val
        for i, val in enumerate(reverse_perm):
            key = verso_keys[i]
            perm[key] = val
        yield from_factoradic(left_inversion_count(perm))
