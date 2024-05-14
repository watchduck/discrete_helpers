from itertools import permutations, product
from discretehelpers.a import int_to_exposet
from discretehelpers.perm.a import left_inversion_count
from factoradic import from_factoradic


def schoute_coset_gen(key_int, val_int, arity):

    pow_arity = 1 << arity  # 2 ** arity
    assert key_int < pow_arity
    assert val_int < pow_arity

    universe = set(range(arity))

    obverse_keys = int_to_exposet(key_int)
    reverse_keys = sorted(universe.difference(set(obverse_keys)))

    obverse_vals = int_to_exposet(val_int)
    reverse_vals = sorted(universe.difference(set(obverse_vals)))

    obverse_perms = permutations(obverse_vals)
    reverse_perms = permutations(reverse_vals)

    for obverse_perm, reverse_perm in product(obverse_perms, reverse_perms):
        perm = [0] * arity
        for i, val in enumerate(obverse_perm):
            key = obverse_keys[i]
            perm[key] = val
        for i, val in enumerate(reverse_perm):
            key = reverse_keys[i]
            perm[key] = val
        yield from_factoradic(left_inversion_count(perm))
