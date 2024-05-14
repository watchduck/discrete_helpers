from collections import defaultdict
from discretehelpers.boolf.a import segment_to_adjacent_spots
from ... import Segment


class CollectionOfSegments(object):

    def __init__(self, boolf):
        self.boolf = boolf
        self.valency = self.boolf.valency
        self.segments = defaultdict(dict)
        self.number_by_dimension = [0] * (self.valency + 1)

        for binary_exposet in self.boolf.fullspot_atoms.values():
            ternary_vector = [-1] * self.valency  # binary 0 corresponds to balanced ternary -1
            for i in binary_exposet:
                ternary_vector[i] = 1  # binary 1 corresponds to balanced ternary 1
            self.add(ternary_vector)

    def inquire(self, vector):
        dimension = vector.count(0)
        if dimension in self.segments.keys():
            return tuple(vector) in self.segments[dimension].keys()
        else:
            return False

    def demand(self, vector):
        if not self.inquire(vector):
            self.add(vector)

    def add(self, vector):
        assert not self.inquire(vector)
        segment = Segment(vector=vector, collection=self)
        self.segments[segment.dimension][tuple(vector)] = segment
        self.number_by_dimension[segment.dimension] += 1
        segment.run_demands()

    def get_spots(self):
        spot_ints = set()
        for vector in self.segments[0].keys():
            spotint = 0
            for key, val in enumerate(vector):
                if val == 1:
                    spotint += 2**key
            spot_ints.add(spotint)
        return spot_ints

    def get_links(self):  # neighboring spots
        pairs_of_spots = defaultdict(set)
        for vector, segment in self.segments[1].items():
            atomkey = segment.zero_atomkeys[0]
            pair = segment_to_adjacent_spots(vector)
            pair = tuple(pair)
            pairs_of_spots[atomkey].add(pair)
        return dict(pairs_of_spots)

    def get_neighboring_links(self):
        from math import log
        pairs_of_links = defaultdict(set)
        for crossing_vector, crossing_segment in self.segments[2].items():
            for changing_atomkey, two_link_vectors in crossing_segment.inferior_vectors.items():
                ((a, b), (c, d)) = tuple([tuple(segment_to_adjacent_spots(_)) for _ in two_link_vectors])
                belonging_atomkey = int(log(a ^ b, 2))
                assert belonging_atomkey == int(log(c ^ d, 2))
                pairs_of_links[belonging_atomkey].add(((a, b), (c, d)))
        return dict(pairs_of_links)

    def print_segments(self, atomnames=None):
        from discretehelpers.a import sorted_colex, balanced_ternary_vector_to_string
        from discretehelpers.a import have, true_except, alphabet_subset
        from discretehelpers.ex import ArgMismatchError
        if have(atomnames):
            true_except(len(set(atomnames)) == self.valency, ArgMismatchError)
        else:
            atomnames = alphabet_subset(self.boolf.atomvals)
        for dimension, dict_of_segments in self.segments.items():
            print('##########################', dimension)
            pattern_to_vectors = defaultdict(list)
            for vector in dict_of_segments.keys():
                pattern = tuple([key for key, val in enumerate(vector) if val == 0])
                pattern_to_vectors[pattern].append(vector)
            patterns = sorted_colex(pattern_to_vectors.keys())
            for pattern in patterns:
                pattern_with_atomnames = [atomnames[_] for _ in pattern]
                pattern_with_atomnames = ','.join(pattern_with_atomnames)
                list_of_vectors = sorted_colex(pattern_to_vectors[pattern])
                vector_strings_to_adjacent_spots = dict()
                for vector in list_of_vectors:
                    vector_string = balanced_ternary_vector_to_string(vector)
                    adjacent_spots = segment_to_adjacent_spots(vector)
                    vector_strings_to_adjacent_spots[vector_string] = adjacent_spots
                print(pattern_with_atomnames, '  ', vector_strings_to_adjacent_spots)



