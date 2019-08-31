#!/usr/bin/env python

import numpy as np


def Rotate3d(vector, theta_x, theta_y, theta_z):
    
    """
    3-d rotation of a vector around the x-, y- and z-axes.
    
    INPUTS
      vector : vector to be rotated
      theta_x : rotation angle around x-axis
      theta_y : rotation angle around y-axis
      theta_z : rotation angle around z-axis
    
    OUTPUTS
      rotated vector
    """
    
    # cosines and sines of rotation angles
    sinx = np.sin(theta_x)
    cosx = np.cos(theta_x)
    siny = np.sin(theta_y)
    cosy = np.cos(theta_y)
    sinz = np.sin(theta_z)
    cosz = np.cos(theta_z)
    
    # rotation matrices for each axis
    rx = np.array([[1, 0, 0], [0, cosx, -sinx], [0, sinx, cosx]])
    ry = np.array([[cosy, 0, siny], [0, 1, 0], [-siny, 0, cosy]])
    rz = np.array([[cosz, -sinz, 0], [sinz, cosz, 0], [0, 0, 1]])
    
    # combined rotation matrices
    rotation_matrix = rz.dot(ry.dot(rx))
    
    # rotated vector
    rotated_vector = rotation_matrix.dot(vector)
    
    return rotated_vector
