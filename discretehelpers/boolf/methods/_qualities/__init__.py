from discretehelpers.a import int_to_weight


def is_sharp(self, arity):

    return bool(self.tt(arity).weight % 2)


def is_acute(self, arity):

    return self.is_ugly ^ self.is_sharp(arity)


def is_rude(self, arity):

    return self.is_odd ^ self.is_sharp(arity)


def is_rough(self, arity):

    return self.is_odious ^ self.is_sharp(arity)


########################################################################################################################

def is_solid(self, arity):

    i, j = self.hasse_matrix_coordinates(arity)

    coordinate_length = 2 ** (arity - 1)
    shift_length = coordinate_length - 2  # The two highest bits shall remain.

    shifted_i = i >> shift_length
    shifted_j = j >> shift_length
    
    return int_to_weight(shifted_i ^ shifted_j) % 2
