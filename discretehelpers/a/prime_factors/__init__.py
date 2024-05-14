from discretehelpers.a import inventory_dict, have, true_except

from .ex import UnexpectedFactorError


def prime_factors(n, expected_factors=None):
    """
    :param n:
        integer to be factorized
    :param expected_factors:
        optional set (or list or tuple) of factors
    :return:
        usually dict of factors to exponents,
        if called with `expected_factors` tuple of exponents
    """
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)

    factors_to_exponents = inventory_dict(factors)

    if not have(expected_factors):
        return factors_to_exponents
    else:
        set_of_found_factors = set(factors_to_exponents.keys())
        set_of_expected_factors = set(expected_factors)
        true_except(set_of_found_factors.issubset(set_of_expected_factors), UnexpectedFactorError)
        expected_factors = sorted(set_of_expected_factors)
        exponents = []
        for factor in expected_factors:
            try:
                exponents.append(factors_to_exponents[factor])
            except KeyError:
                exponents.append(0)
        return exponents

"""
https://stackoverflow.com/questions/16996217/prime-factorization-list
"""