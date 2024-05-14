from discretehelpers.a import true_except

from .ex import *


def to_pretty_string(vector):
    if type(vector) == str:
        vector = vector.replace(' ', '')
    length = len(vector)
    allowed_lengths = [2**i for i in range(7)]

    true_except(length in allowed_lengths, PrettyLengthError)

    string = ''
    for i, digit in enumerate(vector):
        string += str(int(digit))
        if not i+1 == length:
            if (i+1) % 4 == 0:
                if (i+1) % 16 == 0:
                    string += '  '  # two spaces between groups of 16 digits
                else:
                    string += ' '  # one space between groups of 4 digits
    return string
