from discretehelpers.a import true_except
from discretehelpers.ex import ArgTooBigError, ArgValueError


def index_to_noble(i, arity):

    if arity == 0:
        true_except(i == 0, ArgTooBigError)
        return 0

    junarity = arity - 1
    row_length = 1 << (1 << junarity)  # 2 ** 2 ** junarity
    true_except(i < row_length, ArgTooBigError)

    from discretehelpers.boolf.a import twin_int

    i_twin = twin_int(i, junarity)

    return (i_twin ^ i) + (row_length * i)


def noble_to_index(noble, arity, trust=False):

    if arity == 0:
        true_except(noble == 0, ArgTooBigError)
        return 0

    max_noble = (1 << (1 << arity)) - 2  # 2 ** (2 ** arity) - 2
    true_except(noble <= max_noble, ArgTooBigError)

    if not trust:
        from discretehelpers.boolf import Boolf
        boolf = Boolf(noble, arity=arity)
        true_except(boolf.is_noble(arity), ArgValueError)

    from discretehelpers.boolf.a import praetor_int, twin_int

    praetor = praetor_int(noble, arity)

    return twin_int(praetor, arity - 1)


####################################################################################

def noble_to_quadrant(noble_int, arity):

    if arity == 0:
        true_except(noble_int == 0, ArgTooBigError)
        return 0

    from discretehelpers.boolf.a import noble_to_index
    from discretehelpers.boolf import Boolf

    noble_index = noble_to_index(noble_int, arity)

    return Boolf(noble_index, arity=arity-1).quadrant


def noble_to_royal_and_quadrant(noble_int, arity):

    if arity == 0:
        true_except(noble_int == 0, ArgTooBigError)
        return 0, 0

    quadrant = noble_to_quadrant(noble_int, arity)

    if quadrant == 0:  # weak evil
        return noble_int, quadrant

    def p():
        return 1 << ((1 << arity) - 1)  # unique power of two among nobles     2 ** (2 ** arity - 1)

    def q():
        return (1 << (1 << arity)) - 2  # greatest entry among nobles          2 ** (2 ** arity) - 2

    if quadrant == 1:  # strong evil
        return noble_int ^ p() ^ q(), quadrant
    if quadrant == 2:  # weak odious
        return noble_int ^ p(), quadrant
    if quadrant == 3:  # strong odious
        return noble_int ^ q(), quadrant


def noble_to_royal(noble_int, arity):
    return noble_to_royal_and_quadrant(noble_int, arity)[0]


def noble_to_king_and_quadrant(noble_int, arity):
    from discretehelpers.boolf import Boolf

    royal_int, quadrant = noble_to_royal_and_quadrant(noble_int, arity)

    royal_boolf = Boolf(royal_int, arity=arity)
    king_boolf = royal_boolf.faction_minrep
    king_int = king_boolf.tt(arity).intval
    return king_int, quadrant


def noble_to_king_index_and_quadrant(noble_int, arity):
    king_int, quadrant = noble_to_king_and_quadrant(noble_int, arity)
    king_index = noble_to_index(king_int, arity)
    return king_index, quadrant
