#!/usr/bin/env python

from scipy import stats


def GaussGaussGauss(x, mean1, width1, mean2, width2, mean3, width3, fraction1, fraction2):
    
    """
    Function of three Gaussians.
    
    INPUTS:
      mean1: mean of Gaussian 1
      width1: width of Gaussian 1
      mean2: mean of Gaussian 2
      width2: width of Gaussian 2
      mean3: mean of Gaussian 3
      width3: width of Gaussian 3
      fraction1: fraction of Gaussian1
      fraction2: fraction of Gaussian2
    """
    
    fraction3 = 1 - fraction1 - fraction2
    y = fraction1*stats.norm.pdf(x, mean1, width1) \
        + fraction2*stats.norm.pdf(x, mean2, width2) \
        + fraction3*stats.norm.pdf(x, mean3, width3)
    
    return y
