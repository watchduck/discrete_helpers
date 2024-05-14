import numpy as np


def broaden_moved(a_len, b_len, a_moved, b_moved):

    big_len = np.lcm(a_len, b_len)

    a_repetitions = big_len // a_len
    b_repetitions = big_len // b_len

    a_moved_set_big = sub(a_moved, a_len, a_repetitions)
    b_moved_set_big = sub(b_moved, b_len, b_repetitions)

    moved_set_big = a_moved_set_big.union(b_moved_set_big)

    return big_len, moved_set_big


def sub(small_set, perilen, repetitions):
    big_set = set()
    for i in range(repetitions):
        addend = i * perilen
        for small_item in small_set:
            big_item = addend + small_item
            big_set.add(big_item)
    return big_set
