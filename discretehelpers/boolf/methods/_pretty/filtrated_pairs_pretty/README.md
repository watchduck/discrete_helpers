This method is a wrapper around the property
[`filtrated_pairs`](../../properties/filtrated_pairs).

It orders pairs with the same truth table in a list.

If the argument `atomnames` is used,
the pairs will contain its entries (rather than atomkeys).
It must be a unique list of length `self.valency`.
A typical value for a `Boolf` with valency 4 would be `['A', 'B', 'C', 'D']`.

The example in the test file is *tokosi*.
(See [here](https://en.wikiversity.org/wiki/Studies_of_Euler_diagrams/bloated#tokosi) for its diagram.)
