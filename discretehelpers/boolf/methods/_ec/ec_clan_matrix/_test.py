from discretehelpers.boolf.examples import berusa


def test_berusa():

    faction_reps, family_reps, faction_rep_to_row, family_rep_to_col, rep_pair_to_splinter, \
        faction_splinter_sizes, lcm_of_splinter_sizes, \
        faction_rep_to_weight, faction_rep_to_keyneg_exposet, family_rep_to_perm_exposet, \
        zhe_to_keyneg_exposet, zhe_to_valneg_exposet, zhe_to_index_triples = berusa.ec_clan_matrix()

    assert faction_reps == [151, 158, 189, 233]

    assert family_reps == [151]

    assert faction_rep_to_row == {
        151: [151],
        158: [158, 182, 214],
        189: [189, 219, 231],
        233: [233]
    }

    assert family_rep_to_col == {
        151: [151, 158, 182, 189, 214, 219, 231, 233]
    }

    assert rep_pair_to_splinter == {
        (151, 151): [151],
        (158, 151): [158, 182, 214],
        (189, 151): [231, 219, 189],
        (233, 151): [233]
    }

    assert faction_splinter_sizes == {151: 1, 158: 3, 189: 3, 233: 1}

    assert lcm_of_splinter_sizes == 3

    assert faction_rep_to_weight == {151: 5, 158: 5, 189: 6, 233: 5}

    assert faction_rep_to_keyneg_exposet == {151: [6], 158: [2, 4, 7], 189: [0, 3, 5], 233: [1]}

    assert family_rep_to_perm_exposet == {151: [0, 1, 2, 3, 4, 5]}

    assert zhe_to_keyneg_exposet == {
        151: [6],
        158: [2, 4, 7],
        182: [2, 4, 7],
        189: [0, 3, 5],
        214: [2, 4, 7],
        219: [0, 3, 5],
        231: [0, 3, 5],
        233: [1]
    }

    assert zhe_to_valneg_exposet == {
        151: [3, 5, 6],
        158: [1, 2, 7],
        182: [1, 4, 7],
        189: [0, 3, 5],
        214: [2, 4, 7],
        219: [0, 3, 6],
        231: [0, 5, 6],
        233: [1, 2, 4]
    }

    assert zhe_to_index_triples == {  # (keyneg_index, perm_index, valneg_index)
        151: [(6, 0, 6), (6, 1, 5), (6, 2, 6), (6, 3, 3), (6, 4, 5), (6, 5, 3)],
        158: [(2, 0, 2), (2, 1, 1), (4, 2, 2), (4, 4, 1), (7, 3, 7), (7, 5, 7)],
        182: [(2, 2, 4), (2, 3, 1), (4, 0, 4), (4, 5, 1), (7, 1, 7), (7, 4, 7)],
        189: [(0, 0, 0), (0, 2, 0), (3, 1, 3), (3, 3, 5), (5, 4, 3), (5, 5, 5)],
        214: [(2, 4, 4), (2, 5, 2), (4, 1, 4), (4, 3, 2), (7, 0, 7), (7, 2, 7)],
        219: [(0, 1, 0), (0, 4, 0), (3, 0, 3), (3, 5, 6), (5, 2, 3), (5, 3, 6)],
        231: [(0, 3, 0), (0, 5, 0), (3, 2, 5), (3, 4, 6), (5, 0, 5), (5, 1, 6)],
        233: [(1, 0, 1), (1, 1, 2), (1, 2, 1), (1, 3, 4), (1, 4, 2), (1, 5, 4)]
    }
