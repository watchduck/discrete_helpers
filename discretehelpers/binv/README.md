# `Binv` (binary vector)

Wikiversity: [Discrete helpers/binv](https://en.wikiversity.org/wiki/Discrete_helpers/binv)

This object has two similar purposes:
* to represent binary vectors and easily get the index numbers of entries 1
* to convert between integers and their representation in little endian binary

```python
from discretehelpers.binv import Binv


binv = Binv('1101000')

assert binv.length == 7
assert binv.weight == 3
assert binv.vector == [True, True, False, True, False, False, False]
assert binv.string == '1101000'
assert binv.exposet == {0, 1, 3}
assert binv.intval == 11  # 2**0 + 2**1 + 2**3
assert binv.changes == 3  # changes between 0 and 1 (down, up, down)
assert ~binv == binv.complement == Binv('0010111')

assert binv == Binv('11 01 000')
assert binv == Binv([1, 1, 0, 1, 0, 0, 0])
assert binv == Binv(intval=11, length=7)
assert binv == Binv(exposet={0, 1, 3}, length=7)
```

The property [`pretty`](properties/pretty.py) can be used when the length is a power of two up to 64.
See [tests](a/to_pretty_string/_test.py).
```python
assert Binv(intval=38505).pretty == '1001 0110 0110 1001'
```