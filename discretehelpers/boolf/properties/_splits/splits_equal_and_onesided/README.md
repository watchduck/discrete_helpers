`splits_equal` and `splits_onesided` are created in the same process.

Both refer to `splits`, which is a list of length `valency`.

`splits_equal` is a dictionary assigning a truth value to each pair of splits,
telling if the splits (not necessarily the sets) are equal.
If the valency is 3, these pairs are `(0, 1)`, `(0, 2)` and `(1, 2)`.

`splits_onesided` is a list of length `valency` of truth values.
If one split has an empty and a full side, the respective entry is `True`.