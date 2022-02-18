#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.LIMS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from __future__ import division, print_function
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
    except: unit = 1
    if unit is None: unit = 1
    
    # check if plus/minus errors are different
    if np.shape(err) == (2,) + np.shape(x):
        perr = err[0]
        merr = err[1]
    else:
        perr = err
        merr = err
    
    try: meunit, merr = merr.unit, merr.value
    except: meunit = 1.
    try: peunit, perr = perr.unit, perr.value
    except: peunit = 1.
    
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
