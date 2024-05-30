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


def right_inversion_count_to_permutation(vector):
    n = len(vector)
    stack = list(range(n))
    perm = []
    for a in range(n):
        b = vector[a]
        c = stack.pop(b)
        perm.append(c)
    return perm


def left_inversion_count_to_permutation(vector):
    from collections import deque
    n = len(vector)
    stack = list(range(n))
    perm = deque()
    for a in range(n - 1, -1, -1):  # n-1, n-2 ... 1, 0
        b = vector[a]
        c = stack.pop(b)
        perm.appendleft(n - 1 - c)
    return list(perm)


def inversion_set_to_count(pairs, variant_left=True):
    assert type(variant_left) is bool
    from collections import defaultdict
    key_to_count = defaultdict(int)
    length = 0
    for a, b in pairs:
        length = max(length, a + 1, b + 1)
        key = b if variant_left else a
        key_to_count[key] += 1
    vector = [0] * length
    for key, count in key_to_count.items():
        vector[key] = count
    return vector
