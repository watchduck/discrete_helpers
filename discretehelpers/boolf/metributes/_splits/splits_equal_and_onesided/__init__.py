from discretehelpers.a import have


# splits_equal
@property
def splits_equal(self):
    return self._splits_equal


@splits_equal.setter
def splits_equal(self, val):
    self._splits_equal = val


@splits_equal.getter
def splits_equal(self):
    if have(self._splits_equal):
        return self._splits_equal

    some_magic(self)
    return self.splits_equal


# splits_onesided
@property
def splits_onesided(self):
    return self._splits_onesided


@splits_onesided.setter
def splits_onesided(self, val):
    self._splits_onesided = val


@splits_onesided.getter
def splits_onesided(self):
    if have(self._splits_onesided):
        return self._splits_onesided

    some_magic(self)
    return self.splits_onesided


# function to create both metribute
def some_magic(self):

    if self.valency == 0:
        self.splits_equal = {}
        self.splits_onesided = []

    elif self.valency == 1:
        self.splits_equal = {}
        self.splits_onesided = [True]

    else:
        equal_dict = dict()
        onesided_list = [False] * self.valency
        for (index1, index2), count in self.splits_overlap_counts.items():
            are_equal = False
            if count == 1:
                # Both splits are onesided, and thus equal.
                are_equal = True
                onesided_list[index1] = onesided_list[index2] = True
            elif count == 2:
                # both sides of both splits
                pos1, neg1 = self.splits[index1]
                pos2, neg2 = self.splits[index2]
                # A split is onesided, if only one side in non-empty.
                # There are two possible cases:
                # - Both splits are not onesided. In that case they are equal.
                # - Only one of them is onesided. Then they are not equal.
                uni1 = sum([bool(pos1), bool(neg1)]) == 1
                uni2 = sum([bool(pos2), bool(neg2)]) == 1
                onesided_list[index1] = uni1
                onesided_list[index2] = uni2
                are_equal = not uni1 and not uni2
            equal_dict[(index1, index2)] = are_equal
        self.splits_equal = equal_dict
        self.splits_onesided = onesided_list
