from functools import cached_property

from discretehelpers.binv import Binv


@cached_property
def hypersplits_detailed(self):

    result = dict()

    for n, old_list_of_split_dicts in self.hypersplits.items():
        new_list_of_split_dicts = []

        for old_split_dict in old_list_of_split_dicts:
            atomkeys = old_split_dict['atomkeys']

            # express set partition as dict of blocks with binary labels
            labeled_blocks = dict()
            for block_index in range(2**n):
                block_binv = Binv(intval=block_index, length=n)
                block_str = block_binv.string
                block_set = self.fullspots.copy()
                for place in range(n):
                    atomkey = atomkeys[place]
                    index_to_split_side = int(not(block_binv[place]))  # 0: inside (set), 1: outside (complement)
                    atomkey_split_side = self.splits[atomkey][index_to_split_side]
                    block_set = block_set.intersection(atomkey_split_side)
                labeled_blocks[block_str] = sorted(block_set)

            new_split_dict = {'atomkeys': atomkeys, 'setpart': labeled_blocks}

            new_list_of_split_dicts.append(new_split_dict)

        result[n] = new_list_of_split_dicts

    return result
