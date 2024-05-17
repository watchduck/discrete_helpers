from functools import cached_property

from itertools import product


@cached_property
def hypersplits_potential_cores(self):

    assert self.is_blightless

    result = dict()

    for dimension, hs_dicts in self.hypersplits.items():
        pc_dicts = []
        
        for hs_dict in hs_dicts:
            fixed_atomkeys = hs_dict['atomkeys']  # e.g. [0, 3]
            free_atomkeys = sorted(set(range(self.valency)).difference(set(fixed_atomkeys)))  # e.g. [1, 2]
            determined_atomkeys = dict()
            fixed_free_pairs = product(fixed_atomkeys, free_atomkeys)
            for fixed, free in fixed_free_pairs:
                filtrate = self.filtrated_pair(fixed, free)
                if filtrate == '1111':  # border `fixed` crosses border `free`
                    pass  # nothing to do
                elif filtrate in ['0111', '1011']:  # universal or subset, i.e. border `fixed` is in area `free`
                    if free in free_atomkeys:
                        free_atomkeys.remove(free)
                    assert (free not in determined_atomkeys.keys()) or (determined_atomkeys[free] == 1)
                    determined_atomkeys[free] = 1
                elif filtrate in ['1101', '1110']:  # superset or disjoint, i.e. border `fixed` is outside area `free`
                    if free in free_atomkeys:
                        free_atomkeys.remove(free)
                    assert (free not in determined_atomkeys.keys()) or (determined_atomkeys[free] == -1)
                    determined_atomkeys[free] = -1
                else:
                    raise RuntimeError  # The function is blightless, so this should not happen.

            # create all vectors
            vectors = []
            raw_vector = [0] * self.valency
            for atomkey, sign_val in determined_atomkeys.items():
                raw_vector[atomkey] = sign_val  # -1 or 1
            free_size = len(free_atomkeys)
            free_tuples = list(product([-1, 1], repeat=free_size))
            for free_tuple in free_tuples:
                vector = raw_vector.copy()
                for i, ternary_val in enumerate(free_tuple):
                    atomkey = free_atomkeys[i]
                    vector[atomkey] = ternary_val
                vectors.append(vector)


            pc_dicts.append({
                'fixed': fixed_atomkeys,
                'free': free_atomkeys,
                'determined': determined_atomkeys,
                'vectors': vectors
            })

        result[dimension] = pc_dicts

    return result
