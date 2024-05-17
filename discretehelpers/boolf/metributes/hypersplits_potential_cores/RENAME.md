Each hypersplit must have at least one core segment of the respective dimension.<br>

Assume a function with sets A, B, C, D and a hypersplit of sets A, B, C.<br>
There are two possible core segments: `000−` and `000+`<br>
These are the crossing points of the borders of A, B, C. There is one inside and one outside of set D.

If both segments are potential cores, the respective dict looks like this:<br>
* `{'fixed': [0, 1, 2], 'free': [3], 'determined': {}}`

If the core must be inside or outside of set D, it looks like this:<br>
* `{'fixed': [0, 1, 2], 'free': [], 'determined': {3: '+'}}`<br>
* `{'fixed': [0, 1, 2], 'free': [], 'determined': {3: '−'}}`

See also method [`hypersplits_potential_cores_pretty`](../../methods/_pretty/hypersplits_potential_cores_pretty).
