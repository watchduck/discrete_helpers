The filtrates (with names like _sed..._) are spread. The others are dense.<br>
To avoid long calculations, the BECs of the filtrates are calculated with the dense equivalent.

The signed variations to get the actual filtrate are then calculated with the help of the filtrate's 
[`spread_vector`](../../../properties/spread_vector):

```python
from discretehelpers.boolf.examples import gepofu, sedofu


sedofu_dense = sedofu.dense_boolf

sigperm = [2, 0, 1, 3]
# gepofu.apply(*sigperm) == sedofu_dense

spread = sedofu.spread_vector  # [1, 1, 2, 2]

sigvar = [sigperm[i] + spread[sigperm[i]] for i in range(4)]  # [4, 1, 2, 5]
# gepofu.apply(*sigvar) == sedofu
```

The signed permutations and variations in these examples happen to be all unsigned.

_Miniri_ and _sediri_ have valency 5, so the whole calculation is not feasible as a test.
There is [this script](../../../scripts/10_conversions/miniri_sediri.py) instead.<br>
[`miniri_sediri_test.py`](miniri_sediri_test.py) shows only examples taken from that calculation.
