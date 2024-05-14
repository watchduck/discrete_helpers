def to_string(v):
    result_str = ''
    for e in v:
        e_str = '1' if bool(int(e)) else '0'
        result_str += e_str
    return result_str
