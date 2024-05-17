# attributes, metributes and methods

## attributes

* `neutral`: super attribute
* `perilen`: super attribute
* `matrix_minimal`
* `vector_object`
* `transpose_vector_object`
* `degree`

## metributes

* `mapping`: super attribute, [adapted](metributes/mapping)
* `order`: super metribute, inherited
* `cycles`: super metribute, inherited
* `inverse`: super metribute, [adapted](metributes/inverse)
* `moved`: super **attribute**, [adapted](metributes/moved)
* `determinant`


## methods

* `sequence`: super method, slightly [adapted](__init__.py) (added parameter `degree`)
* `cycles_dynamic`: super method, slightly [adapted](__init__.py) (added parameter `degree`)
* `apply_on_vector`: super method inherited
* `matrix`
* `vector`

## orphans

attribute `length` (use `perilen` instead)


# misc.

## verification

Theoretically one could use the binary matrix to check if the Walsh permutation is valid.<br>
It is, if the real determinant modulo 2 is 1.<br>
But calculating a determinant does not always give and integer, where it should.

In practice the verification happens in the metribute [mapping](metributes/mapping).<br>
To cause the verification, the metribute is called (without further effect) in the [`__init__`](__init__.py) method,<br>
unless `WalshPerm` is initialized with `trust=True`. 
