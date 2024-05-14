from discretehelpers.a import have, true_except, alphabet_subset
from discretehelpers.ex import ArgMismatchError


def bundles_pretty(self, atomnames=None):

    if have(atomnames):
        true_except(len(set(atomnames)) == self.valency, ArgMismatchError)
    else:
        atomnames = alphabet_subset(self.atomvals)

    return [[atomnames[atomkey] for atomkey in bundle] for bundle in self.bundles]
