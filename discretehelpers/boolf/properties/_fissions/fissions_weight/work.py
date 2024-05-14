def work(self):

    result_layers = []
    result_ints = []

    for a, b in self.fissions_layered:
        result_layers.append([
            tuple([sum(_) for _ in a]),
            tuple([sum(_) for _ in b])
        ])

    for a, b in result_layers:
        result_ints.append([sum(a), sum(b)])

    return result_ints, result_layers
