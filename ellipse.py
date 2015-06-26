#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.ELLIPSE
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def ellipse(a, b, xc=0., yc=0., rot=0., n=101):
    
    """
    Program calculates the x and y coordinates of an ellipse.
    
    INPUTS
      a : semi-major axis
      b : semi-minor axis
    
    OPTIONS
      xc  : x-coordinate of the centre (default: 0.)
      yc  : y-coordinate of the centre (default: 0.)
      rot : rotation angle of the ellipse [radians] (default: 0. = x-axis)
      n   : number of points to generate (default: 101)
    """
    
    # generate eccentric anomaly values
    ea = np.linspace(0., 2.*np.pi, n)
    
    # x and y coordinates
    x = a * np.cos(ea)*np.cos(rot) + b*np.sin(ea)*np.sin(rot) + xc
    y = -a * np.cos(ea)*np.sin(rot) + b*np.sin(ea)*np.cos(rot) + yc
    
    return x, y
