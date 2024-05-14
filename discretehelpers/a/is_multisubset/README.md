# functions

## is multisubset

A multiset in this context is a dict from elements (usually integers) to counts (natural numbers).<br>
Count 0 means, that the element could just as well not be in the dict.

`a` is multisubset of `b`, iff for every count in `a`, the respective count in `b` is greater or equal.


## multiset to distri

The helper function `multiset_to_distri` is also here. See the example below.

# example

Together with
[`find_integer_partitions`](../find_integer_partitions)
these functions were used to verify the results of
[`next_integer_partition`](../../boolf/a/next_integer_partition).

```python
from discretehelpers.a import find_integer_partitions, inventory_dict, is_multisubset, multiset_to_distri


inventory = {5: 3, 2: 4, 1: 7}
target = 15
values = [5, 2, 1]

ip_tuples = find_integer_partitions(target)
for ip_tuple in ip_tuples:
    ip_dict = inventory_dict(ip_tuple)
    if is_multisubset(ip_dict, inventory):
        print(multiset_to_distri(ip_dict, values))
```

E.g. the code above creates these eight triples:

```
[2, 1, 3]
[3, 0, 0]
[0, 4, 7]
[2, 2, 1]
[1, 3, 4]
[2, 0, 5]
[1, 2, 6]
[1, 4, 2]
```
