from discretehelpers.boolf.examples import godogi


def test():

    assert godogi.hypersplits_potential_cores_pretty() == {
        1: [
            {'fixed': 'A', 'free': 'BC', 'determined': 'D−', 'vectors': ['0−−−', '0−+−', '0+−−', '0++−']},
            {'fixed': 'B', 'free': 'ACD', 'determined': '', 'vectors': ['−0−−', '−0−+', '−0+−', '−0++', '+0−−', '+0−+', '+0+−', '+0++']},
            {'fixed': 'C', 'free': 'ABD', 'determined': '', 'vectors': ['−−0−', '−−0+', '−+0−', '−+0+', '+−0−', '+−0+', '++0−', '++0+']},
            {'fixed': 'D', 'free': 'BC', 'determined': 'A−', 'vectors': ['−−−0', '−−+0', '−+−0', '−++0']}
        ],
        2: [
            {'fixed': 'AB', 'free': 'C', 'determined': 'D−', 'vectors': ['00−−', '00+−']},
            {'fixed': 'AC', 'free': 'B', 'determined': 'D−', 'vectors': ['0−0−', '0+0−']},
            {'fixed': 'BC', 'free': 'AD', 'determined': '', 'vectors': ['−00−', '−00+', '+00−', '+00+']},
            {'fixed': 'BD', 'free': 'C', 'determined': 'A−', 'vectors': ['−0−0', '−0+0']},
            {'fixed': 'CD', 'free': 'B', 'determined': 'A−', 'vectors': ['−−00', '−+00']}
        ],
        3: [
            {'fixed': 'BCD', 'free': '', 'determined': 'A−', 'vectors': ['−000']}
        ]
    }
