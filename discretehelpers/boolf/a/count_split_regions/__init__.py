def count_split_regions(split1, split2):
    pos1, neg1 = split1
    pos2, neg2 = split2
    return sum([
        bool(pos1.intersection(pos2)),
        bool(pos1.intersection(neg2)),
        bool(neg1.intersection(pos2)),
        bool(neg1.intersection(neg2))
    ])
