# meet and join

Mathematics Stackexchange: [Meets and joins in the lattice of partitions](https://math.stackexchange.com/questions/2064808/meets-and-joins-in-the-lattice-of-partitions)

Meet and join are methods that combine two partitions.
* The meet ∧ is the coarsest partition finer than both. &nbsp; (greatest lower bound)
* The join ∨ is the finest partition coarser than both. &nbsp; (least upper bound)

The meet is easy to calculate. The join currently uses the metribute [pairs](../../metributes/pairs), which is expensive.

## example

```python
red = SetPart([[0, 1, 2, 4], [5, 6, 9], [7, 8]])
green = SetPart([[0, 1], [2, 3, 4], [6, 8, 9]])

assert red.meet(green) == SetPart([[0, 1], [2, 4], [6, 9]])
assert red.join(green) == SetPart([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
```

The brown fields are the intersection of the red and the green partitions.

<a href="https://commons.wikimedia.org/wiki/File:Join_and_meet_of_a_partition_of_a_10-set.svg">
    <img src="_img/join_and_meet_of_a_partition_of_a_10-set.svg">
</a>
