import numpy as np

from itertools import combinations

from discretehelpers.binv import Binv


def diagonal_adjacency_matrix(self, minus_places):

    tt = self.root
    valency = self.valency
    vertices = sorted(self.fullspots)
    size = len(vertices)

    matrix = np.zeros([size, size], dtype=int)
    for a, b in combinations(range(2 ** valency), 2):
        if tt[a] and tt[b]:
            i = Binv(intval=a ^ b).weight - 1
            a_index = vertices.index(a)
            b_index = vertices.index(b)
            entry = -1 if minus_places[i] else 1
            matrix[a_index, b_index] = matrix[b_index, a_index] = entry

    return matrix
