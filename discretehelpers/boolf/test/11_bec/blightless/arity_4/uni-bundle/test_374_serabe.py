from discretehelpers.boolf.examples import serabe as boolf


letters = ['A', 'B', 'C', 'D']


def test_serabe():

    assert boolf.filtrated_pairs_pretty(letters) == {
        'crossing': [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    }

    assert boolf.atom_to_crossing_atoms == {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }

    # FULLspots_by_degree (?)
    # FULLspotlinks_by_atom
    # border_FULLspots_by_atom
    # atom_to_crossing_atoms PRETTY
