This script uses `SetPart` to model the Cayley table of the symmetric group S<sub>4</sub>.

<a href="https://commons.wikimedia.org/wiki/File:Symmetric_group_4;_Cayley_table_(left);_numbers.svg">
    <img src="../../../_img/Cayley_table_S4.svg" width="500px">
</a>

The 24<sup>2</sup> integer pairs (_a_, _b_) are the elements of the set to be partitioned.<br>
The block labels are the integers _c_ for which P<sub>_c_</sub> = P<sub>_a_</sub> &middot; P<sub>_b_</sub>.

```python
cayley.get_label_from_element((5, 12)) == 13
cayley.get_label_from_element((12, 5)) == 17

cayley.get_block_from_label(13) == [(0, 13), (1, 19), (2, 7), (3, 6), (4, 18), (5, 12), (6, 15), (7, 21), (8, 9), (9, 11), (10, 23), (11, 17), (12, 1), (13, 0), (14, 3), (15, 5), (16, 2), (17, 4), (18, 20), (19, 14), (20, 22), (21, 16), (22, 8), (23, 10)]
cayley.get_block_from_label(17) == [(0, 17), (1, 23), (2, 11), (3, 9), (4, 21), (5, 15), (6, 16), (7, 22), (8, 10), (9, 8), (10, 20), (11, 14), (12, 5), (13, 3), (14, 4), (15, 2), (16, 1), (17, 0), (18, 19), (19, 13), (20, 18), (21, 12), (22, 7), (23, 6)]

row_12 = [cayley.get_label_from_element((12, _)) for _ in range(24)]
row_12 == [12, 13, 14, 15, 16, 17,  2, 3, 0, 1, 5, 4,  8, 9, 6, 7, 11, 10,  22, 23, 19, 18, 21, 20]
```

This is the complete bijection between labels and blocks:
&nbsp;&nbsp;&nbsp; (It is stored in `cayley.block_labels` as a `bidict` from blocks to labels.)

