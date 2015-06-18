#!/usr/bin/env python
# -----------------------------------------------------------------------------
# ELLIPSE
#   
#   Program calculates the x and y coordinates of an ellipse.
#   
#   INPUTS
#     a : semi-major axis
#     b : semi-minor axis
#   
#   OPTIONS
#     xc  : x-coordinate of the centre (default: 0.)
#     yc  : y-coordinate of the centre (default: 0.)
#     rot : rotation angle of the ellipse [radians] (default: 0. = x-axis)
#     n   : number of points to generate (default: 101)
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/06
#     v1.1 : LLW, MPIA, 2013/02/27 - generate eccentric anomalies instead of
#            radii and theta to give smoother sampling
# -----------------------------------------------------------------------------

from numpy import cos, linspace, pi, sin, sqrt


def ellipse( a, b, xc=0., yc=0., rot=0., n=101 ):
    
    # generate eccentric anomaly values
    ea = linspace( 0., 2. * pi, n )
    
    # x and y coordinates
    x = a * cos( ea ) * cos( rot ) + b * sin( ea ) * sin( rot ) + xc
    y = -a * cos( ea ) * sin( rot ) + b * sin( ea ) * cos( rot ) + yc
    
    return x, y
