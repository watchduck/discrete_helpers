from discretehelpers.a import have, true_except, alphabet_subset
from discretehelpers.ex import ArgMismatchError


def hypersplits_pretty(self, atomnames=None, print_only=False):

    """
    `print_only` will just print the result in a readable way, without returning it.
    """

    if have(atomnames):
        true_except(len(set(atomnames)) == self.valency, ArgMismatchError)
    else:
        atomnames = alphabet_subset(self.atomvals)

    result = dict()

    for dimension, old_list_of_dicts in self.hypersplits_detailed.items():
        new_list_of_dicts = []
        for old_hs_dict in old_list_of_dicts:
            old_molecule = old_hs_dict['atomkeys']
            new_molecule = [atomnames[atomkey] for atomkey in old_molecule]
            old_setpart = old_hs_dict['setpart']
            new_setpart = dict()
            for old_block_label, block_list in old_setpart.items():
                new_block_label = []
                for binary_place, binary_digit in enumerate(old_block_label):
                    parenthesis = '+' if binary_digit == '1' else '−'
                    atomname = new_molecule[binary_place]
                    new_block_label.append(parenthesis + atomname)
                new_block_label = ' '.join(new_block_label)
                new_setpart[new_block_label] = block_list
            new_list_of_dicts.append(new_setpart)
        result[dimension] = new_list_of_dicts

    if print_only:
        for dimension, list_of_dicts in result.items():
            print('##################################', dimension)
            for hs_dict in list_of_dicts:
                print(hs_dict)
    else:
        return result
