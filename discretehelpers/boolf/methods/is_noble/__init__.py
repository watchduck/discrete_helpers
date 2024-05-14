from discretehelpers.a import have


def is_noble(self, arity=None):

    if not have(arity):
        arity = self.adicity

    return self == self.twin(arity)
