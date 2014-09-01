#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.LIMS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import *


def lims( x, f=0., log=False, err=0, pivot=None ):
    
    """
    Return the minimum and maximum of a distribution.  There is an option to
    pad the limits by an additional factor f, this is especially useful when
    calculating limits for a plot.  If f is given with two elements, then the
    upper and lower padding will be different.  The program ignores nan values.
    
    INPUTS
      x : data for which limits required
    
    OPTIONS
      f     : extra padding factor [default:0.] (can have different upper and
              lower padding by providing f as a list or tuple)
      log   : pad limits on log scale
      err   : errors on x, so limits will include error bars (can have
              different upper/lower errors by passing as (plus,minus) tuple)
      pivot : make limits symmetric around pivot point (use largest offset)
    """
    
    
    # check if plus/minus errors are different
    if shape(err) == (2,) + shape(x):
        perr = err[0]
        merr = err[1]
    else:
        perr = err
        merr = err
    
    xmin = nanmin(x-merr)
    xmax = nanmax(x+perr)
    
    if log:
        xmin = log10(xmin)
        xmax = log10(xmax)
    
    if pivot != None:
        offset = max(pivot-xmin, xmax-pivot)
        xmin = pivot-offset
        xmax = pivot+offset
    
    xptp = xmax - xmin
    if size(f) == 1: f = [f]
    lims = array([ xmin - xptp * f[0], xmax + xptp * f[-1] ])
    
    if log: lims = 10**lims
    
    return lims
