figures = '0123456789'


def pretty_signs(arg):

    raw_string = str(arg).replace('True', '●').replace('False', '○')

    result = []

    last_char = ' '
    for char in raw_string:
        if char in figures and (last_char not in figures and last_char != '-'):
            result.append(' ')  # space instead of a plus sign
        result.append(char)
        last_char = char

    return ''.join(result)
