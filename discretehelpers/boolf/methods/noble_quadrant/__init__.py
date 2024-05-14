from discretehelpers.a import have, true_except


def noble_quadrant(self, arity=None):

    if not have(arity):
        arity = self.adicity

    true_except(self.is_noble(arity), ValueError)

    tt = self.tt(arity)
    is_strong = tt[1]

    return int(is_strong) + int(self.is_odious) * 2
