This function recognizes inflated truth tables of Boolean functions, and returns the shortest possible one, that encodes the same information.

It also receives and returns the list of integers denoting the arguments. (These `atomvals` can be thought of as the names of the sets or atomic statements.)

The opposite can be achieved with the method [`inflated_fullspots`](../../methods/inflated_fullspots). This is demonstrated in [`test_inflate_and_deflate`](_test.py).