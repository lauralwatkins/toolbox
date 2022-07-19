#!/usr/bin/env python

import numpy as np
from scipy import optimize
from .GaussGaussGauss import GaussGaussGauss


def Fit3Gaussians(data, bins=100, weights=None):
    
    """
    Fit 3 gaussian profiles to a given distribution. Returns fit and covariance.
    
    INPUTS:
      data : input quantity
    
    OPTIONS:
      bins : number of bins in histogram [default 100]
      weights : weights for data values [default None]
    """
    
    # normalised histogram of data
    yh, lims = np.histogram(data, bins=bins, density=True, weights=weights)
    xh = (lims[1:] + lims[:-1])/2
    binsize = lims.ptp()/bins
    
    # calculate mean and dispersion of input data
    m = data.mean()
    s = data.std()
    
    # initialise with means [m-s,m,m+s] and widths s, and equal split
    p0 = np.array([m-s/2, s, m, s, m+s/2, s, 1/3, 1/3])
    
    # fit mean in [-inf,inf], widths in [binsize,inf] and f in [0,1]
    # widths can't go less than binsize to stop overfitting single spikes
    p, cov = optimize.curve_fit(GaussGaussGauss, xh, yh, p0,
        bounds=([-np.inf,3*binsize,-np.inf,3*binsize,-np.inf,3*binsize,0,0],
        [np.inf,np.inf,np.inf,np.inf,np.inf,np.inf,1,1]))
    
    return p, cov
