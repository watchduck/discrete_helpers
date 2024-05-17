# consul &nbsp; (binary Walsh spectrum)

The product of the truth table and a Walsh matrix (of positive and negative 1s) is the [_Walsh spectrum_](../walsh_spectrum).<br>
One can use a binary Walsh matrix instead, and the is always a Walsh function.<br>
It may be called _binary Walsh spectrum_, and the corresponding integer shall be called **consul**.<br>
(Where it is convenient, the term may also be used for the Walsh function itself.)

The consul is the integer part of the [twin](../twin) [prefect](../../metributes/prefect).<br>
(This requires, that consul and twin are calculated with the same arity.)

One could also define a sign for the consul (like for the prefect),<br>
by multiplying with a _negated_ binary Walsh matrix.<br>
But the sign would just be the weight oddness.

----

`consul` is a fast function. It takes for granted, that the binary Walsh spectrum is indeed a Walsh function.<br>
It takes an optional argument, which determines the [truth table](../tt). (Typically the arity. May also be a list of atomvals.)

`consul_weight` also takes an optional argument to determine the truth table. (Typically the arity.)

----

`consul_slow` is used only to test its fast equivalent.<br>
It takes nothing for granted. It performs the matrix multiplication, and checks if the result is a Walsh function.<br>
It takes the second optional argument `prefab_matrix`, which can be used to provide the binary Walsh matrix.

----

Families of truth tables with odd weight have every possible consul.<br>
Families of truth tables with even weight have a unique.
Clans of truth tables with even weight have a unique consul weight.
