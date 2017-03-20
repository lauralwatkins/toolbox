#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.COV_ELLIPSE
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from ellipse import ellipse
from covar import covar


def cov_ellipse(x, sigma=1., w=None):
    
    """
    Program calculates the x and y coordinates of an ellipse with parameters
    specified by a 2d covariance matrix.
    
    INPUTS
      x : 2xN array of points (N = # samples)
    
    OPTIONS
      sigma : level of contours (default: 1.)
      w : weights for covariance calculation (default: None)
    """
    
    cov = covar(x, w=w)
    
    # calculate eigenvalues and eigenvectors
    e, v = np.linalg.eig(cov)
    
    # rotation angle of the ellipse
    rot = -np.arctan2(v[1,0], v[0,0])
    
    # semi-major and semi-minor axes
    a = np.sqrt(e[0])*sigma
    b = np.sqrt(e[1])*sigma
    
    # ellipse centre
    if w is None: w = np.ones(x.shape)
    xc = np.sum(x[0]*w)/np.sum(w)
    yc = np.sum(x[1]*w)/np.sum(w)
    
    # ellipse coordinates
    x, y = ellipse(a, b, xc=xc, yc=yc, rot=rot)
    
    return x, y
