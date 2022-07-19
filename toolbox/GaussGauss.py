#!/usr/bin/env python

from scipy import stats


def GaussGauss(x, mean1, width1, mean2, width2, fraction1):
    
    """
    Function of two Gaussians.
    
    INPUTS:
      mean1: mean of Gaussian 1
      width1: width of Gaussian 1
      mean2: mean of Gaussian 2
      width2: width of Gaussian 2
      fraction1: fraction of Gaussian1
    """
    
    fraction2 = 1 - fraction1
    y = fraction1*stats.norm.pdf(x, mean1, width1) \
        + fraction2*stats.norm.pdf(x, mean2, width2)
    
    return y
