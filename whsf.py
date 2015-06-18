#!/usr/bin/env python
# -----------------------------------------------------------------------------
# WHSF
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import *


def whsf( x ):
    
    """
    Returns the position of the first significant figure in a floating point
    number.  Positive numbers indicate the first significant digit is after
    the decimal point, negative numbers are before the decimal point.
    
    INPUT
      x : input number
    """
    
    # calculate position of first significant figure
    sf = -int_( floor( log10( x ) ) )
    
    # round number to first significant figure
    if size( x ) == 1: rd = round( x, sf )
    else: rd = array( [ round( x[i], sf[i] ) for i in range( x.size ) ] )
    
    # check SF of rounded number as rounding can cause problems just below 1
    # e.g. 0.096 returns sf=2, but the rounded value is 0.10 which has sf=1
    sf = -int_( floor( log10( rd ) ) )
    
    return sf
