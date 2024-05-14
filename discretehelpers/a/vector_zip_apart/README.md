# vector zip apart

Arguments:
* `vector:` vector to be separated
* `pattern`: separation pattern, e.g. `[]`

`result[k]` is a list of those `vector[i]` where `pattern[i] == k`.

``` 
vector:  [10, 11, 12, 13, 14, 15]
pattern: [ 0,  1,  0,  1,  0,  2]

         0             1         2
result: [[10, 12, 14], [11, 13], [15]]
```

```python
from discretehelpers.a import vector_zip_apart


vector_zip_apart([10, 11, 12, 13, 14, 15], [ 0,  1,  0,  1,  0,  2])
# [[10, 12, 14], [11, 13], [15]]
```

Works also with `Binv` objects:

```python
from discretehelpers.binv import Binv


vector_zip_apart(Binv('0110 0101'), Binv('0000 1111'))
# [Binv('0110'), Binv('0101')]
```

Inverse of [`vector_zip_together`](../vector_zip_together).