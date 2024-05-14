from discretehelpers.a import make_atompattern_gen
from discretehelpers.set_part import SetPart


def atom_partition(atomval, arity):

    addend = 1 << atomval  # 2 ** atomval

    blocks = []

    gen = make_atompattern_gen(atomval, arity, negate=True)

    for k, v in enumerate(gen):
        if v:
            blocks.append([k, k + addend])

    return SetPart(blocks)
