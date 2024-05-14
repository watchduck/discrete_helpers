# `Perm` (permutation)

Wikiversity: [Discrete helpers/perm](https://en.wikiversity.org/wiki/Discrete_helpers/perm)


```pycon
>>> from discretehelpers.perm import Perm
```

## finite permutation

```pycon
>>> cycles = [[0, 3, 2, 1], [4, 6]]
>>> sequence = [3, 0, 1, 2, 6, 5, 4]

>>> p = Perm(cycles)
>>> ps = Perm(sequence)
>>> p == ps
True

>>> p.length
7

>>> p.cycles == cycles
True
>>> p.sequence() == p.sequence(7) == sequence
True
>>> p.sequence(10) == sequence + [7, 8, 9]
True

>>> p.moved  # number of moved elements
{0, 1, 2, 3, 4, 6}
>>> p.mapping
{0: 3, 3: 2, 2: 1, 1: 0, 4: 6, 6: 4}

>>> p.order
4
>>> p**2
Perm([[0, 2], [1, 3]])
>>> p**3
Perm([[0, 1, 2, 3], [4, 6]])
>>> p**4
Perm()

>>> p.inverse == p**-1 == p**3
True
```

Composition is from the left, i.e. `a * b` means `a` after `b`.<br>
The method `apply_on_vector` can be used to permute any list.<br>
See examples in the [tests](test), especially [here](test/02_concat/b_wiki_examples).

## periodic permutation

Most attributes are those of the smallest corresponding finite permutation.<br>
The new attribute `perilen` is the period length.

```pycon
cycles = [[3, 4]]
>>> p5 = Perm(cycles, 5)
>>> p10 = Perm(cycles, 10)
```
The results are `Perm([[3, 4]], perilen=5)` and `Perm([[3, 4]], perilen=10)`.<br>
`perilen` is 5 and 10 respectively.<br>
For both permutations `order` is 2, `cycles` is `[[3, 4]]` and `mapping` is `{3: 4, 4: 3}`.

The length of a sequence must be a multiple of the period length.<br>
These are the results of `p5.sequence(20)` and `p10.sequence(20)`:<br>
[0, 1, 2, **4**, **3**, 5, 6, 7, **9**, **8**, 10, 11, 12, **14**, **13**, 15, 16, 17, **19**, **18**]<br>
[0, 1, 2, **4**, **3**, 5, 6, 7, 8, 9, 10, 11, 12, **14**, **13**, 15, 16, 17, 18, 19]

Analogous to `sequence`, the method `cycles_dynamic` gives the cycles for multiples of the period length:

```pycon
>>> p5.cycles_dynamic(20)
[[3, 4], [8, 9], [13, 14], [18, 19]]
>>> p10.cycles_dynamic(20)
[[3, 4], [13, 14]]
```
