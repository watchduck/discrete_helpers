# basics

## installation

```
me@my:~/Code/discrete_helpers$ sudo apt install python3.8-venv
me@my:~/Code/discrete_helpers$ python3 -m venv env
me@my:~/Code/discrete_helpers$ source env/bin/activate
(env) me@my:~/Code/discrete_helpers$ pip install -r requirements.txt
```

`env/bin/python` must then be chosen as Python interpreter for the project - typically by selecting it in the IDE.

## exceptions

They are usually in `ex.py` next to the respective init and test file.<br>
There are three types, distinguished by the last word in their name:

* `Fail`:  weak exceptions used for control flow
* `Error`: normal exceptions, which are expected for bad input
* `ERROR`: strong exceptions, which should never happen

## helpers

Any folder just called `a` contains simple helper functions.<br>
There is [one for the whole project](../discretehelpers/a).<br>
Typically there is also one in a class folder, e.g. [binv/a](../discretehelpers/binv/a)

## tests

There are general tests in folders like
[boolf/test](../discretehelpers/boolf/test) and [perm/test](../discretehelpers/perm/test)
and specific tests like [a/logic_str/_test.py](../discretehelpers/a/logic_str/_test.py).<br>
The names of files in these folders must be unique.<br>
The name of a test function begins with (and sometimes is) `test`.<br>
The number of tests passed should be at least **714**.

```
(env) me@my:~/Code/discrete_helpers$ pytest -x
```

Somehow the tests do not catch import errors that appear in the console.<br>
Therefore the following includes have to be tested separately:

```
from discretehelpers.binv import Binv
from discretehelpers.boolf import Boolf
from discretehelpers.perm import Perm
from discretehelpers.set_part import SetPart
from discretehelpers.set_part_comp import SetPartComp
from discretehelpers.sig_perm import SigPerm
from discretehelpers.walsh_perm import WalshPerm
```