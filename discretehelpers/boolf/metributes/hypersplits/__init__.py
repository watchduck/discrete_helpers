from functools import cached_property
from itertools import combinations

from discretehelpers.a import true_except
from discretehelpers.set_part import SetPart

from .ex import NotBlightlessError


@cached_property
def hypersplits(self):

    true_except(self.is_blightless, NotBlightlessError)

    result = {1: []}
    for atomkey, split in enumerate(self.splits):
        setpart = SetPart(split)
        result[1].append({
            'atomkeys': [atomkey],
            'setpart': setpart
        })

    n = 2
    while True:
        old_split_dicts = result[n-1]  # coarser
        if len(old_split_dicts) > 1:
            new_split_dicts = []  # finer
            for old_1, old_2 in combinations(old_split_dicts, 2):
                old_1_ak, old_2_ak = set(old_1['atomkeys']), set(old_2['atomkeys'])
                candidate_atomkeys = sorted(old_1_ak.union(old_2_ak))
                old_1_part, old_2_part = old_1['setpart'], old_2['setpart']
                candidate_part = old_1_part.meet(old_2_part)  # new SetPart object
                candidate_blocks = candidate_part.blocks_with_singletons(elements=self.fullspots)
                if len(candidate_atomkeys) == n and len(candidate_blocks) == 2**n:
                    new_split_dict = {
                        'atomkeys': candidate_atomkeys,
                        'setpart': candidate_part
                    }
                    actually_new = True
                    for already_there in new_split_dicts:
                        if already_there == new_split_dict:
                            actually_new = False
                    if actually_new:
                        new_split_dicts.append(new_split_dict)
            if len(new_split_dicts) > 0:
                result[n] = new_split_dicts
                n += 1
            else:  # no new splits found
                break
        else:  # only one old split can not be combined to new splits
            break

    return result
