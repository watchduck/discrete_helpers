from .a import CollectionOfSegments, loop_hypersplits, coco_spots, coco_links


def find_segments(self):

    collection = CollectionOfSegments(boolf=self)

    # loop_hypersplits(collection)

    set_of_spots = collection.get_spots()
    dict_of_sets_of_links = collection.get_links()  # atomkey --> set of spot pairs
    dict_of_sets_of_link_pairs = collection.get_neighboring_links()  # atomkey --> set of pairs of spot pairs

    # print(set_of_spots)
    # print(dict_of_sets_of_links)
    # print(dict_of_sets_of_link_pairs)

    spots_are_connected, cocos_of_spots = coco_spots(set_of_spots, dict_of_sets_of_links)
    links_are_connected, atomkey_to_cocos_of_links = coco_links(dict_of_sets_of_links, dict_of_sets_of_link_pairs, self.valency)

    all_connected = spots_are_connected and links_are_connected

    return all_connected, collection
