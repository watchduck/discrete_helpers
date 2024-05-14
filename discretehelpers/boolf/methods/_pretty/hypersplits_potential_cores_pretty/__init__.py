from discretehelpers.a import have, true_except, alphabet_subset, balanced_ternary_vector_to_string
from discretehelpers.ex import ArgMismatchError


def hypersplits_potential_cores_pretty(self, atomnames=None, print_only=False):

    """
    `print_only` will just print the result in a readable way, without returning it.
    """

    if have(atomnames):
        true_except(len(set(atomnames)) == self.valency, ArgMismatchError)
    else:
        atomnames = alphabet_subset(self.atomvals)

    result = dict()
    
    for dimension, old_pc_dicts in self.hypersplits_potential_cores.items():
        new_list_of_dicts = []
        for old_pc_dict in old_pc_dicts:
            old_fixed, old_free, old_determined, old_vectors = old_pc_dict['fixed'], old_pc_dict['free'], old_pc_dict['determined'], old_pc_dict['vectors']
            new_fixed = ''.join([atomnames[atomkey] for atomkey in old_fixed])
            new_free = ''.join([atomnames[atomkey] for atomkey in old_free])
            new_determined = []
            for atomkey, int_val in old_determined.items():
                atomname = atomnames[atomkey]
                str_val = {-1: '−', 1: '+'}[int_val]
                new_determined.append(atomname + str_val)
            new_determined = ' '.join(new_determined)
            new_vectors = [balanced_ternary_vector_to_string(_) for _ in old_vectors]
            new_list_of_dicts.append({
                'fixed': new_fixed,
                'free': new_free,
                'determined': new_determined,
                'vectors': new_vectors
            })
        result[dimension] = new_list_of_dicts

    if print_only:
        for dimension, list_of_dicts in result.items():
            print('##################################', dimension)
            for pc_dict in list_of_dicts:
                print(pc_dict)
    else:
        return result
