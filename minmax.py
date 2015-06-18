#!/usr/bin/env python
# -----------------------------------------------------------------------------
# STATS.MINMAX
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import array


def minmax( x ):
    
    """
    Return the minimum and maximum value of an array simultaenously.
    
    INPUTS
      x : input value of array
    """
    
    return array([ x.min(), x.max() ])
