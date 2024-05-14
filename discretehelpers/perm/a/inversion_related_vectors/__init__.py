def left_inversion_count(p):
    n = len(p)
    v = [0] * n
    for i in range(n):
        count = 0
        for k in range(i):
            if p[k] > p[i]:
                count += 1
        v[i] = count
    return v


def right_inversion_count(p):
    n = len(p)
    v = [0] * n
    for i in range(n):
        count = 0
        for k in range(i, n):
            if p[k] < p[i]:
                count += 1
        v[i] = count
    return v


def inversion_vector(p):
    n = len(p)
    v = [0] * n
    for i in range(n):
        count = 0
        for k in range(i):
            if p[k] > p[i]:
                count += 1
        v[p[i]] = count
    return v
