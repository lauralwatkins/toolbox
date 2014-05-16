#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.LIMS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import array, log10, size


def lims( x, f=0., log=False, err=0, pivot=None ):
    
    """
    Return the minimum and maximum of a distribution.  There is an option to
    pad the limits by an additional factor f, this is especially useful when
    calculating limits for a plot.  If f is given with two elements, then the
    upper and lower padding will be different.
    
    INPUTS
      x : data for which limits required
    
    OPTIONS
      f     : extra padding factor [default:0.] (can have different upper and
              lower padding by providing f as a list or tuple)
      log   : pad limits on log scale
      err   : errors on x, so limits will include error bars
      pivot : make limits symmetric around pivot point (use largest offset)
    """
    
    xmin = ( x - err ).min()
    xmax = ( x + err ).max()
    
    if log:
        xmin = log10( xmin )
        xmax = log10( xmax )
    
    xptp = xmax - xmin
    if size(f) == 1: f = [f]
    lims = array( [ xmin - xptp * f[0], xmax + xptp * f[-1] ] )
    
    if pivot != None:
        offset = abs( lims - pivot ).max()
        lims = pivot + array( [ -1., 1. ] ) * offset
    
    if log: lims = 10**lims
    
    return lims
