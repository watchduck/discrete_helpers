import numpy as np
from bidict import bidict
from itertools import product

from discretehelpers.a import rev_colex_perms

from discretehelpers.binv import Binv
from discretehelpers.perm import Perm
from discretehelpers.sig_perm import SigPerm
from discretehelpers.set_part import SetPart

"""
python -m discretehelpers.sig_perm.scripts.02_cayley_compare
"""

# prepare ##############################################################################################################

perms_raw = rev_colex_perms(3)
perms = [Perm(list(_)) for _ in perms_raw]
binvs = [Binv(intval=_) for _ in range(8)]  # binary vectors from 000 to 111 in little-endian order

ids = list(product(range(8), range(6)))  # 3**2 × 3! = 8 × 6
domain = list(product(ids, repeat=2))

id_to_sigperm = bidict()
id_to_matrix = bidict()
id_to_cvp = bidict()

for m, n in ids:
    sigperm = SigPerm(valneg=binvs[m], perm=perms[n])
    id_to_sigperm[(m, n)] = sigperm
    id_to_matrix[(m, n)] = tuple([tuple(row) for row in sigperm.matrix(3)])
    id_to_cvp[(m, n)] = sigperm.schoute_perm


# Cayley table from signed permutations (SigPerm) ######################################################################

cayley_sigperm = SetPart(blocks=[], domain=domain)

for id_a, a in id_to_sigperm.items():
    for id_b, b in id_to_sigperm.items():
        p = a * b
        id_p = id_to_sigperm.inverse[p]
        cayley_sigperm.add_label_to_element(element=(id_a, id_b), label=id_p)


# Cayley table from 3×3 signed permutation matrices ####################################################################

cayley_matrix = SetPart(blocks=[], domain=domain)

for id_a, tuple_a in id_to_matrix.items():
    a = np.array(tuple_a)
    for id_b, tuple_b in id_to_matrix.items():
        b = np.array(tuple_b)
        p = np.dot(a, b)
        tuple_p = tuple([tuple(row) for row in p])
        id_p = id_to_matrix.inverse[tuple_p]
        cayley_matrix.add_label_to_element(element=(id_a, id_b), label=id_p)


# Cayley table from cube vertex permutations (Perm) ####################################################################

cayley_cvp = SetPart(blocks=[], domain=domain)

for id_a, a in id_to_cvp.items():
    for id_b, b in id_to_cvp.items():
        p = a * b
        id_p = id_to_cvp.inverse[p]
        cayley_cvp.add_label_to_element(element=(id_a, id_b), label=id_p)


# compare ##############################################################################################################

print(cayley_sigperm == cayley_matrix == cayley_cvp)
print(cayley_sigperm.block_labels == cayley_matrix.block_labels == cayley_cvp.block_labels)