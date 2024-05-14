from discretehelpers.binv import Binv

from discretehelpers.a import true_except, vector_zip_apart, make_atompattern


def deflate(binv, atomvals):
    true_except(type(binv) == Binv, ValueError)
    vector = binv.vector
    atomvals = atomvals.copy()

    valency = len(atomvals)

    pattern_index = 0
    while True:
        if sum(vector) % 2 == 0:  # if weight even --> test vector for inflation
            if pattern_index >= valency:
                break
            pattern_bool = make_atompattern(pattern_index, valency)
            pattern = [int(val) for val in pattern_bool]  # int rather than bool expected in vector_zip_apart
            first_half, second_half = vector_zip_apart(vector, pattern)
            pattern_index += 1
            if first_half == second_half:  # if inflation found --> reduce vector by half
                vector = first_half
                valency -= 1
                del atomvals[pattern_index - 1]  # still the old pattern index
                pattern_index = 0
        else:
            break

    return Binv(vector), atomvals
