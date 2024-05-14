# `Binv` (binary vector)

Wikiversity: [Discrete helpers/binv](https://en.wikiversity.org/wiki/Discrete_helpers/binv)

This object has two similar purposes:
* to represent binary vectors and easily get the index numbers of entries 1
* to convert between integers and their representation in little endian binary

```pycon
>>> from discretehelpers.binv import Binv


>>> binv = Binv('1101000')

>>> binv.length
7
>>> binv.weight
3
>>> binv.vector
[True, True, False, True, False, False, False]
>>> binv.string
'110100'
>>> binv.exposet
{0, 1, 3}
>>> binv.intval  # 2**0 + 2**1 + 2**3
11

>>> binv.changes  # changes between 0 and 1 (down, up, down)
3

>>> binv.complement  # same as `~binv`
Binv('0010111')

>>> a = Binv('11 01 000')
>>> b = Binv([1, 1, 0, 1, 0, 0, 0])
>>> c = Binv(intval=11, length=7)
>>> d = Binv(exposet={0, 1, 3}, length=7)
>>> a == b == c == d == binv
True
```

The property [`pretty`](properties/pretty.py) can be used when the length is a power of two up to 64.
See [tests](a/_to_pretty_string/_test.py).
```pycon
Binv(intval=38505).pretty
'1001 0110 0110 1001'
```