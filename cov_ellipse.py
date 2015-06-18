#!/usr/bin/env python
# -----------------------------------------------------------------------------
# COV_ELLIPSE
#   
#   Program calculates the x and y coordinates of an ellipse with parameters
#   specified by a 2d covariance matrix.
#   
#   INPUTS
#     x : 2xN array of points (N = # samples)
#   
#   OPTIONS
#     sigma : level of contours (default: 1.)
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/07
# -----------------------------------------------------------------------------

from numpy import arctan2, sqrt
from numpy.linalg import eig
from ellipse import ellipse
from covar import covar

def cov_ellipse( x, sigma=1. ):
    
    cov = covar( x )
    
    # calculate eigenvalues and eigenvectors
    e, v = eig( cov )
    
    # rotation angle of the ellipse
    rot = -arctan2( v[1,0] , v[0,0] )
    
    # semi-major and semi-minor axes
    a = sqrt( e[0] ) * sigma
    b = sqrt( e[1] ) * sigma
    
    x, y = ellipse( a, b, xc=x[0].mean(), yc=x[1].mean(), rot=rot )
    
    return x, y
