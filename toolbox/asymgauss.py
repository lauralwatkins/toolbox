#!/usr/bin/env python

import numpy as np
from scipy import stats


def asymgauss(x, mu, sigma_lower, sigma_upper):
    
    """
    Program calculates an asymmetric Gaussian distribution (ie. a Gaussian
    with different standard deviations above and below the mean) for a given
    mean and standard deviations. There is an option to adjust the height of
    the distibution.
    
    INPUTS
      x           : variable coordinate
      mu          : mean of distribution
      sigma_lower : standard deviation of distribution below the mean
      sigma_upper : standard deviation of distribution above the mean
    """
    
    # check that widths are positive
    sigma_lower = np.abs(sigma_lower)
    sigma_upper = np.abs(sigma_upper)
    
    fac = 2/(sigma_lower+sigma_upper)
    
    y_lower = fac*sigma_lower*stats.norm.pdf(x, mu, sigma_lower)
    y_upper = fac*sigma_upper*stats.norm.pdf(x, mu, sigma_upper)
    
    y = (x<mu)*y_lower + (x>=mu)*y_upper
    
    return y
