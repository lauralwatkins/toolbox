#!/usr/bin/env python

import numpy as np

def Rotate2d(vector, angle):
    
    """
    2-d rotation of a vector around the perpendicular axis.
    
    INPUTS
      vector : vector to be rotated
      angle : rotation angle
    
    OUTPUTS
      rotated vector
    """
    
    # cosine and sine of rotation angle
    sin_angle = np.sin(angle)
    cos_angle = np.cos(angle)
    
    # rotation matrix
    rotation_matrix = np.array([[cos_angle,sin_angle],[-sin_angle,cos_angle]])
    
    # rotated vector
    rotated_vector = rotation_matrix.dot(vector)
    
    return rotated_vector
