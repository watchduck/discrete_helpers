from discretehelpers.boolf.a import atom_indices_to_sequence, sequence_to_entry_counts


def hyperfission_walsh_spectra_labeled(self, dimensions):

    walsh_spectra = self.hyperfission_walsh_spectra(dimensions)

    if len(dimensions) == 0:
        return walsh_spectra[0]

    sequence_length = 2 ** self.adicity
    sequence = atom_indices_to_sequence(dimensions, sequence_length)
    entry_counts = sequence_to_entry_counts(sequence)

    outer_length = len(walsh_spectra)
    inner_length = len(walsh_spectra[0])
    labels = [[None for inner_index in range(inner_length)] for outer_index in range(outer_length)]

    for i in range(sequence_length):
        outer_index = sequence[i]
        inner_index = entry_counts[i]
        labels[outer_index][inner_index] = i

    result = dict()
    for i, walsh_spectrum in enumerate(walsh_spectra):
        label = tuple(labels[i])
        result[label] = list(walsh_spectrum)

    return result
