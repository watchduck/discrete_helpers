# `Boolf` (Boolean function)

Wikiversity: [Discrete helpers/boolf](https://en.wikiversity.org/wiki/Discrete_helpers/boolf)

```python
from discretehelpers.boolf import Boolf


a = Boolf('0101')
b = Boolf('0011')

assert a == Boolf('01')
assert b == Boolf('01', [1])

assert a & b == Boolf('0001')  # AND
assert a | b == Boolf('0111')  # OR
assert a ^ b == Boolf('0110')  # XOR


assert ~a == Boolf('10')  # NOT
assert ~(a&b) == Boolf('1110')
```

```python
assert Boolf('0000') == Boolf('0')  == Boolf('0', [])   == Boolf(False)
assert Boolf('1111') == Boolf('1')  == Boolf('1', [])   == Boolf(True)
assert Boolf('0101') == Boolf('01') == Boolf('01', [0]) == Boolf(atom=0)
assert Boolf('1010') == Boolf('10') == Boolf('10', [0]) == Boolf(atom=~0)
assert Boolf('0011')                == Boolf('01', [1]) == Boolf(atom=1)
assert Boolf('1100')                == Boolf('10', [1]) == Boolf(atom=~1)

assert Boolf('0001')                == Boolf('0001', [0, 1]) == Boolf(multi_and=[0, 1])
assert Boolf('0111')                == Boolf('0111', [0, 1]) == Boolf(multi_or=[0, 1])

assert Boolf('0101 1010')           == Boolf('0110', [0, 2])
assert Boolf('0101 1111')           == Boolf('0111', [0, 2]) == Boolf(multi_or=[0, 2])
assert Boolf('1111 0101')           == Boolf('1101', [0, 2]) == Boolf(multi_or=[0, ~2])
```

## valency &le; adicity &le; arity
 
Valency is the number of arguments actually used.<br>
Adicity follows from the biggest atom, and corresponds to the required length of the truth table.<br>
(For a [root](metributes/is_root) BF, valency and adicity are equal.)<br>
`Boolf('0001')` (_A and B_) has valency and adicity 2.<br>
`Boolf('0000 0011')` (_B and C_) has valency 2 and adicity 3.<br>
The term _arity_ is only used for arguments of methods, e.g. to calculate the [consul](methods/consul).

```python
boolf = Boolf('0000 0011')
assert boolf == Boolf('0001', [1, 2])
assert boolf.valency, boolf.adicity == (2, 3)
```

## fractions

While BFs of the same arity (see above) are easily expressed as integers,
BFs in general are better thought of as fractions.

```python
from fractions import Fraction
```

Let _v_ be the truth table of a BF, _binary(v)_ its interpretation as a (big-endian) binary number,<br>
and _t_ the truth table of the same length with only 1s.<br>
Then the rational value of the BF is _binary(v) / binary(t)_.

```python
assert a.value_fract() == Fraction(5, 15) == Fraction(1, 3)
assert b.value_fract() == Fraction(3, 15) == Fraction(1, 5)
assert (a & b).value_fract() == Fraction(1, 15)
assert (a | b).value_fract() == Fraction(7, 15)
assert (a ^ b).value_fract() == Fraction(6, 15) == Fraction(2, 5)
```

The weight is the number of 1s in the truth table.

```python
assert a.weight_fract == b.weight_fract == (a ^ b).weight_fract == Fraction(2, 4) == Fraction(1, 2)
assert (a & b).weight_fract == Fraction(1, 4)
assert (a | b).weight_fract == Fraction(3, 4)
```

## examples

There are many example BFs with unique names (which are random 3-syllable words).<br>
Usually they have an illustrated description on Wikiversity, which is linked from
[this list](https://en.wikiversity.org/wiki/Studies_of_Euler_diagrams/list).


```python
from discretehelpers.boolf.examples import medusa, rudege


assert medusa == Boolf('1111 1111 1110 1010')
assert rudege == Boolf('0101 1111 1110 1010')
assert medusa & ~rudege == Boolf('1000 0000', [0, 2, 3])
```