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
* **FitGaussian**: Fit a gaussian profile to a given distribution.
* **fmttime**: Output time elapsed in seconds into a sensible format.
* **into_pixels**: Bin a 2D dataset into pixels. This returns both the pixels and the pixel IDs of each datapoint.
* **into_vorbins**: Bin pixels into Voronoi bins (basically this is a wrapper for [voronoi.bin2d](https://github.com/lauralwatkins/voronoi) that takes care of tedious housekeeping). This returns both the bins and the bin IDs of each datapoint.
* **lims**: Returns the minimum and maximum of a distribution. There is an option to pad the limits by an additional factor f (on a linear or log scale), to include measurement errors and to pivot about a central values. This code is especially useful for calculating limits for a plot.
* **LinearTransformation**: Apply linear transformations to a set of positions in 2 dimensions.
* **minmax**: Returns the minimum and maximum value of an array simultaneously.
* **multigauss**: Evaluates multivariate Gaussian distributions, each at different data points. This code is optimised to evaluate M Gaussians of dimension N at M points. (By contrast, the scipy.stats.multivariatenormal function can only evaluate one Gaussian of dimension N at M points in one call, so (slow) for loops are required for >1 Gaussian. This method is much faster for large numbers of Gaussians.)
* **nearest**: Rounds the inputs to the nearest base. (Use with caution, due to the nature of floating point arithmetic, this maybe not work as you expect.)
* **PercentileErrors**: Returns the median of a distribution along with uncertainties estimated as the offsets of the 15.9 and 84.1 percentiles, which spans the 68.2% (or "1-sigma") confidence region.
* **PositionAngleRotation**: Rotation over position angle of major axis with respect to North, measured through East.
* **Rotate2d**: 2-d rotation of a vector around the perpendicular axis.
* **Rotate3d**: 3-d rotation of a vector around the x-, y- and z-axes.
* **randbn**: Draws numbers randomly from an input distribution in a given range.
* **whsf**: Returns the position of the first significant figure in a floating point number.


-------------------------------------------------------------------------------


REQUIREMENTS
----------------------------------------

This code uses [astropy](https://github.com/astropy/astropy), [voronoi](https://github.com/lauralwatkins/voronoi) and the standard python libraries numpy, scipy and matplotlib.
