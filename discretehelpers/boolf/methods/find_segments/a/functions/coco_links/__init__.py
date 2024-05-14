import networkx as nx


def coco_links(dict_of_sets_of_links, dict_of_sets_of_link_pairs, valency):

    all_are_connected = True
    atomkey_to_cocos = dict()

    for atomkey in range(valency):

        graph = nx.Graph()

        try:
            set_of_links = dict_of_sets_of_links[atomkey]
            for link in set_of_links:
                graph.add_node(link)
        except KeyError:
            pass

        try:
            set_of_link_pairs = dict_of_sets_of_link_pairs[atomkey]
            for pair_of_links in set_of_link_pairs:
                graph.add_edge(*pair_of_links)
        except KeyError:
            pass

        cocos = [_ for _ in nx.connected_components(graph)]
        if len(cocos) > 1:
            all_are_connected = False
        atomkey_to_cocos[atomkey] = cocos

    return all_are_connected, atomkey_to_cocos
