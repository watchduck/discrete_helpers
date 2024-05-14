from discretehelpers.set_part import SetPart


def test_simple():
    set_part = SetPart([[1, 2, 3, 4], [6, 7]])
    set_part.refine_block([[1, 2], [3, 4]])
    assert set_part == SetPart([[1, 2], [3, 4], [6, 7]])


def test_labels():
    set_part = SetPart([[1, 2, 3, 4], [6, 7]])
    set_part.add_label_to_element(1, 'below 5')
    set_part.add_label_to_element(6, 'above 5')
    assert dict(set_part.block_labels) == {
        (1, 2, 3, 4): 'below 5',
        (6, 7): 'above 5'
    }

    set_part.refine_block(new_blocks=[[1, 2, 4], [3]], new_labels=['powers of 2', 'singleton 3'])
    assert set_part == SetPart([[1, 2, 4], [6, 7]])
    assert dict(set_part.block_labels) == {
        (6, 7): 'above 5',
        (1, 2, 4): 'powers of 2',
        (3,): 'singleton 3'
    }
