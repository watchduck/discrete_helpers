# foibles (three metributes)

Compare the [four methods](../../methods/_foibles).<br>
The foibles not dependent on arity are _odd_, _odious_ and _ugly_.<br>
(And there is the sharpness of the dense truth table.)

<a href="https://commons.wikimedia.org/wiki/File:Foibles_of_Boolean_functions.svg">
    <img src="../../_img/Foibles_of_Boolean_functions.svg" width="300px">
</a>

## odd &nbsp; (oddness)

The following image shows the 3-ary **even** functions. (The **odd** functions are their complements.)<br>
Above are the Zhegalkin indices, below the truth tables.<br>
In both the first digit is false.

<a href="https://commons.wikimedia.org/wiki/File:Selection_of_Zhegalkin_twins;_place_0_is_0.svg">
    <img src="_img/Selection_of_Zhegalkin_twins;_place_0_is_0.svg" width="745">
</a>


## odious &nbsp; (odiousness)

The following image shows the 3-ary **evil** functions. (The **odious** functions are their complements.)<br>
Above are the Zhegalkin indices, below the truth tables.<br>
The weight of the Zhegalkin index is even, and the last digit of the truth table is false.

<a href="https://commons.wikimedia.org/wiki/File:Selection_of_Zhegalkin_twins;_tt(7)_is_0.svg">
    <img src="_img/Selection_of_Zhegalkin_twins;_tt(7)_is_0.svg" width="745">
</a>

"Last digit" is somewhat ambiguous. Digit 7 is false in all columns.<br>
The first 8 columns are the 2-ary evil functions. For them digit 3 is also false.<br>
The first 2 columns are the 1-ary evil functions. For them digit 1 is also false.


## ugly

XOR of oddness and odiousness.<br>
A Boolean function is ugly, iff the first and last digit of its truth table are different.


## dense is sharp

Attribute `dense_tt` [is_sharp](../../methods/_foibles).