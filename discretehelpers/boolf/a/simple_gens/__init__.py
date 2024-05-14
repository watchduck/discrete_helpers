from discretehelpers.a import make_atompattern_gen


def _and(bt):
    return 0 not in bt


def _or(bt):
    return 1 in bt


def _sand(bt, av):
    return sum(bt) == len(av) - 1


def _gand(bt, av):
    return _and(bt) or _sand(bt, av)


# most operators need only the binary_tuple (bt), but some also need the atomvals (av)
operator_to_details = {
    'AND': {
        'default': True,
        'criterion': lambda bt, av: _and(bt)
    },
    'XAND': {
        'default': True,
        'criterion': lambda bt, av: sum(bt) % 2 == len(av) % 2
    },
    'OR': {
        'default': False,
        'criterion': lambda bt, av: _or(bt)
    },
    'XOR': {
        'default': False,
        'criterion': lambda bt, av: sum(bt) % 2
    },
    'EQ': {
        'default': False,
        'criterion': lambda bt, av: not(_or(bt)) or _and(bt)  # union of NOR and AND  (false first row comes from default)
    },
    'SAND': {  # all but one
        'default': False,
        'criterion': lambda bt, av: _sand(bt, av)
    },
    'GAND': {  # SAND extended by AND
        'default': True,
        'criterion': lambda bt, av: _gand(bt, av)
    },
    'ESAND': {  # SAND for odd number, GAND for even number of atomvals
        'default': True,
        'criterion': lambda bt, av: _sand(bt, av) if len(av) % 2 else _gand(bt, av)
    },
    'OSAND': {  # GAND for odd number, SAND for even number of atomvals
        'default': False,
        'criterion': lambda bt, av: _gand(bt, av) if len(av) % 2 else _sand(bt, av)
    },

}


def raw_gen(atomvals, arity, operator_name):
    details = operator_to_details[operator_name]
    default = details['default']
    criterion = details['criterion']
    if not atomvals:
        length = 1 << arity  # 2 ** arity
        for i in range(length):
            yield default
    atom_gens = [make_atompattern_gen(atomval, arity) for atomval in atomvals]
    zipped_atom_gens = zip(*atom_gens)
    for binary_tuple in zipped_atom_gens:
        yield criterion(binary_tuple, atomvals)


########################################################################################################################


def atoms_to_and_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'AND')


def atoms_to_xand_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'XAND')


def atoms_to_or_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'OR')


def atoms_to_xor_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'XOR')


def atoms_to_eq_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'EQ')


def atoms_to_sand_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'SAND')


def atoms_to_gand_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'GAND')


def atoms_to_esand_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'ESAND')


def atoms_to_osand_gen(atomvals, arity):
    return raw_gen(atomvals, arity, 'OSAND')
