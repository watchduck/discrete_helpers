from discretehelpers.a import have


def leader(self, arity=None):

    if not have(arity):
        arity = self.adicity

    q = self.quadrant

    if q == 0:
        return self
    elif q == 1:
        return self.twin(arity).complement.twin(arity)  # partner (change least significant bit)
    elif q == 2:
        return self.complement.twin(arity).complement.twin(arity)  # partner of the complement
    elif q == 3:
        return self.complement