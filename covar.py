#!/usr/bin/env python
# -----------------------------------------------------------------------------
# COVAR
#   
#   Program calculates the covariance matrix for a given parameter set.
#   
#   INPUTS
#     x : MxN array of points ( M = # parameters, N = # samples )
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/07
# -----------------------------------------------------------------------------

from numpy import array

def covar( x ):
    
    cov = array( [ [ ( i * j ).mean() - i.mean() * j.mean()
        for j in x ] for i in x ] )
    
    return cov
