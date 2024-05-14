from discretehelpers.a import vector_zip_apart
from discretehelpers.boolf.a import atom_indices_to_sequence


def hyperfission(self, dimensions):

    if len(dimensions) == 0:
        return [self.tt()]
    elif len(dimensions) == 1:
        return self.fissions[dimensions[0]]

    sequence = atom_indices_to_sequence(dimensions, 2 ** self.adicity)

    return vector_zip_apart(self.tt(), sequence)
