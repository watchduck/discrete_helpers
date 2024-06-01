from discretehelpers.a import have, sort_together

from discretehelpers.set_part import SetPart


# equality blocks
@property
def splits_equality_blocks(self):
    return self._splits_equality_blocks


@splits_equality_blocks.setter
def splits_equality_blocks(self, val):
    self._splits_equality_blocks = val


@splits_equality_blocks.getter
def splits_equality_blocks(self):
    if have(self._splits_equality_blocks):
        return self._splits_equality_blocks

    some_magic(self)
    return self.splits_equality_blocks


# preferred side
@property
def splits_preferred_side(self):
    return self._splits_preferred_side


@splits_preferred_side.setter
def splits_preferred_side(self, val):
    self._splits_preferred_side = val


@splits_preferred_side.getter
def splits_preferred_side(self):
    if have(self._splits_preferred_side):
        return self._splits_preferred_side

    some_magic(self)
    return self.splits_preferred_side


# function to create both metributes
def some_magic(self):

    if self.is_constant:
        self.splits_equality_blocks = []
        self.splits_preferred_side = []
        return  # break

    equality_partition = SetPart()
    for (a, b), are_equal in self.splits_equal.items():
        if are_equal:
            equality_partition.merge_pair(a, b)
    equality_blocks = equality_partition.blocks_with_singletons(self.valency)

    ##########################################

    preferred_sides = []

    for block in equality_blocks:

        if len(block) == 1:  # set does not even have a duplicate, therefore no complement

            preferred_sides.append(None)

        else:  # set has duplicates, complements might be among them

            recto_atomkey = block[0]
            verso_atomkey = self.bloat.get_comp(recto_atomkey)  # if there is a complement, None otherwise

            if not have(verso_atomkey):  # no complement among duplicate sets - thus no need to choose

                preferred_sides.append(None)

            else:  # complement among duplicate sets - need to choose preferred side

                split = self.splits[recto_atomkey]
                recto_fullspots, verso_fullspots = split

                if set() in split:  # split is onesided
                    # prefer universe over empty side
                    prefer_recto_condition = verso_fullspots == set()
                else:  # split has fullspots on both sides
                    # prefer side with smallest spotint (essentially random choice)
                    prefer_recto_condition = min(recto_fullspots) < min(verso_fullspots)

                preferred_atomkey = recto_atomkey if prefer_recto_condition else verso_atomkey
                preferred_sides.append(preferred_atomkey)

    ##########################################

    representative_atomkeys = []  # of each equality block
    for i in range(len(equality_blocks)):
        preferred_side = preferred_sides[i]
        if have(preferred_side):
            atomkey = preferred_side
        else:
            atomkey = equality_blocks[i][0]
        representative_atomkeys.append(atomkey)

    _, equality_blocks = sort_together(representative_atomkeys, equality_blocks)
    _, preferred_sides = sort_together(representative_atomkeys, preferred_sides)

    self.splits_equality_blocks = equality_blocks
    self.splits_preferred_side = preferred_sides
