from discretehelpers.a import have


def weight_quadrant(self, arity=None):

    if not have(arity):
        arity = self.adicity

    return self.is_rough(arity) + 2 * self.is_odious


def acute_quadrant(self, arity=None):

    if not have(arity):
        arity = self.adicity

    return self.is_ugly + 2 * self.is_acute(arity)


def octant(self, arity):

    if not have(arity):
        arity = self.adicity

    return self.quadrant + 4 * self.is_acute(arity)
