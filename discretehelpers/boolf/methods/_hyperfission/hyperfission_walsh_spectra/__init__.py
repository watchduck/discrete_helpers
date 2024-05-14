from sympy import fwht  # fast Walsh-Hadamard transform (Walsh spectrum)


def hyperfission_walsh_spectra(self, dimensions):

    result = []

    for binv in self.hyperfission(dimensions):
        vector = [int(_) for _ in binv]
        walsh_spectrum = tuple(fwht(vector))
        result.append(walsh_spectrum)

    return result
