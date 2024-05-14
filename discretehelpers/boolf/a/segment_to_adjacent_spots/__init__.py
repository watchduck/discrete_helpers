from itertools import product

from discretehelpers.binv import Binv


def segment_to_adjacent_spots(vector):

    ternary_to_binary = {
        -1: 0,
        0: None,
        1: 1
    }

    raw_spot_vector = [ternary_to_binary[_] for _ in vector]

    free_places = [key for key, val in enumerate(vector) if val == 0]
    free_length = len(free_places)
    free_tuples = product([0, 1], repeat=free_length)

    spotints = []
    for free_tuple in free_tuples:
        spot_vector = raw_spot_vector.copy()
        for short_index, long_index in enumerate(free_places):
            spot_vector[long_index] = free_tuple[short_index]
        spotint = Binv(vector=spot_vector).intval
        spotints.append(spotint)

    return sorted(spotints)
