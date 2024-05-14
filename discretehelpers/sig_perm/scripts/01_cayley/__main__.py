import numpy as np
from bidict import bidict
from itertools import product

from discretehelpers.a import rev_colex_perms

from discretehelpers.binv import Binv
from discretehelpers.perm import Perm
from discretehelpers.sig_perm import SigPerm
from discretehelpers.set_part import SetPart

"""
python -m discretehelpers.sig_perm.scripts.01_cayley
"""


# Cayley table of the octahedral group #################################################################################

perms_raw = rev_colex_perms(3)
perms = [Perm(list(_)) for _ in perms_raw]
binvs = [Binv(intval=_) for _ in range(8)]  # binary vectors from 000 to 111 in little-endian order

ids = list(product(range(8), range(6)))  # 3**2 × 3! = 8 × 6

id_to_sigperm = bidict()
for m, n in ids:
    id_to_sigperm[(m, n)] = SigPerm(valneg=binvs[m], perm=perms[n])

domain = list(product(ids, repeat=2))
cayley = SetPart(blocks=[], domain=domain)

for id_a, a in id_to_sigperm.items():
    for id_b, b in id_to_sigperm.items():
        p = a * b
        id_p = id_to_sigperm.inverse[p]
        cayley.add_label_to_element(element=(id_a, id_b), label=id_p)


# Cayley table of the Symmetric group S3 ###############################################################################

domain_s3 = list(product(range(6), repeat=2))
cayley_s3 = SetPart(blocks=[], domain=domain_s3)

for id_a, a in enumerate(perms):
    for id_b, b in enumerate(perms):
        p = a * b
        id_p = perms.index(p)
        cayley_s3.add_label_to_element(element=(id_a, id_b), label=id_p)


# move parts (check that this is indeed simple) ########################################################################

# for double_pair in domain:
#     (am, an), (bm, bn) = double_pair
#     pm, pn = cayley.get_label_from_element(double_pair)
#     if pn != cayley_s3.get_label_from_element((an, bn)):
#         print('Expected not to happen!')

"""
(pm, pn) = (am, an) * (bm, bn)
The move part is indeed predictable:  pn = an * bn
But how to calculate the sign part _pm_?
"""

# sign parts ###########################################################################################################

sign_in_moved_cayley = np.empty([6, 6], dtype=object)

for an, bn in domain_s3:
    sign_cayley = np.zeros([8, 8], dtype=int)
    for am, bm in product(range(8), repeat=2):
        double_pair = ((am, an), (bm, bn))
        pm, pn = cayley.get_label_from_element(double_pair)
        sign_cayley[am, bm] = pm
    sign_in_moved_cayley[an, bn] = sign_cayley

"""
`sign_in_moved_cayley` is a 6×6 matrix (the Cayley table of S3) filled with 8×8 matrices.
Now the question is, which of these 8×8 matrices are equal.
"""

sign_cayley_tuples_to_matrices = dict()

moved_cayley = SetPart(blocks=[], domain=domain_s3)
for an, bn in domain_s3:
    sign_cayley = sign_in_moved_cayley[an, bn]
    sign_cayley_tuples = tuple([tuple(sign_cayley[i, :]) for i in range(8)])
    sign_cayley_tuples_to_matrices[sign_cayley_tuples] = sign_cayley
    moved_cayley.add_label_to_element(element=(an, bn), label=sign_cayley_tuples)

# for block in moved_cayley.blocks:
#     print('##########################', block)
#     sign_cayley_tuples = moved_cayley.get_label_from_block(block)
#     sign_cayley = sign_cayley_tuples_to_matrices[sign_cayley_tuples]
#     print(sign_cayley)

"""
There are 6 different 8×8 matrices, and those in the same row of the 6×6 matrix are equal.
So here is a variation of the code before to create a dict from row number to matrix:
"""

mc_row_to_sc_matrix = dict()
for block in moved_cayley.blocks:
    row_number = block[0][0]
    sign_cayley_tuples = moved_cayley.get_label_from_block(block)
    sign_cayley = sign_cayley_tuples_to_matrices[sign_cayley_tuples]
    mc_row_to_sc_matrix[row_number] = sign_cayley

# for i in range(6):
#     print('##########################', i)
#     print(mc_row_to_sc_matrix[i])

"""
The rows and columns of the 8×8 matrices are permutations of 0 ... 7.
The rows are different in all matrices, but the 8 columns are the same.
"""

# set_of_rows = set()
# set_of_cols = set()
# for matrix in mc_row_to_sc_matrix.values():
#     for i in range(8):
#         set_of_rows.add(tuple(matrix[:, i]))
#         set_of_cols.add(tuple(matrix[i, :]))
#
# print(len(set_of_rows))  # 8
# print(len(set_of_cols))  # 48

"""
The 8 different columns are those of the XOR matrix.
The 48 different rows are the cube vertex permutations forming the octahedral group.

`id_to_sigperm` assigns pairs to SigPerm objects, which have the property `schoute_perm`.
Row _m_ of matrix _n_ is the cvp corresponding to signed permutation _(m, n)_.
"""

# id_to_cvp = dict()
# for id, sigperm in id_to_sigperm.items():
#     id_to_cvp[id] = sigperm.schoute_perm.sequence(8)
#
# for n in range(6):
#     matrix = mc_row_to_sc_matrix[n]
#     for m in range(8):
#         matrix_row = list(matrix[m, :])
#         if matrix_row != id_to_cvp[m, n]:
#             print('Expected not to happen!')

"""
So how to determine _pm_ in _(pm, pn) = (am, an) * (bm, bn)_?

_an_ determines which 8×8 matrix is used.
It is a XOR matrix with permuted rows, so that the top row is _cvp(0, an)_.
(Not permuted by this permutation, but identical to its sequence.)

_am_ is the row index of the 8×8 matrix. The entry in the left column is _am_ itself.
_bm_ is the col index of the 8×8 matrix. The entry in the top row is _cvp(0, an)[bm]_.
The entry in row _am_ and column _bm_ is the bitwise XOR of the left entry in the row and the top entry in the column:
pm = am ^ cvp(0, an)[bm]
"""

# for double_pair in domain:
#     (am, an), (bm, bn) = double_pair
#     pm, pn = cayley.get_label_from_element(double_pair)
#     cvp = id_to_sigperm[(0, an)].schoute_perm.sequence(8)
#     if pm != am ^ cvp[bm]:
#         print('Expected not to happen!')


"""
One can also avoid the XOR and use the cvp of the matrix row:
pm = cvp(am, an)[bm]
"""

# for double_pair in domain:
#     (am, an), (bm, bn) = double_pair
#     pm, pn = cayley.get_label_from_element(double_pair)
#     cvp = id_to_sigperm[(am, an)].schoute_perm.sequence(8)
#     if pm != cvp[bm]:
#         print('Expected not to happen!')
