# Schoute wrapper (faction)

This function uses [schoute_coset_gen](../../../../../../a/schoute_coset_gen).

Take the following matrices for the example Boolf _farofe_:

<a href="https://commons.wikimedia.org/wiki/File:Faction_of_Zhe_8329.svg">
    <img src="../../faction_minrep/_img/Faction_of_Zhe_8329.svg" width="1005px">
</a>

The point of this wrapper is to get the complement of a column in the green matrix.<br>
It is the complement, because potential representatives are in the false places,<br>
which are here shown in white.

A slight complication is needed to make the code faster:

* If the layer is mostly true, it is efficient to find the few false places and return them.<br>
  (In this case `needles` are the false places of the layer.)
* But if the layer is mostly false, it is more efficient to find the few true places, and complement the result.<br>
  (In this case `needles` are the true places of the layer.)
