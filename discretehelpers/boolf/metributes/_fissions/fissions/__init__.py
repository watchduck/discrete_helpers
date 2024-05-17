from discretehelpers.a import have
from .work import work


# main property
@property
def fissions(self):
    return self._fissions


@fissions.setter
def fissions(self, val):
    self._fissions = val


@fissions.getter
def fissions(self):
    if have(self._fissions):
        return self._fissions

    return work(self)[0]


# derived property
@property
def fissions_layered(self):
    return self._fissions_layered


@fissions_layered.setter
def fissions_layered(self, val):
    self._fissions_layered = val


@fissions_layered.getter
def fissions_layered(self):
    if have(self._fissions_layered):
        return self._fissions_layered

    return work(self)[1]
