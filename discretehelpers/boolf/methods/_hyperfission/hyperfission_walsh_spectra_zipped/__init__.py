from discretehelpers.a import vector_zip_together
from discretehelpers.boolf.a import atom_indices_to_sequence


def hyperfission_walsh_spectra_zipped(self, dimensions):

    walsh_spectra = self.hyperfission_walsh_spectra(dimensions)

    if len(dimensions) == 0:
        return walsh_spectra[0]

    sequence = atom_indices_to_sequence(dimensions, 2 ** self.adicity)

    return vector_zip_together(walsh_spectra, sequence)
