#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.INTO_PIXELS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from __future__ import division, print_function
import numpy as np
from astropy import table


def into_pixels(xdata, ydata, nx=None, ny=None, xscale=None, yscale=None,
    xlim=None, ylim=None, x="x", y="y", id="id", n="N", quiet=False):
    
    """
    Put a 2D dataset into pixels. The code returns two objects:
    1) an astropy QTable for the pixels with the pixel ID number, x-centre, 
       y-centre, and number of objects -- the properties of the pixel grid 
       are also output in the Qtable metadata;
    2) an array containing the pixel ID number of all input objects -- 
       objects outside the limits of the pixel grid are given a pixel ID of -1.
    
    INPUTS
      xdata : first coordinate of data (refered to as "x")
      ydata : second coordinate of data (refered to as "y")
    
    OPTIONS
      nx : number of pixels in x [default None] (*)
      ny : number of pixels in y [default None] (*)
      xscale : scale of x pixels [default None] (*)
      yscale : scale of y pixels [default None] (*)
      xlim : limits of pixelised area in x [default None] (*)
      ylim : limits of pixelised area in y [default None] (*)
      x : name for x-coordinate column of output table [default "x"]
      y : name for y-coordinate column of output table [default "y"]
      id : name for pixel ID column of output table [default "id"]
      n : name for number of datapoints column of output table [default "N"]
      quiet : suppress text outputs? [default False]
    
    NOTES
      (*) Some pixels settings must be provided, but it is not necessary to 
        provide all options. The behaviour of the code for different 
        combinations of inputs is outlined here:
        1) No settings are provided: the code will fail.
        2) Limits only: the code will fail.
        3) Number of pixels only: the data limits are used for the pixel
           limits. Then the behaviour follows from case 5.
        4) Scale only: the data limits are used but with the lower limit
           rounded down to the nearest scale factor and the upper limit
           rounded up to the nearest scale factor. Then the behaviour follows 
           from case 7.
        5) Limits and number of pixels: scale is calculated. Then the 
           behaviour follows from case 8.
        6) Scale and number of pixels: limits are chosen so that the centre 
           of the pixel grid coincides with the centre of the data. Then the 
           behaviour follows from case 8.
        7) Limits and scale: number of pixels is calculated. Then the 
           behaviour proceeds as case 8.
        8) Number of pixels, pixel scale and limits are all given: the code 
           checks that they are all consistent, and fails if not.
    """
    
    # throw an error if no settings are given for the x pixels
    if not xlim and not xscale and not nx:
        print("ERROR: Please provide pixel settings for the x-coordinate.")
        return
    
    # throw an error if no settings are given for the y pixels
    if not ylim and not yscale and not ny:
        print("ERROR: Please provide pixel settings for the y-coordinate.")
        return
    
    # do no proceed if only limits are given for x-coordinate
    if xlim and not xscale and not nx:
        print("ERROR: Please provide required number of pixels or pixel "\
            +"scale for x-coordinate as well as limits of pixelised region.")
        return
    
    # do no proceed if only limits are given for y-coordinate
    if ylim and not yscale and not ny:
        print("ERROR: Please provide required number of pixels or pixel "\
            +"scale for y-coordinate as well as limits of pixelised region.")
        return
    
    # calculate limits, if needed
    if not xlim:
        if nx and xscale:
            xmid = xdata.min()+xdata.ptp()/2.
            xlim = (xmid-nx/2.*xscale, xmid+nx/2.*xscale)
        elif not xscale: xlim = (xdata.min(), xdata.max())
        else: xlim = (np.floor(xdata.min()/xscale)*xscale,
            np.ceil(xdata.max()/xscale)*xscale)
    if not ylim:
        if ny and yscale:
            ymid = ydata.min()+ydata.ptp()/2.
            ylim = (ymid-ny/2.*yscale, ymid+ny/2.*yscale)
        elif not yscale: ylim = (ydata.min(), ydata.max())
        else: ylim = (np.floor(ydata.min()/yscale)*yscale,
            np.ceil(ydata.max()/yscale)*yscale)
    
    # calculate pixel scale, if needed
    if not xscale: xscale = (xlim[1]-xlim[0])/nx
    if not yscale: yscale = (ylim[1]-ylim[0])/ny
    
    # calculate number of pixels, if needed
    if not nx: nx = int(np.round((xlim[1]-xlim[0])/xscale))
    if not ny: ny = int(np.round((ylim[1]-ylim[0])/yscale))
    
    # make sure pixel numbers are integers
    if nx!=int(nx):
        print("You have a non-integer number of x pixels.")
        return
    if ny!=int(ny):
        print("You have a non-integer number of y pixels.")
        return
    
    # total number of pixels
    npix = nx*ny
    
    # check that everything is consistent
    dx = 1-(xlim[1]-xlim[0])/nx/xscale
    dy = 1-(ylim[1]-ylim[0])/ny/yscale
    if np.abs(dx)>1e-3 or np.abs(dy)>1e-3:
        if np.abs(dx)>1e-3: print("ERROR: Your x-coordinate scales, limits, "\
            +"and pixel numbers are inconsistent.")
        if np.abs(dy)>1e-3: print("ERROR: Your y-coordinate scales, limits, "\
            +"and pixel numbers are inconsistent.")
        return
    
    
    
    if not quiet:
        print("\nbin 2D data into pixels")
        print("")
        print("  x coordinate: {:}".format(x))
        print("  y coordinate: {:}".format(y))
        print("")
        print("  x scale: {:} /pixel".format(xscale))
        print("  y scale: {:} /pixel".format(yscale))
        print("")
        print("  x limits: {:} to {:}".format(*xlim))
        print("  y limits: {:} to {:}".format(*ylim))
        print("")
        print("  x pixels: {:}".format(nx))
        print("  y pixels: {:}".format(ny))
        print("  total pixels: {:}".format(npix))
    
    # make QTable for pixels
    pix = table.QTable()
    pix[id] = range(npix)
    
    # pixel centres
    xx = np.linspace(xlim[0]/xscale+0.5, xlim[1]/xscale-0.5, nx)*xscale
    yy = np.linspace(ylim[0]/yscale+0.5, ylim[1]/yscale-0.5, ny)*yscale
    pix[x], pix[y] = [p.reshape(npix) for p in np.meshgrid(xx,yy)]
    
    # pixel number for each datapoint
    data_pix = (np.round((xdata-xx.min())/xscale) \
        + np.round((ydata-yy.min())/yscale)*nx).astype(int)
    data_pix[(xdata<xlim[0])|(xdata>xlim[1])|(ydata<ylim[0])|(ydata>ylim[1])]\
        = -1
    
    # number of datapoints in each pixel
    pix[n] = np.histogram(data_pix, range=(-0.5,npix-0.5), bins=npix)[0]
    
    # put grid properties into metadata
    pix.meta = {
        "npix": npix,
        "nx": nx,
        "ny": ny,
        "xmin": min(xlim),
        "xmax": max(xlim),
        "ymin": min(ylim),
        "ymax": max(ylim),
        "xscale": xscale,
        "yscale": yscale,
    }
    
    return pix, data_pix
