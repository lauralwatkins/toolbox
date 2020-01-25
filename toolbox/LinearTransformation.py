#!/usr/bin/env python


def LinearTransformation(p, x, y):
    
    """
    Apply linear transformations to a set of positions in 2 dimensions.
    
    INPUTS
      p : linear transformation matrix
      x : x-coordinates
      y : y-coordinates
    
    OUTPUTS
      x : transformed x coordinates
      y : transformed y coordinates
    """
    
    translation = p[:2]
    rotation = p[2:].reshape(2,2).T
    
    x, y = (translation + rotation.dot([x,y]).T).T
    
    return x, y
