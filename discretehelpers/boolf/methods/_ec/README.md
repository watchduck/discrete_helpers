# equivalence classes

The equivalence classes are [`SetPart`](../../../set_part) objects with block labels.<br>
The blocks of the families consist of integers denoting negator patterns.<br>
Those of the clans consist of pairs of integers denoting signed permutations ([`SigPerm`](../../../sig_perm)).

So with `clan = boolf.ec_clan()`, the relevant information is hidden in `clan.block_labels`.

This allows to use some handy methods of `SetPart`.

## signed permutations

The transform under which the functions in a clan are equivalent is a signed permutation.
(This is often called an NP transform, for _negation_ and _permutation_.)
A [`SigPerm`](../../../sig_perm) can be denoted by a pair (_m_, _n_), where _m_ denotes the negator pattern and _n_ the permutation.

All pairs whose transform produces the same function form a block of the `SetPart`.<br>
In `block_labels` the `Boolf` is assigned as its label.

If _arity_ is greater _valency_ (because the argument is provided, or because the function is spread)
there are ignored inputs. That makes the SigPerms of size _arity_ inefficient, because _k_ ignored places will produce 2<sup>_k_</sup> &middot; _k_! duplicates.
Therefore, the default for this case is to use triples (_m_, _n_, _c_),
where (_m_, _n_) denotes a SigPerm of size _valency_,
while _c_ is the key to a list of atomval tuples, which can be found in `clan.glove_compartment`. 

The [tests for _vinona_](../../test/02_val_apply_ec/vinona/vinona_ec_test.py) (_A_ OR _B_) show the 2-ary case, 
and the 3-ary case with pairs and triples.

## conversions

The following code shows how to find the 16 signed permutations that turn _potula_ into _basori_.

```python
from discretehelpers.boolf.examples import potula, basori


potula_clan = potula.ec_clan(5)
potula_clan.get_block_from_label(basori, suppress_abbreviation=True)
# [(0, 60), (0, 84), (2, 60), (2, 84), (4, 60), (4, 84), (6, 60), (6, 84), (8, 65), (8, 89), (10, 65), (10, 89), (12, 65), (12, 89), (14, 65), (14, 89)]
```

The two starting with 0 require no negators, i.e. only permutation of arguments.

```python
from itertools import permutations
from discretehelpers.a import rev_colex_perms

perms5 = rev_colex_perms(5)
p60 = perms5[60]  # (0, 3, 4, 1, 2)
p84 = perms5[84]  # (0, 3, 4, 2, 1)

# potula.atomvals == [0, 1, 2]
# [p60[_] for _ in potula.atomvals] == [p84[_] for _ in potula.atomvals] == [0, 3, 4]

# potula.apply_sigperm(p60) == potula.apply_sigperm(p84) == potula.apply(0, 3, 4) == basori
```

Back from _basori_ to _potula_:

```python
basori_clan = basori.ec_clan(5, suppress_abbreviation=True)
basori_clan.get_block_from_label(potula)
# [(0, 60), (0, 62), (2, 114), (2, 116), (8, 60), (8, 62), (10, 114), (10, 116), (16, 60), (16, 62), (18, 114), (18, 116), (24, 60), (24, 62), (26, 114), (26, 116)]

p62 = perms5[62]  # (0, 4, 3, 1, 2)

# basori.atomvals == [0, 3, 4]
# [p60[_] for _ in basori.atomvals] == [p62[_] for _ in basori.atomvals] == [0, 1, 2]

# basori.apply_sigperm(p60) == basori.apply_sigperm(p62) == basori.apply(0, 1, 2) == potula
```


