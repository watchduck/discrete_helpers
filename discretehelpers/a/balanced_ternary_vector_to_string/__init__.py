def balanced_ternary_vector_to_string(vector):

    int_to_char = {-1: '−', 0: '0', 1: '+'}

    list_of_chars = []

    for entry in vector:
        char = int_to_char[entry]
        list_of_chars.append(char)

    return ''.join(list_of_chars)
