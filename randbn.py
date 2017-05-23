#!/usr/bin/env python
# --------------------------------------------------------------------------- #
# TOOLBOX.RANDBN
# Laura L Watkins [lauralwatkins@gmail.com]
# --------------------------------------------------------------------------- #

from __future__ import division, print_function
import numpy as np
from scipy import integrate, interpolate


def randbn(fn_name, params=None, num=1, vmin=0., vmax=1., ncdf=20):
    
    """
    Draws numbers randomly from an input distribution in a given range.
    
    INPUTS
      fn_name : function name [*]
    
    OPTIONS
      params  : parameters of the distribution [*][default None]
      num     : number of random numbers to generate [default 1]
      vmin    : lower limit of number range [default 0]
      vmax    : upper limit of number range [default 1]
      ncdf    : number of points at which to sample the CDF [**][default 20]
    
    NOTES
      [*] The function 'fn_name' should calculate the values x of the required
      function for a given parameter set p, that is fn_name(x,p).
      [**] Sampling the CDF at more points will increase the computation time
      as each point requires an integral, but it may be necessary for complex
      functions.
    """
    
    
    values = np.linspace(vmin, vmax, ncdf)
    
    # normalised cumulative distribution function
    if not params: f = lambda x: fn_name(x)
    else: f = lambda x: fn_name(x, params)
    cdf = np.cumsum([integrate.quad(f, values[max(0,i-1)], values[i])[0] \
        for i in range(ncdf)])
    cdf /= cdf[-1]
    
    # sample is drawn by calculating the value for randomly-generated CDFs
    sample = interpolate.interp1d(cdf, values)(np.random.rand(num))
    
    return sample
