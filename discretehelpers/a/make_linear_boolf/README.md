row of a binary Walsh matrix as [Binv](../../binv)

arguments:
* `walsh_index`
* `negate` (default `False`)


```python
make_linear_boolf(0, False) == Boolf('0')
make_linear_boolf(0, True)  == Boolf('1')

make_linear_boolf(7, False) == Boolf('0110 1001')
make_linear_boolf(7, True)  == Boolf('1001 0110')

make_linear_boolf(12, False) == Boolf('0110', [2, 3]) == Boolf('0000 1111 1111 0000')
make_linear_boolf(12, True)  == Boolf('1001', [2, 3]) == Boolf('1111 0000 0000 1111')
```

<a href="https://commons.wikimedia.org/wiki/File:Multigrade_operator_XOR.svg" width="300px">
    <img src="../../_img/Multigrade_operator_XOR.svg">
</a>

The other direction is [`walsh_function_to_index`](../walsh_function_to_index).

This functions returns a `Boolf` object.<br>
[`make_linear_binv`](../make_linear_binv) returns a specific truth table, i.e. a `Binv` object.