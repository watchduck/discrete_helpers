from functools import cached_property

from discretehelpers.a import other_entry_in_pair


@cached_property
def atom_to_crossing_atoms(self):

    result = dict()

    crossing_pairs = set()
    for pair, filtrate_string in self.filtrated_pairs.items():
        if filtrate_string == '1111':
            crossing_pairs.add(pair)

    for atomkey in range(self.valency):
        crossing_atomkeys = []
        for pair in crossing_pairs:
            if atomkey in pair:
                crossing_atomkeys.append(other_entry_in_pair(pair, atomkey))
        result[atomkey] = sorted(crossing_atomkeys)

    return result
