#!/usr/bin/env python
# --------------------------------------------------------------------------- #
# TOOLBOX.RANDBN
# Laura L Watkins [lauralwatkins@gmail.com]
# --------------------------------------------------------------------------- #

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d


def randbn(fn_name, params=None, num=1, min=0., max=1.):
    
    """
    Draws numbers randomly from an input distribution in a given range.
    
    INPUTS
      fn_name : function name [*]
    
    OPTIONS
      params  : parameters of the distribution [*][default None]
      n       : number of random numbers to generate [default 1]
      min     : lower limit of number range [default 0]
      max     : upper limit of number range [default 1]
    
    NOTES
      [*] The function 'fn_name' should calculate the values x of the required
      function for a given parameter set p, that is fn_name(x,p).
    """
    
    
    xx = np.linspace(min, max, 100)
    
    # normalisation constant and cumulative distribution function
    if not params: f = lambda x: fn_name(x)
    else: f = lambda x: fn_name(x, params)
    cst, err = quad(f, min, max)
    dx = np.array([quad(f, min, x) for x in xx]).T[0]/cst
    
    # generate random CDF values and sort for spline fitting
    cdf = np.random.rand(num)
    cdf.sort()
    
    # calculate corresponding x values
    f = interp1d(dx, xx)
    rx = f(cdf)
    
    # re-randomise (ie undo sorting)
    rx = rx[np.argsort(np.random.rand(num))]
    
    return rx
