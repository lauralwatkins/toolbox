#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.MULTIGAUSS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from __future__ import division, print_function
import numpy as np


def multigauss(x, mu, cov, norm=True):
    
    """
    Evaluates multivariate Gaussian distributions, each at different data
    points. This code is optimised to evaluate M Gaussians of dimension N
    at M points. The distribution is normalised by default but there is an
    option to turn off normalisation.
    
    (By contrast, the scipy.stats.multivariatenormal function can only
    evaluate one Gaussian of dimension N at M points in one call, so (slow)
    for loops are required for >1 Gaussian. This method is much faster for
    large numbers of Gaussians.)
    
    INPUTS
      x    : variable coordinate (M x N array)
      mu   : mean of distribution (M x N array)
      cov  : covariance matrix for distribution (M x N x N array)
    
    KEYWORDS
      norm : option to normalise distribution [default: True]
    """
    
    # number of dimensions
    ndim = cov.shape[2]
    
    # normalising factors
    fac = 1.
    if norm: fac /= np.sqrt((2*np.pi)**ndim*np.abs(np.linalg.det(cov)))
    
    # invert covariance matrix
    icov = np.linalg.inv(cov)
    
    # calculate exponent, must be positive definite
    xmu = x-mu
    expo = np.einsum('ai,aij,aj->a', xmu, icov, xmu)
    expo[expo<0] = np.nan
    
    # calculate multivariate gaussian
    result = np.exp(-0.5*expo)*fac
    
    return result
