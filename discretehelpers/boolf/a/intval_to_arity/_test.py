from discretehelpers.boolf.a import intval_to_arity as f


def test():

    input_to_output = {
        0: 0,
        1: 0,
        2: 1,
        3: 1,
        4: 2,
        15: 2,
        16: 3,
        255: 3,
        256: 4,
        65535: 4,
        65536: 5
    }

    for x, fx in input_to_output.items():
        assert f(x) == fx
