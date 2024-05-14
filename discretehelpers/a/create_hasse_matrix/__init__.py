import numpy as np


def create_hasse_matrix(list_of_nodes, is_under, with_indirect_edges=False):
    """Creates adjacency matrix of a Hasse diagram with nodes from `list_of_nodes`
    using the relation given by the function `is_under`.
    Matrix entries are 0 by default, 1 for a direct edge, and 2 for an indirect connection."""

    n = len(list_of_nodes)
    old_matrix = np.zeros([n, n], dtype=int)
    for i, a in enumerate(list_of_nodes):
        for j, b in enumerate(list_of_nodes):
            if is_under(a, b):
                old_matrix[i, j] = 1

    for i in range(n):
        old_matrix[i, i] = 0

    # print(old_matrix)
    # print('########################')

    new_matrix = old_matrix.copy()
    last_sum = sum(sum(new_matrix))
    while True:
        for i in range(n):
            for j in range(n):
                # An arrow (i, j) is redundant if there are already shorter arrows (i, k) and (k, j).
                # Check for shorter arrows in `old_matrix`, remove redundant longer arrows in `new_matrix`.
                if new_matrix[i, j] == 1:
                    for k in range(n):
                        if old_matrix[i, k] == 1 and old_matrix[k, j] == 1:
                            new_matrix[i, j] = 2
        current_sum = sum(sum(new_matrix % 2))  # modulo?

        if current_sum == last_sum:
            break
        last_sum = current_sum

    return new_matrix if with_indirect_edges else new_matrix % 2
