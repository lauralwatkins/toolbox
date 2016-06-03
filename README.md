TOOLBOX
=======

> **AUTHORS**
Laura L Watkins (STScI), <lauralwatkins@gmail.com>


-------------------------------------------------------------------------------


CONTENTS
--------

* license and referencing
* code description
* requirements


-------------------------------------------------------------------------------


LICENSE AND REFERENCING
-----------------------

This code is released under a BSD 2-clause license.

If you find this code useful for your research, please mention it in your acknowledgements.


-------------------------------------------------------------------------------


CODE DESCRIPTION
----------------

This is a random collection of useful python functions. I primarily wrote them for myself, but share them in case they are useful to anyone else.

* **clip2d**: Perform sigma-clipping of a two-dimensional distribution. Optionally, test whether a given dataset would pass or fail the sigma clipping.
* **cov_ellipse**: Calculates the x and y coordinates of an ellipse with parameters specified by a 2d covariance matrix.
* **covar**: Calculates the covariance matrix for a given parameter set.
* **ellipse**: Calculates x and y coordinates of an ellipse.
* **fit_gauss**: Fit a gaussian profile to a given distribution.
* **fmttime**: Output time elapsed in seconds into a sensible format.
* **into_pixels**: Bin a 2D dataset into pixels. This returns both the pixels and the pixel IDs of each datapoint.
* **lims**: Returns the minimum and maximum of a distribution. There is an option to pad the limits by an additional factor f (on a linear or log scale), to include measurement errors and to pivot about a central values. This code is especially useful for calculating limits for a plot.
* **minmax**: Returns the minimum and maximum value of an array simultaneously.
* **nearest**: Rounds the inputs to the nearest base. (Use with caution, due to the nature of floating point arithmetic, this maybe not work as you expect.)
* **whsf**: Returns the position of the first significant figure in a floating point number.


-------------------------------------------------------------------------------


REQUIREMENTS
----------------------------------------

This code uses [astropy](https://github.com/astropy/astropy) and the standard python libraries numpy, scipy and matplotlib.
