import numpy as np
from discretehelpers.a import int_to_exposet
from discretehelpers.boolf.a import atoms_to_and_gen, atoms_to_xand_gen, atoms_to_or_gen, atoms_to_xor_gen, \
    atoms_to_eq_gen, atoms_to_sand_gen, atoms_to_gand_gen, atoms_to_esand_gen, atoms_to_osand_gen


expected_mat_and = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1]
])

expected_mat_xand = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 1]
])

expected_mat_or = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1]
])

expected_mat_xor = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1]
])

expected_mat_eq = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1]
])

expected_mat_sand = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0]
])

expected_mat_gand = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 1]
])

expected_mat_esand = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 0]
])

expected_mat_osand = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1]
])

expected_matrices = {
    'AND': expected_mat_and,
    'XAND': expected_mat_xand,
    'OR': expected_mat_or,
    'XOR': expected_mat_xor,
    'EQ': expected_mat_eq,
    'SAND': expected_mat_sand,
    'GAND': expected_mat_gand,
    'ESAND': expected_mat_esand,
    'OSAND': expected_mat_osand,

}

generators = {
    'AND': atoms_to_and_gen,
    'XAND': atoms_to_xand_gen,
    'OR': atoms_to_or_gen,
    'XOR': atoms_to_xor_gen,
    'EQ': atoms_to_eq_gen,
    'SAND': atoms_to_sand_gen,
    'GAND': atoms_to_gand_gen,
    'ESAND': atoms_to_esand_gen,
    'OSAND': atoms_to_osand_gen,
}


def test():

    for operator_name, generator in generators.items():
        matrix = np.zeros([8, 8], dtype=int)

        for row_index in range(8):
            row_exposet = int_to_exposet(row_index)

            row_gen = generator(row_exposet, 3)

            matrix[row_index, :] = list(row_gen)

        expected_matrix = expected_matrices[operator_name]
        assert np.array_equal(matrix, expected_matrix)
