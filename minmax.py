#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.MINMAX
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def minmax(x):
    
    """
    Return the minimum and maximum value of an array simultaneously.
    
    INPUTS
      x : input value of array
    """
    
    return np.array([ x.min(), x.max() ])
