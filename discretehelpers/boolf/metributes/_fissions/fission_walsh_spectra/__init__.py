from discretehelpers.a import have
from .work import work


# signed flat ##########################################################################################################

@property
def fission_walsh_spectra(self):
    return self._fission_walsh_spectra


@fission_walsh_spectra.setter
def fission_walsh_spectra(self, val):
    self._fission_walsh_spectra = val


@fission_walsh_spectra.getter
def fission_walsh_spectra(self):
    if have(self._fission_walsh_spectra):
        return self._fission_walsh_spectra

    return work(self)[0]


# abs flat #############################################################################################################

@property
def fission_walsh_spectra_abs(self):
    return self._fission_walsh_spectra_abs


@fission_walsh_spectra_abs.setter
def fission_walsh_spectra_abs(self, val):
    self._fission_walsh_spectra_abs = val


@fission_walsh_spectra_abs.getter
def fission_walsh_spectra_abs(self):
    if have(self._fission_walsh_spectra_abs):
        return self._fission_walsh_spectra_abs

    return work(self)[1]


# signed layered #######################################################################################################

@property
def fission_walsh_spectra_layered(self):
    return self._fission_walsh_spectra_layered


@fission_walsh_spectra_layered.setter
def fission_walsh_spectra_layered(self, val):
    self._fission_walsh_spectra_layered = val


@fission_walsh_spectra_layered.getter
def fission_walsh_spectra_layered(self):
    if have(self._fission_walsh_spectra_layered):
        return self._fission_walsh_spectra_layered

    return work(self)[2]


# abs layered ##########################################################################################################

@property
def fission_walsh_spectra_layered_abs(self):
    return self._fission_walsh_spectra_layered_abs


@fission_walsh_spectra_layered_abs.setter
def fission_walsh_spectra_layered_abs(self, val):
    self._fission_walsh_spectra_layered_abs = val


@fission_walsh_spectra_layered_abs.getter
def fission_walsh_spectra_layered_abs(self):
    if have(self._fission_walsh_spectra_layered_abs):
        return self._fission_walsh_spectra_layered_abs

    return work(self)[3]
