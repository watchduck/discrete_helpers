[documentation](https://en.wikiversity.org/wiki/Studies_of_Euler_diagrams/conversions)


## from _dagoro_ to _darimi_ (BEC with triples)

[`dagoro_darimi_test.py`](dagoro_darimi_test.py) shows also the other direction

```python
from discretehelpers.boolf.examples import dagoro, darimi
from discretehelpers.sig_perm import SigPerm


dagoro_clan = dagoro.ec_clan(5)

block = dagoro_clan.get_block_from_label(darimi)  # [(1, 5, 4)]

m, n, c = block[0]

combos = dagoro_clan.glove_compartment  # [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4)]

signed_variation = SigPerm(pair=(m, n)).apply_on_vector(combos[c])  # [~3,  2,  1,  4]

# dagoro.apply(*signed_variation) == darimi
```