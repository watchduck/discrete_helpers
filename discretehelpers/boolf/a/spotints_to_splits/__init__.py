from discretehelpers.a import make_atompattern

from discretehelpers.binv import Binv


def spotints_to_splits(spotints, valency):

    binv = Binv(exposet=spotints, length=2**valency)

    splits = []
    for atomkey in range(valency):
        recto_binv = binv & make_atompattern(atomkey, valency)
        verso_binv = binv & make_atompattern(~atomkey, valency)
        splits.append((
            set(recto_binv.exposet),
            set(verso_binv.exposet)
        ))

    return splits
