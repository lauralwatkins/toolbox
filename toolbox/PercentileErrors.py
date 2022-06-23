#!/usr/bin/env python

import numpy as np

def PercentileErrors(values):
    
    """
    Returns the median of a distribution along with uncertainties estimated as
    the offsets of the 15.9 and 84.1 percentiles, which spans the 68.2% (or
    "1-sigma") confidence region. For a Gaussian, these are equivalent to the
    mean and standard deviation.
  
    INPUTS
      values : array of values, can optionally have units
    
    OUTPUTS
      v : median value of the distribution
      ep_v : plus / upper uncertainty
      em_v : minus / lower uncertainty
    """
    
    v_m1, v, v_p1 = np.percentile(values, (15.9, 50, 84.1))
    ep_v = v_p1 - v
    em_v = v - v_m1
    
    return v, ep_v, em_v
