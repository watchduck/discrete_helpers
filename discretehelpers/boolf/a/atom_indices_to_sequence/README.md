# atom exposet to sequence

Takes a list of positive integers, which are exposet of atomic Boolean functions.<br>
Stacks their truth tables as rows of a long matrix, and converts its columns to integers.

The optional second argument is `target_length`, which will repeat the sequence accordingly.

```python
atom_indices_to_sequence([2]) == (0, 0, 0, 0,  1, 1, 1, 1)

atom_indices_to_sequence([0, 1, 2]) == (0, 1, 2, 3,  4, 5, 6, 7)

atom_indices_to_sequence([0, 3]) == (0, 1, 0, 1,  0, 1, 0, 1,  2, 3, 2, 3,  2, 3, 2, 3)
atom_indices_to_sequence([1, 3]) == (0, 0, 1, 1,  0, 0, 1, 1,  2, 2, 3, 3,  2, 2, 3, 3)
```

----

One could also use the similar function [`walsh_indices_to_sequence`](../../../seal/a/walsh_indices_to_sequence):

```python
walsh_exposet = [2 ** _ for _ in atom_exposet]
atom_indices_to_sequence(atom_exposet) == walsh_indices_to_sequence(walsh_exposet)
```
