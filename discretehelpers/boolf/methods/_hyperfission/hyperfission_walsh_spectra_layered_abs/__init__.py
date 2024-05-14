from discretehelpers.boolf.a import flat_to_layered


def hyperfission_walsh_spectra_layered_abs(self, dimensions):

    result = []

    for _before in self.hyperfission_walsh_spectra_abs(dimensions):
        _after = flat_to_layered(_before)
        result.append(_after)

    return result
