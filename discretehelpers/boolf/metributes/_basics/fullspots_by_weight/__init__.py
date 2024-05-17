from collections import defaultdict

from discretehelpers.a import have


# fullspots by weight (detailed) #######################################################################################
@property
def fullspots_by_weight(self):
    return self._fullspots_by_weight


@fullspots_by_weight.setter
def fullspots_by_weight(self, val):
    self._fullspots_by_weight = val


@fullspots_by_weight.getter
def fullspots_by_weight(self):
    if have(self._fullspots_by_weight):
        return self._fullspots_by_weight

    some_magic(self)
    return self.fullspots_by_weight


# layered fullspots (simple) ###########################################################################################
@property
def layered_fullspots(self):
    return self._layered_fullspots


@layered_fullspots.setter
def layered_fullspots(self, val):
    self._layered_fullspots = val


@layered_fullspots.getter
def layered_fullspots(self):
    if have(self._layered_fullspots):
        return self._layered_fullspots

    some_magic(self)
    return self.layered_fullspots


# weights ##############################################################################################################
@property
def fullspot_weights(self):
    return self._fullspot_weights


@fullspot_weights.setter
def fullspot_weights(self, val):
    self._fullspot_weights = val


@fullspot_weights.getter
def fullspot_weights(self):
    if have(self._fullspot_weights):
        return self._fullspot_weights

    some_magic(self)
    return self.fullspot_weights


# function to create all metributes ####################################################################################
def some_magic(self):
    result_detailed = defaultdict(dict)
    result_simple_raw = defaultdict(list)

    for spotint, atomkeys in self.fullspot_atoms.items():
        weight = len(atomkeys)
        result_detailed[weight][spotint] = atomkeys
        result_simple_raw[weight].append(spotint)

    result_simple = []
    for weight in range(self.valency + 1):
        spotints = result_simple_raw[weight]
        result_simple.append(sorted(spotints))

    result_detailed = dict(result_detailed)
    result_weights = sorted(result_detailed.keys())

    self.fullspots_by_weight = result_detailed
    self.layered_fullspots = result_simple
    self.fullspot_weights = result_weights
