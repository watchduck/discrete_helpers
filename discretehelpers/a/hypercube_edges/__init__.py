from discretehelpers.a import true_except

from discretehelpers.ex import ArgValueError


def hypercube_edges(n):
    true_except(type(n) == int and n >= 0, ArgValueError)
    if n == 0:
        return []
    elif n == 1:
        return [(0, 1)]
    else:
        addend = 2**(n-1)
        old_half = hypercube_edges(n-1)
        new_half = [(a+addend, b+addend) for (a, b) in old_half]
        connections = [(i, i+addend) for i in range(addend)]
        return sorted(old_half + new_half + connections)
