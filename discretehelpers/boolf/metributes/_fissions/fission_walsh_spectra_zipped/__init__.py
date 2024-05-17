from discretehelpers.a import have
from .work import work


# main property
@property
def fission_walsh_spectra_zipped(self):
    return self._fission_walsh_spectra_zipped


@fission_walsh_spectra_zipped.setter
def fission_walsh_spectra_zipped(self, val):
    self._fission_walsh_spectra_zipped = val


@fission_walsh_spectra_zipped.getter
def fission_walsh_spectra_zipped(self):
    if have(self._fission_walsh_spectra_zipped):
        return self._fission_walsh_spectra_zipped

    return work(self)[0]


# derived property
@property
def fission_walsh_spectra_abs_zipped(self):
    return self._fission_walsh_spectra_abs_zipped


@fission_walsh_spectra_abs_zipped.setter
def fission_walsh_spectra_abs_zipped(self, val):
    self._fission_walsh_spectra_abs_zipped = val


@fission_walsh_spectra_abs_zipped.getter
def fission_walsh_spectra_abs_zipped(self):
    if have(self._fission_walsh_spectra_abs_zipped):
        return self._fission_walsh_spectra_abs_zipped

    return work(self)[1]
