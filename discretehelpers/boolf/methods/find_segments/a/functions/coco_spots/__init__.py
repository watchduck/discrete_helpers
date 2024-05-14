import networkx as nx


def coco_spots(set_of_spots, dict_of_sets_of_links):

    graph = nx.Graph()

    for spot in set_of_spots:
        graph.add_node(spot)

    for atomkey, set_of_links in dict_of_sets_of_links.items():
        for pair_of_spots in set_of_links:
            graph.add_edge(*pair_of_spots)

    cocos = [_ for _ in nx.connected_components(graph)]
    is_connected = len(cocos) == 1

    return is_connected, cocos
