from discretehelpers.a import make_atompattern

from discretehelpers.binv import Binv


def spotints_to_splits(spotints, valency):

    binv = Binv(exposet=spotints, length=2**valency)

    splits = []
    for atomkey in range(valency):
        pos_binv = binv & make_atompattern(atomkey, valency)
        neg_binv = binv & make_atompattern(~atomkey, valency)
        splits.append((
            set(pos_binv.exposet),
            set(neg_binv.exposet)
        ))

    return splits
