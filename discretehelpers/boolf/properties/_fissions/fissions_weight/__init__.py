from discretehelpers.a import have
from .work import work


# pair of vectors
@property
def fissions_weight(self):
    return self._fissions_weight


@fissions_weight.setter
def fissions_weight(self, val):
    self._fissions_weight = val


@fissions_weight.getter
def fissions_weight(self):
    if have(self._fissions_weight):
        return self._fissions_weight

    return work(self)[0]


# pair of integers
@property
def fissions_weight_layered(self):
    return self._fissions_weight_layered


@fissions_weight_layered.setter
def fissions_weight_layered(self, val):
    self._fissions_weight_layered = val


@fissions_weight_layered.getter
def fissions_weight_layered(self):
    if have(self._fissions_weight_layered):
        return self._fissions_weight_layered

    return work(self)[1]
