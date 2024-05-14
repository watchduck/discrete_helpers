from discretehelpers.a import have, true_except, sorted_colex, alphabet_subset
from discretehelpers.ex import ArgMismatchError


def filtrated_pairs_pretty(self, atomnames=None):

    if have(atomnames):
        true_except(len(set(atomnames)) == self.valency, ArgMismatchError)
    else:
        atomnames = alphabet_subset(self.atomvals)

    unpretty = self.filtrated_pairs
    intermediate = dict()

    ###########################################################

    rel_patterns = sorted_colex(set(unpretty.values()))
    for rel_pattern in rel_patterns:
        intermediate[rel_pattern] = []

    for pair_of_atomkeys, rel_pattern in unpretty.items():
        pair_of_atomnames = tuple(
            [atomnames[_] for _ in pair_of_atomkeys]
        )
        intermediate[rel_pattern].append(pair_of_atomnames)

    ###########################################################

    pretty_pre = dict()
    list_of_pairs_with_rel_subset = []

    for rel_pattern, list_of_atomname_pairs in intermediate.items():
        if rel_pattern == '1111':
            pretty_pre['crossing'] = list_of_atomname_pairs
        elif rel_pattern == '1110':
            pretty_pre['disjoint'] = list_of_atomname_pairs
        elif rel_pattern == '0111':
            pretty_pre['universal'] = list_of_atomname_pairs
        elif rel_pattern == '0110':
            pretty_pre['complementary'] = list_of_atomname_pairs
        elif rel_pattern == '1001':
            pretty_pre['equal'] = list_of_atomname_pairs
        elif rel_pattern == '1011':  # subset
            for (a, b) in list_of_atomname_pairs:
                list_of_pairs_with_rel_subset.append((a, b))
        elif rel_pattern == '1101':  # superset
            for (a, b) in list_of_atomname_pairs:
                list_of_pairs_with_rel_subset.append((b, a))
        else:
            pretty_pre[rel_pattern] = list_of_atomname_pairs

    if list_of_pairs_with_rel_subset:
        pretty_pre['subset'] = sorted(list_of_pairs_with_rel_subset)

    ###########################################################

    # This is only cosmetics. The keys should always appear in the same order.
    key_words = ['crossing', 'disjoint', 'universal', 'subset', 'equal', 'complementary']
    pretty = dict()
    for key in key_words:
        if key in pretty_pre.keys():
            pretty[key] = pretty_pre[key]

    for key in pretty_pre.keys():
        if key not in key_words:
            pretty[key] = pretty_pre[key]

    return pretty
