from discretehelpers.boolf.examples import medusa
from discretehelpers.boolf.methods.find_segments.a import CollectionOfSegments


def test():

    collection = CollectionOfSegments(boolf=medusa)
    assert collection.number_by_dimension == [13, 22, 12, 2, 0]
