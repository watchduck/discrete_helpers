# foibles (four methods)

Compare the [three metributes](../../metributes/_foibles).<br>
The foibles dependent on arity are _sharp_, _acute_, _rude_ and _rough_.

<a href="https://commons.wikimedia.org/wiki/File:Foibles_of_Boolean_functions.svg">
    <img src="../../_img/Foibles_of_Boolean_functions.svg" width="300px">
</a>

## acute

Acuteness is a rather unintuitive property of a truth table.

* XOR of oddness, odiousness and sharpness, i.e. `self.is_ugly ^ self.is_sharp(arity)`.
* The [patron quadrant](../_patron) is 1 or 2, i.e. the patron's oddness and odiousness are different.
* The [weight quadrant](../_quadrant_extensions) is different from the quadrant.

<img src="_img/3-ary_Boolean_functions;_Walsh_126.svg" width="500">

See [conjecture](../../conjectures/3_acute).


## sharp

A truth table is sharp, if its weight is odd.<br>
As increasing the arity means doubling the weight, only the shortest truth table of a Boolf can be sharp.

<img src="_img/3-ary_Boolean_functions;_Walsh_255.svg" width="500">

The twin of a sharp Boolean function is odious.


## rude

Rude is sharp XOR odd.<br>
The twin of a rude Boolean function is ugly.<br>
Its reverse is rough.


<img src="_img/3-ary_Boolean_functions;_Walsh_254.svg" width="500">


## rough

Rough is sharp XOR odious.<br>
The twin of a rough Boolean function is also rough.<br>
Its reverse is rude.

<img src="_img/3-ary_Boolean_functions;_Walsh_127.svg" width="500">
