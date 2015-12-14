#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.LIMS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def lims(x, f=0., log=False, err=0, pivot=None):
    
    """
    Return the minimum and maximum of a distribution. There is an option to
    pad the limits by an additional factor f, this is especially useful when
    calculating limits for a plot. If f is given with two elements, then the
    upper and lower padding will be different. The program ignores nan values.
    
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
    
    try: unit, x = x.unit, x.value
    except: unit = 1.
    xerr = err/unit
    
    # check if plus/minus errors are different
    if np.shape(xerr) == (2,) + np.shape(x):
        perr = xerr[0]
        merr = xerr[1]
    else:
        perr = xerr
        merr = xerr
    
    xmin = np.nanmin(x-merr)
    xmax = np.nanmax(x+perr)
    
    if log:
        xmin = np.log10(xmin)
        xmax = np.log10(xmax)
    
    if pivot != None:
        offset = max(pivot-xmin, xmax-pivot)
        xmin = pivot-offset
        xmax = pivot+offset
    
    xptp = xmax - xmin
    if np.size(f)==1: f = [f]
    lims = np.array([ xmin-xptp*f[0], xmax+xptp*f[-1] ])
    
    if log: lims = 10**lims
    
    lims = lims*unit
    
    return lims
