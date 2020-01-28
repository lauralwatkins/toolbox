#!/usr/bin/env python


def LinearTransformation(translation, rotation, x, y):
    
    """
    Apply linear transformations to a set of positions in 2 dimensions.
    
    INPUTS
      translation : translation vector
      rotation : rotation matrix
      x : x-coordinates
      y : y-coordinates
    
    OUTPUTS
      x : transformed x coordinates
      y : transformed y coordinates
    """
    
    try: unit, x, y = x.unit, x.value, y.value
    except: unit = 1
    x, y = (translation + rotation.dot([x,y]).T*unit).T
    
    return x, y
