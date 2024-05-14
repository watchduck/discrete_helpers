# pretty signs

This functions takes any container with nested integers, and adds a space before any natural number.<br>
It also replaces `True` and `False` by `●` and `○`.<br>
This can improve the readability of printed rows in the console.


```python
from discretehelpers.a import pretty_signs


bar = [
    [(1, 2), (-3, 4), (5, True)],
    [(1, -2), (-3, 4), (5, False)],
    [(-1, 2), (3, -4), (-5, False)],
    [(1, 2), (3, -4), (-5, True)]
]

for foo in bar:
    print(pretty_signs(foo))
```

The code above produces this output:

```
[( 1,  2), (-3,  4), ( 5, ●)]
[( 1, -2), (-3,  4), ( 5, ○)]
[(-1,  2), ( 3, -4), (-5, ○)]
[( 1,  2), ( 3, -4), (-5, ●)]
```