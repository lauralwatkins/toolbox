#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.NEAREST
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from __future__ import division, print_function


def nearest(x, base=1.):
    
    """
    Round the inputs to the nearest base. Beware, due to the nature of
    floating point arithmetic, this maybe not work as you expect.
    
    INPUTS
      x : input value of array
    
    OPTIONS
      base : number to which x should be rounded
    """
    
    return round(x/base)*base
