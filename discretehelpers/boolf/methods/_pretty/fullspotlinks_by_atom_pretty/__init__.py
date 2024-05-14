from discretehelpers.a import have, true_except, alphabet_subset
from discretehelpers.ex import ArgMismatchError


def fullspotlinks_by_atom_pretty(self, atomnames=None, print_only=False):

    """
    `print_only` will just print the result in a readable way, without returning it.
    """

    if have(atomnames):
        true_except(len(set(atomnames)) == self.valency, ArgMismatchError)
    else:
        atomnames = alphabet_subset(self.atomvals)

    unpretty = self.fullspotlinks_by_atom
    pretty = dict()

    for atomkey, list_of_pairs in unpretty.items():
        atomname = atomnames[atomkey]
        pretty[atomname] = list_of_pairs

    if print_only:
        for dimension, list_of_pairs in pretty.items():
            print('##################################', dimension)
            print(list_of_pairs)
    else:
        return pretty
