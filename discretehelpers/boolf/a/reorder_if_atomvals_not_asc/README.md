If the atomvals have to be sorted, the boolean vector has to be sorted accordingly.

The atomvals are sorted together with a list of ascending integers:<br>
`sorted_atomvals, reordered_integers = sort_together(atomvals, asc_integers)`

Let `atomvals` be `[2, 0, 1]` or any vector in the same disorder (like `[5, 1, 3]`).<br>
Then `reordered_integers` is `[1, 2, 0]`. As a permutation that is the inverse of `[2, 0, 1]`.

`fin_perm = Perm(reordered_integers).inverse` is the finite permutation that sorts the atomvals into ascending order.<br>
```
fin_perm == Perm([2, 0, 1])

fin_perm.apply_on_vector([2, 0, 1]) == [0, 1, 2]
fin_perm.apply_on_vector([5, 1, 3]) == [1, 3, 5]

fin_perm.apply_on_vector([1, 2, 4]) == [2, 4, 1]
```
It also permutes a vector of ascending powers of two into the compression vector of the needed bit permutation.<br>
`bit_perm = WalshPerm([2, 4, 1])`

```
bit_perm.apply_on_vector([0, 2, 4, 6, 1, 3, 5, 7]) == [0, 1, 2, 3, 4, 5, 6, 7]
bit_perm.apply_on_vector([0, 1, 0, 0, 1, 0, 1, 1]) == [0, 1, 1, 0, 0, 1, 0, 1]
```

![](_img/example.svg)
