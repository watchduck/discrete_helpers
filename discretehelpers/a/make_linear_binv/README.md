row of a binary Walsh matrix as [Binv](../../binv)

arguments:
* `walsh_index`
* `arity` (length is 2<sup>arity</sup>)
* `negate` (default `False`)
* optional: `prefab_atom_patterns`

```python
make_linear_binv(0, 4, False) == Binv('0000 0000 0000 0000')
make_linear_binv(0, 4, True)  == Binv('1111 1111 1111 1111')

make_linear_binv(7, 4, False) == Binv('0110 1001 0110 1001')
make_linear_binv(7, 4, True)  == Binv('1001 0110 1001 0110')

make_linear_binv(12, 4, False) == Binv('0000 1111 1111 0000')
make_linear_binv(12, 4, True)  == Binv('1111 0000 0000 1111')
```

<a href="https://commons.wikimedia.org/wiki/File:Multigrade_operator_XOR.svg" width="300px">
    <img src="../../_img/Multigrade_operator_XOR.svg">
</a>

The other direction is [`walsh_function_to_index`](../walsh_function_to_index).

This functions returns a `Binv` object (with the specified length).<br>
[`make_linear_boolf`](../make_linear_boolf) returns a `Boolf` object.