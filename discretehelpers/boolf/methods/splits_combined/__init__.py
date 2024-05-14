from discretehelpers.set_part import SetPart


def splits_combined(self, atomkeys):

    if len(atomkeys) == 0:
        return []  # dummy

    combined_part = SetPart(self.splits[atomkeys[0]])

    if len(atomkeys) > 1:
        for atomkey in atomkeys[1::]:
            atom_part = SetPart(self.splits[atomkey])
            combined_part = combined_part.meet(atom_part)

    return combined_part.blocks_with_singletons(elements=self.fullspots)
