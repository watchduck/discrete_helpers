from discretehelpers.a import true_except
from discretehelpers.ex import ArgValueError


def alphabet_subset(exposet):

    if max(exposet) < 26:

        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        result = []

        for i in exposet:
            result.append(alphabet[i])

        return result

    else:

        return exposet
