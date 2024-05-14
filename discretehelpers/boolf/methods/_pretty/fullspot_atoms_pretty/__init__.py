from discretehelpers.a import have, true_except, alphabet_subset
from discretehelpers.ex import ArgMismatchError


def fullspot_atoms_pretty(self, atomnames=None):

    if have(atomnames):
        true_except(len(set(atomnames)) == self.valency, ArgMismatchError)
    else:
        atomnames = alphabet_subset(self.atomvals)

    unpretty = self.fullspot_atoms
    pretty = dict()

    for spotint, list_of_atomkeys in unpretty.items():
        list_of_atomnames = []
        for atomkey in list_of_atomkeys:
            list_of_atomnames.append(atomnames[atomkey])
        pretty[spotint] = list_of_atomnames

    return pretty
