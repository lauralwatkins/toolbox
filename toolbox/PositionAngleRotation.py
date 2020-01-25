#!/usr/bin/env python

import numpy as np


def PositionAngleRotation(pa, x, y, dx=None, dy=None):
    
    """
    Rotation over position angle of major axis with respect to North, measured
    through East.
  
    INPUTS
      pa : position angle (with angular unit)
      x  : x-coordinate (West)
      y  : y-coordinate (North)
    
    KEYWORDS
      dx : errors on x
      dy : errors on y
    
    OUTPUTS
      x : x-coordinate along major axis
      y : y-coordinate along minor axis
      dx : error on x (only if input errors given)
      dy : error on y (only if input errors given)
    """
    
    sinpa = np.sin(pa)
    cospa = np.cos(pa)
    rotation = np.array([[-sinpa, cospa], [-cospa, -sinpa]])
    
    x, y = rotation.dot([x, y])
    
    if dx is not None and dy is not None:
        dx, dy = np.sqrt((rotation**2).dot([dx**2, dy**2]))
        return x, y, dx, dy
    
    return x, y
