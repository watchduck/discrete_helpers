from discretehelpers.boolf.a import noble_to_royal, noble_to_quadrant, noble_to_index, noble_to_king_index_and_quadrant


def patron_int(self, arity):
    intval = self.tt(arity).intval
    return intval ^ self.zhe


def patron_index(self, arity):
    return noble_to_index(self.patron_int(arity), arity)


def patron_boolf(self, arity):
    return self ^ self.twin(arity)


#####################################################################

def patron_royal(self, arity):
    return noble_to_royal(self.patron_int(arity), arity)


def patron_quadrant(self, arity):
    return noble_to_quadrant(self.patron_int(arity), arity)


#####################################################################

def patron_king_index_and_quadrant(self, arity):
    _patron_int = self.patron_int(arity)
    return noble_to_king_index_and_quadrant(_patron_int, arity)