```
0: [(0, 0), (1, 1), (2, 2), (3, 4), (4, 3), (5, 5), (6, 6), (7, 7), (8, 12), (9, 18), (10, 13), (11, 19), (12, 8), (13, 10), (14, 14), (15, 20), (16, 16), (17, 22), (18, 9), (19, 11), (20, 15), (21, 21), (22, 17), (23, 23)]
1: [(0, 1), (1, 0), (2, 3), (3, 5), (4, 2), (5, 4), (6, 7), (7, 6), (8, 13), (9, 19), (10, 12), (11, 18), (12, 9), (13, 11), (14, 15), (15, 21), (16, 17), (17, 23), (18, 8), (19, 10), (20, 14), (21, 20), (22, 16), (23, 22)]
2: [(0, 2), (1, 4), (2, 0), (3, 1), (4, 5), (5, 3), (6, 8), (7, 10), (8, 14), (9, 20), (10, 16), (11, 22), (12, 6), (13, 7), (14, 12), (15, 18), (16, 13), (17, 19), (18, 11), (19, 9), (20, 17), (21, 23), (22, 15), (23, 21)]
3: [(0, 3), (1, 5), (2, 1), (3, 0), (4, 4), (5, 2), (6, 9), (7, 11), (8, 15), (9, 21), (10, 17), (11, 23), (12, 7), (13, 6), (14, 13), (15, 19), (16, 12), (17, 18), (18, 10), (19, 8), (20, 16), (21, 22), (22, 14), (23, 20)]
4: [(0, 4), (1, 2), (2, 5), (3, 3), (4, 0), (5, 1), (6, 10), (7, 8), (8, 16), (9, 22), (10, 14), (11, 20), (12, 11), (13, 9), (14, 17), (15, 23), (16, 15), (17, 21), (18, 6), (19, 7), (20, 12), (21, 18), (22, 13), (23, 19)]
5: [(0, 5), (1, 3), (2, 4), (3, 2), (4, 1), (5, 0), (6, 11), (7, 9), (8, 17), (9, 23), (10, 15), (11, 21), (12, 10), (13, 8), (14, 16), (15, 22), (16, 14), (17, 20), (18, 7), (19, 6), (20, 13), (21, 19), (22, 12), (23, 18)]

6: [(0, 6), (1, 7), (2, 12), (3, 18), (4, 13), (5, 19), (6, 0), (7, 1), (8, 2), (9, 4), (10, 3), (11, 5), (12, 14), (13, 20), (14, 8), (15, 10), (16, 22), (17, 16), (18, 15), (19, 21), (20, 9), (21, 11), (22, 23), (23, 17)]
7: [(0, 7), (1, 6), (2, 13), (3, 19), (4, 12), (5, 18), (6, 1), (7, 0), (8, 3), (9, 5), (10, 2), (11, 4), (12, 15), (13, 21), (14, 9), (15, 11), (16, 23), (17, 17), (18, 14), (19, 20), (20, 8), (21, 10), (22, 22), (23, 16)]
8: [(0, 8), (1, 10), (2, 14), (3, 20), (4, 16), (5, 22), (6, 2), (7, 4), (8, 0), (9, 1), (10, 5), (11, 3), (12, 12), (13, 18), (14, 6), (15, 7), (16, 19), (17, 13), (18, 17), (19, 23), (20, 11), (21, 9), (22, 21), (23, 15)]
9: [(0, 9), (1, 11), (2, 15), (3, 21), (4, 17), (5, 23), (6, 3), (7, 5), (8, 1), (9, 0), (10, 4), (11, 2), (12, 13), (13, 19), (14, 7), (15, 6), (16, 18), (17, 12), (18, 16), (19, 22), (20, 10), (21, 8), (22, 20), (23, 14)]
10: [(0, 10), (1, 8), (2, 16), (3, 22), (4, 14), (5, 20), (6, 4), (7, 2), (8, 5), (9, 3), (10, 0), (11, 1), (12, 17), (13, 23), (14, 11), (15, 9), (16, 21), (17, 15), (18, 12), (19, 18), (20, 6), (21, 7), (22, 19), (23, 13)]
11: [(0, 11), (1, 9), (2, 17), (3, 23), (4, 15), (5, 21), (6, 5), (7, 3), (8, 4), (9, 2), (10, 1), (11, 0), (12, 16), (13, 22), (14, 10), (15, 8), (16, 20), (17, 14), (18, 13), (19, 19), (20, 7), (21, 6), (22, 18), (23, 12)]

12: [(0, 12), (1, 18), (2, 6), (3, 7), (4, 19), (5, 13), (6, 14), (7, 20), (8, 8), (9, 10), (10, 22), (11, 16), (12, 0), (13, 1), (14, 2), (15, 4), (16, 3), (17, 5), (18, 21), (19, 15), (20, 23), (21, 17), (22, 9), (23, 11)]
13: [(0, 13), (1, 19), (2, 7), (3, 6), (4, 18), (5, 12), (6, 15), (7, 21), (8, 9), (9, 11), (10, 23), (11, 17), (12, 1), (13, 0), (14, 3), (15, 5), (16, 2), (17, 4), (18, 20), (19, 14), (20, 22), (21, 16), (22, 8), (23, 10)]
14: [(0, 14), (1, 20), (2, 8), (3, 10), (4, 22), (5, 16), (6, 12), (7, 18), (8, 6), (9, 7), (10, 19), (11, 13), (12, 2), (13, 4), (14, 0), (15, 1), (16, 5), (17, 3), (18, 23), (19, 17), (20, 21), (21, 15), (22, 11), (23, 9)]
15: [(0, 15), (1, 21), (2, 9), (3, 11), (4, 23), (5, 17), (6, 13), (7, 19), (8, 7), (9, 6), (10, 18), (11, 12), (12, 3), (13, 5), (14, 1), (15, 0), (16, 4), (17, 2), (18, 22), (19, 16), (20, 20), (21, 14), (22, 10), (23, 8)]
16: [(0, 16), (1, 22), (2, 10), (3, 8), (4, 20), (5, 14), (6, 17), (7, 23), (8, 11), (9, 9), (10, 21), (11, 15), (12, 4), (13, 2), (14, 5), (15, 3), (16, 0), (17, 1), (18, 18), (19, 12), (20, 19), (21, 13), (22, 6), (23, 7)]
17: [(0, 17), (1, 23), (2, 11), (3, 9), (4, 21), (5, 15), (6, 16), (7, 22), (8, 10), (9, 8), (10, 20), (11, 14), (12, 5), (13, 3), (14, 4), (15, 2), (16, 1), (17, 0), (18, 19), (19, 13), (20, 18), (21, 12), (22, 7), (23, 6)]

18: [(0, 18), (1, 12), (2, 19), (3, 13), (4, 6), (5, 7), (6, 20), (7, 14), (8, 22), (9, 16), (10, 8), (11, 10), (12, 21), (13, 15), (14, 23), (15, 17), (16, 9), (17, 11), (18, 0), (19, 1), (20, 2), (21, 4), (22, 3), (23, 5)]
19: [(0, 19), (1, 13), (2, 18), (3, 12), (4, 7), (5, 6), (6, 21), (7, 15), (8, 23), (9, 17), (10, 9), (11, 11), (12, 20), (13, 14), (14, 22), (15, 16), (16, 8), (17, 10), (18, 1), (19, 0), (20, 3), (21, 5), (22, 2), (23, 4)]
20: [(0, 20), (1, 14), (2, 22), (3, 16), (4, 8), (5, 10), (6, 18), (7, 12), (8, 19), (9, 13), (10, 6), (11, 7), (12, 23), (13, 17), (14, 21), (15, 15), (16, 11), (17, 9), (18, 2), (19, 4), (20, 0), (21, 1), (22, 5), (23, 3)]
21: [(0, 21), (1, 15), (2, 23), (3, 17), (4, 9), (5, 11), (6, 19), (7, 13), (8, 18), (9, 12), (10, 7), (11, 6), (12, 22), (13, 16), (14, 20), (15, 14), (16, 10), (17, 8), (18, 3), (19, 5), (20, 1), (21, 0), (22, 4), (23, 2)]
22: [(0, 22), (1, 16), (2, 20), (3, 14), (4, 10), (5, 8), (6, 23), (7, 17), (8, 21), (9, 15), (10, 11), (11, 9), (12, 18), (13, 12), (14, 19), (15, 13), (16, 6), (17, 7), (18, 4), (19, 2), (20, 5), (21, 3), (22, 0), (23, 1)]
23: [(0, 23), (1, 17), (2, 21), (3, 15), (4, 11), (5, 9), (6, 22), (7, 16), (8, 20), (9, 14), (10, 10), (11, 8), (12, 19), (13, 13), (14, 18), (15, 12), (16, 7), (17, 6), (18, 5), (19, 3), (20, 4), (21, 2), (22, 1), (23, 0)]
```