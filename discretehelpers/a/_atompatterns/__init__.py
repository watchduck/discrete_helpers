def make_atompattern_gen(signed_atomval, arity, negate=False):
    negated_with_tilda = signed_atomval < 0
    abs_atomval = ~signed_atomval if negated_with_tilda else signed_atomval
    assert abs_atomval < arity
    length = 1 << arity  # 2 ** arity
    half_period_length = 1 << abs_atomval  # 2 ** atomval
    period_length = half_period_length << 1  # half_period_length * 2
    if negate ^ negated_with_tilda:
        for i in range(length):
            yield i % period_length < half_period_length
    else:
        for i in range(length):
            yield i % period_length >= half_period_length


def make_atompattern(*args, **kwargs):
    from discretehelpers.binv import Binv
    return Binv(list(make_atompattern_gen(*args, **kwargs)))


def make_atompatterns(arg):
    if type(arg) == int:
        arity = arg
        assert arity > 0
        atoms = list(range(arity))
    elif type(arg) in [list, tuple]:
        atoms = arg
        arity = len(atoms)
    else:
        raise TypeError

    return [make_atompattern(atom, arity) for atom in atoms]


def atompattern_to_signed_index(binv):
    from discretehelpers.binv import Binv
    from discretehelpers.boolf import Boolf
    if type(binv) != Binv:
        binv = Binv(list(binv))
    boolf = Boolf(binv)
    negate = boolf.tt()[0]
    atomvals = boolf.atomvals
    assert len(atomvals) == 1
    atomval = atomvals[0]
    return atomval, negate
