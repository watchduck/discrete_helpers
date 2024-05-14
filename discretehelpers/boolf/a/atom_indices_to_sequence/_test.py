from discretehelpers.boolf.a import atom_indices_to_sequence


def test():

    assert atom_indices_to_sequence([2]) == (0, 0, 0, 0,  1, 1, 1, 1)

    assert atom_indices_to_sequence([0, 1, 2])     == (0, 1, 2, 3,  4, 5, 6, 7)
    assert atom_indices_to_sequence([0, 1, 2], 16) == (0, 1, 2, 3,  4, 5, 6, 7,  0, 1, 2, 3,  4, 5, 6, 7)

    assert atom_indices_to_sequence([0, 3]) == (0, 1, 0, 1,  0, 1, 0, 1,  2, 3, 2, 3,  2, 3, 2, 3)
    assert atom_indices_to_sequence([1, 3]) == (0, 0, 1, 1,  0, 0, 1, 1,  2, 2, 3, 3,  2, 2, 3, 3)
