from discretehelpers.boolf.examples import dobare, dobipi


def test():

    dobare_family = dobare.ec_family()
    dobipi_family = dobipi.ec_family()

    block_a = dobare_family.get_block_from_label(dobipi)
    block_b = dobipi_family.get_block_from_label(dobare)
    assert block_a == block_b == [1]  # intval 1 means exposet {0}, i.e. 0 gets negated

    assert dobare.apply(~0, 1, 2) == dobipi
    assert dobipi.apply(~0, 1, 2) == dobare
