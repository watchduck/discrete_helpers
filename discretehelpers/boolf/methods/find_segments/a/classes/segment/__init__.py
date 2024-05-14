from collections import defaultdict
from discretehelpers.a import balanced_ternary_vector_to_string


class Segment(object):

    def __init__(self, vector, collection):
        self.collection = collection

        self.valency = self.collection.boolf.valency
        assert len(vector) == self.valency
        assert set(vector).issubset({-1, 0, 1})

        self.zero_atomkeys = [key for key, val in enumerate(vector) if val == 0]
        self.sign_atomkeys = [key for key, val in enumerate(vector) if val != 0]
        self.dimension = len(self.zero_atomkeys)
        self.vector = vector

        # find inferiors
        inferior_vectors = defaultdict(list)
        for atomkey in self.zero_atomkeys:
            for sign in [-1, 1]:
                v = self.vector.copy()
                v[atomkey] = sign
                inferior_vectors[atomkey].append(v)
        self.inferior_vectors = dict(inferior_vectors)

        # find all possible neighbors
        neighbor_vectors = dict()
        for atomkey in self.sign_atomkeys:
            v = self.vector.copy()
            v[atomkey] *= -1  # flip sign
            neighbor_vectors[atomkey] = v
        self.neighbor_vectors = dict(neighbor_vectors)

    def run_demands(self):

        # demand inferiors
        for atomkey, two_vectors in self.inferior_vectors.items():
            for v in two_vectors:
                self.collection.demand(v)

        # check neighbors and demand common superiors
        for atomkey, neighbor_v in self.neighbor_vectors.items():
            if self.collection.inquire(neighbor_v):  # if neighbor exists
                superior_v = self.vector.copy()
                superior_v[atomkey] = 0
                self.collection.demand(superior_v)  # demand common superior

    def string(self):
        return balanced_ternary_vector_to_string(self.vector)
