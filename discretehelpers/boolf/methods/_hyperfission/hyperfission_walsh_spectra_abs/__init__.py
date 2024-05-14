def hyperfission_walsh_spectra_abs(self, dimensions):

    result = []

    for _before in self.hyperfission_walsh_spectra(dimensions):
        _after = tuple([abs(_) for _ in _before])
        result.append(_after)

    return result
