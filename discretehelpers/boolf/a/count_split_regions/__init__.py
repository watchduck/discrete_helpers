def count_split_regions(split1, split2):
    recto1, verso1 = split1
    recto2, verso2 = split2
    return sum([
        bool(recto1.intersection(recto2)),
        bool(recto1.intersection(verso2)),
        bool(verso1.intersection(recto2)),
        bool(verso1.intersection(verso2))
    ])
