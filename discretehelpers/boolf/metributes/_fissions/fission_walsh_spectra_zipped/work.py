from discretehelpers.a import make_atompatterns, vector_zip_together


def work(self):

    atompatterns = make_atompatterns(self.adicity)

    result_signed = []
    result_abs = []

    for i in range(self.adicity):
        atompattern = atompatterns[i]
        a, b = self.fission_walsh_spectra[i]

        zipped_walsh_spectra = vector_zip_together([a, b], atompattern)
        result_signed.append(zipped_walsh_spectra)

        zipped_walsh_spectra_abs = [abs(_) for _ in zipped_walsh_spectra]
        result_abs.append(zipped_walsh_spectra_abs)

    result_signed = [tuple(_) for _ in result_signed]
    result_abs = [tuple(_) for _ in result_abs]

    return result_signed, result_abs
