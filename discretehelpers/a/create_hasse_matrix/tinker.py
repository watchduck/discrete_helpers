from itertools import product
from math import factorial

from discretehelpers.sig_perm import SigPerm
from discretehelpers.perm import Perm
from discretehelpers.a import create_hasse_matrix


dimension = 4

number_of_rows = 2 ** dimension
number_of_columns = factorial(dimension)


nodes = sorted(product(range(number_of_rows), range(number_of_columns)))

node_to_inversion_set = dict()

for node in nodes:
    sp = SigPerm(pair=node)
    schoute_sequence = sp.schoute_perm.sequence(number_of_rows)
    p = Perm(schoute_sequence)
    node_to_inversion_set[node] = p.inversion_set


def is_under(pair_1, pair_2):
    inversion_set_1 = node_to_inversion_set[pair_1]
    inversion_set_2 = node_to_inversion_set[pair_2]
    return inversion_set_1.issubset(inversion_set_2)


def pair_str(pair):
    a, b = pair
    return f"{a}-{b}"


hasse = create_hasse_matrix(nodes, is_under)

edges = []

for i, row in enumerate(hasse):
    for j, entry in enumerate(row):
        if entry:
            a, b = pair_str(nodes[i]), pair_str(nodes[j])
            edges.append((a, b))

print('number of nodes:', len(nodes))
print([pair_str(_) for _ in nodes])

print('number of edges:', len(edges))
print(edges)

# for node, inversion_set in node_to_inversion_set.items():
#     print(node, inversion_set)