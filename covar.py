#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.COVAR
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def covar(x):
    
    """
    Program calculates the covariance matrix for a given parameter set.
    
    INPUTS
      x : MxN array of points (M = # parameters, N = # samples)
    """
    
    cov = np.array([[ (i*j).mean()-i.mean()*j.mean() for j in x] for i in x])
    
    return cov
