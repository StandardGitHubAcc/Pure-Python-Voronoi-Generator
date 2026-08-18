A purely Python voronoi diagram generator.
Partially implements Fortune's Algorithm, but doesn't use a beachline. Horribly unoptimized, do not use.

The diagram calculations are decoupled from the graph display; just remove matplotlib and the section before and after the labled calculation area to use the generator on its own. Near the top of the file are a bunch of points that you can try if you want.

Uses math, rather than pixel distances, to calculate diagram so the scale of the image can be arbitrarily large or small.
https://www.desmos.com/calculator/e30c04e442
In this Desmos, in order:
1. Variables and constants
2. Full derivations of equations
3. Equations turned into functions for repeated use
4. Examples of the functions being used
