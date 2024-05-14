# ceiling of the binary logarithm

`2 ** log_ceil(x)` is the length required for a truth table whose number value requires _x_ binary digits.<br>
See [`intval_to_tt_length`](../../boolf/a/intval_to_tt_length).


<table>
<tr>
<th>arguments</th>
<th>result</th>
<th><code>2 ** result</code></th>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>3 ... 4</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td>5 ... 8</td>
<td>3</td>
<td>8</td>
</tr>
<tr>
<td>9 ... 16</td>
<td>4</td>
<td>16</td>
</tr>
<tr>
<td>17 ... 32</td>
<td>5</td>
<td>32</td>
</tr>
</table>

Compare [`log_floor`](../log_floor).
