#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.LIMS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import array, log10


def lims( x, f=0., log=False, err=0 ):
    
    """
    Return the minimum and maximum of a distribution.  There is an option to
    pad the limits by an additional factor f, this is especially useful when
    calculate limits for a plot.
    
    INPUTS
      x : data for which limits required
    
    OPTIONS
      f : extra padding factor [default:0.]
    """
    
    xmin = ( x - err ).min()
    xmax = ( x + err ).max()
    
    if log:
        xmin = log10( xmin )
        xmax = log10( xmax )
    
    xptp = xmax - xmin
    lims = array( [ xmin - xptp * f, xmax + xptp * f ] )
    
    if log: lims = 10**lims
    
    return lims
