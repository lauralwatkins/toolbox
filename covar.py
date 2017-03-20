#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.COVAR
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def covar(x, w=None):
    
    """
    Program calculates the covariance matrix for a given parameter set.
    Weights are optional.
    
    INPUTS
      x : MxN array of points (M = # parameters, N = # samples)
    
    OPTIONS:
      w : weights at x, should also be an MxN array (default: None)
    """
    
    # set weights if not set
    if w is None: w = np.ones(x.shape)
    wtot = np.sum(w)
    
    # calculate weighted covariance
    cov = np.array([[ np.sum(i*j*w)/wtot - np.sum(i*w)/wtot*np.sum(j*w)/wtot \
        for j in x] for i in x])
    
    return cov
