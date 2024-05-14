# `SetPart` (set partition)

Wikiversity: [Discrete helpers/set part](https://en.wikiversity.org/wiki/Discrete_helpers/set_part)

```python
from discretehelpers.set_part import SetPart


sp = SetPart()
sp.merge_pair(3, 5)
sp.merge_many([7, 8, 9])

assert sp == SetPart([[3, 5], [7, 8, 9]])
assert sp.blocks_with_singletons(10) == [[0], [1], [2], [3, 5], [4], [6], [7, 8, 9]]

sp.merge_pair(5, 7)

assert sp == SetPart([[3, 5, 7, 8, 9]])
assert sp.blocks_with_singletons(10) == [[0], [1], [2], [3, 5, 7, 8, 9], [4], [6]]
```

Usually a partition is changed from fine to coarse with 
[`merge_pair`](methods/merge_pair) or [`merge_many`](methods/merge_many),<br>
but the reverse is possible with [`refine_block`](methods/refine_block).

## Cayley tables

`SetPart` can be used to model the Cayley table of a group.<br>
It makes sense to use a set of simple IDs for the elements of the group.<br>
(Typically that should be integers or pairs of integers.)<br>
Then the `domain` argument is the Cartesian square of the set of IDs.<br>
The entries of the Cayley table are IDs added as labels to the blocks.<br>
The method `add_label_to_element` will take care of creating the blocks.

Let `id_to_perm` be a `bidict` from IDs to permutations.

```python
from itertools import product


ids = id_to_perm.keys()
domain = list(product(ids, repeat=2))  # Cartesian product IDs × IDs
cayley = SetPart(blocks=[], domain=domain)  # initialize as finest set partition (only singletons)

for id_a, a in id_to_perm.items():
    for id_b, b in id_to_perm.items():
        p = a * b
        id_ab = id_to_perm.inverse[p]  # key from val in bidict
        cayley.add_label_to_element(element=(id_a, id_b), label=id_p)

cayley.get_label_from_element((i, j))  # get the entry at place (i, j) in the Cayley table
```

An example for the symmetric group S<sub>4</sub> with integer IDs can be found
[here](../perm/scripts/01_cayley).<br>
One for the octahedral group with integer pair IDs can be found
[here](../sig_perm/scripts/02_cayley_compare).
