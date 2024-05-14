# attributes, properties and methods

## attributes

* `neutral`: super attribute
* `perilen`: super attribute
* `matrix_minimal`
* `vector_object`
* `transpose_vector_object`
* `degree`

## properties

* `mapping`: super attribute, [adapted](properties/mapping)
* `order`: super property, inherited
* `cycles`: super property, inherited
* `inverse`: super property, [adapted](properties/inverse)
* `moved`: super **attribute**, [adapted](properties/moved)
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

In practice the verification happens in the property [mapping](properties/mapping).<br>
To cause the verification, the property is called (without further effect) in the [`__init__`](__init__.py) method,<br>
unless `WalshPerm` is initialized with `trust=True`. 

