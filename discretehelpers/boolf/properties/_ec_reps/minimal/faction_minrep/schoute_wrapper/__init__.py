from discretehelpers.a import schoute_coset_gen


def schoute_wrapper(haystack_index, arity, layer_to_false_and_true_places, layer_index, layer_ratio):

    do_complement = layer_ratio < .5  # Most entries are false. Find true entries instead, then complement.

    found_set = set()  # may still have to be complemented

    needles = layer_to_false_and_true_places[layer_index][int(do_complement)]

    for needle in needles:
        for found_index in schoute_coset_gen(needle, haystack_index, arity):
            found_set.add(found_index)

    if do_complement:

        from math import factorial

        cardinality = factorial(arity)
        return set(range(cardinality)).difference(found_set)

    else:

        return found_set
