from itertools import product

from discretehelpers.a import rev_colex_perms

from discretehelpers.set_part import SetPart
from discretehelpers.perm import Perm

"""
python -m discretehelpers.perm.scripts.01_cayley
"""

perms_raw = rev_colex_perms(4)
perms = [Perm(list(_)) for _ in perms_raw]

domain = list(product(range(24), repeat=2))  # all 24**2 = 576 pairs (a, b) with a, b in 0 ... 23

cayley = SetPart(blocks=[], domain=domain)

for index_a in range(24):
    perm_a = perms[index_a]
    for index_b in range(24):
        perm_b = perms[index_b]
        perm_ab = perm_a * perm_b
        index_ab = perms.index(perm_ab)
        cayley.add_label_to_element(element=(index_a, index_b), label=index_ab)


print(
    cayley.get_label_from_element((5, 12)),  # 13
    cayley.get_label_from_element((12, 5))   # 17
)

print(
    cayley.get_block_from_label(13)
)

print(
    cayley.get_block_from_label(17)
)


row_12 = [cayley.get_label_from_element((12, _)) for _ in range(24)]
print(row_12)


# for block in cayley.blocks:
#     label = cayley.get_label_from_block(block)
#     print(str(label) + ': ' + str(block))
