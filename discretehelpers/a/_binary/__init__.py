def int_to_exposet(n):
    """integer 2**a + 2**b + 2**c ... to set of binary exponents {a, b, c...}"""
    exposet = []
    count = 0
    while n > 0:
        if n % 2:
            exposet.append(count)
        n = n // 2
        count += 1
    return exposet


def exposet_to_int(exposet):
    """set of binary exponents {a, b, c...} to integer 2**a + 2**b + 2**c ..."""
    return sum(1 << _ for _ in exposet)


def vector_to_int(vector):
    """little-endian binary vector to integer"""
    place = 0
    result = 0
    for digit in vector:
        if digit:
            result += 1 << place  # 2 ** place
        place += 1
    return result


def int_to_weight(n):
    return bin(n).count('1')
