from discretehelpers.a import is_natural, have, repeat_sequence


def atom_indices_to_sequence(exposet, target_length=None):
    from discretehelpers.boolf import Boolf

    assert type(exposet) in [list, tuple]
    assert len(set(exposet)) == len(exposet)

    arity = max(exposet) + 1
    length = 2 ** arity
    result = [0] * length

    for i, atom_index in enumerate(exposet):
        assert is_natural(atom_index)
        boolf = Boolf(atom=atom_index)
        place_value = 2 ** i
        for j in range(length):
            if boolf[j]:
                result[j] += place_value

    if have(target_length):
        result = repeat_sequence(result, target_length)

    return tuple(result)
