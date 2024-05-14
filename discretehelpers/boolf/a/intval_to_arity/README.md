# natural number to arity (or truth table length)

Truth tables with integer values 4 ... 15 require length 2<sup>2</sup> = 4, and thus have arity 2.<br>
Those with integer values 16 ... 255 require length 2<sup>3</sup> = 8, and thus have arity 3.

`intval_to_arity(x)` returns the smallest _n_, so that _x_ can be represented as a binary number of length 2<sup>_n_</sup>.<br>
`intval_to_tt_length(x)` returns 2<sup>_n_</sup>.

E.g. 260 requires `log_floor(260) + 1` = 9 binary digits.<br>
So the shortest possible truth table has length `2 ** log_ceil(9)` = 16.<br>
`Binv(intval=260, length=16)` = `Binv('0010 0000 1000 0000')`

This function uses [`log_floor`](../../../a/log_floor).
