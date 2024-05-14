from discretehelpers.a import have
from discretehelpers.boolf.a import vector_to_twin_gen


def twin(self, arity=None):

    from discretehelpers.boolf import Boolf

    if not have(arity):
        arity = self.adicity
    else:
        assert arity >= self.adicity

    tt = self.tt(arity)

    twin_tt_gen = vector_to_twin_gen(tt, arity)

    return Boolf(list(twin_tt_gen))
