#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.CLIP2D
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import toolbox


def clip2d(xx, yy, sigma, nmax=10, verbose=False, graph=False):
    
    """
    Perform sigma-clipping of a two-dimensional distribution.
    
    INPUTS:
      xx    : x-coordinates
      yy    : y-coordinates
      sigma : number of sigmas at which to clip
    
    OPTIONS:
      nmax    : maximum number of iterations [default 10]
      verbose : print out progress [default False]
      graph   : show graph of results [default False]
    """
    
    
    if verbose: print "\nsigma clip at {:} sigma".format(sigma)
    
    keep = np.array([ int(n) for n in np.linspace(0,len(xx)-1,len(xx)) ])
    fail = np.array([], dtype="int")
    
    count = 1
    nremoved = 1
    while count <= nmax and nremoved > 0:
        
        x = xx[keep]
        y = yy[keep]
        
        # estimate dispersions by fitting gaussian
        px = toolbox.fit_gauss(x)[0]
        py = toolbox.fit_gauss(y)[0]
        
        # create elliptical limits from dispersions and clip data
        a = sigma * px[1]
        b = sigma * py[1]
        phi = np.arctan2(y-py[0],x-px[0])
        rell = a*b / np.sqrt( (a*np.sin(phi))**2 + (b*np.cos(phi))**2 )
        r = np.sqrt( (x-px[0])**2 + (y-py[0])**2 )
        fail = np.append(fail, keep[r>=rell])
        keep = keep[r<rell]
        
        nremoved = len(x)-np.size(keep)
        if verbose: print "  {:} ... removed {:}".format(count, nremoved)
        count += 1
    
    
    if verbose:
        print "  dispersions: {:}|{:} mas/yr".format(px[1],py[1])
        print "  clip values: {:}|{:} mas/yr".format(a,b)
        print "  points removed: {:}".format(len(xx)-keep.size)
        print "  points remaining: {:}".format(keep.size)
        print ""
    
    if graph:
        
        # set up plotting
        plt.rc('font', family='serif')
        plt.rc('text', usetex=True)
        plt.rc('xtick', labelsize='8')
        plt.rc('ytick', labelsize='8')
        plt.rc('axes', labelsize='10')
        plt.rc('legend', fontsize='9')
        
        fig = plt.figure(figsize=(4,3))
        fig.subplots_adjust(left=0.13, bottom=0.13, top=0.97, right=0.97)
        plt.xlim(toolbox.lims(xx))
        plt.ylim(toolbox.lims(yy))
        plt.xlabel(r"$\rm x \; coordinate$")
        plt.ylabel(r"$\rm y \; coordinate$")
        plt.scatter(xx[keep], yy[keep], lw=0, c="k", s=5)
        plt.scatter(xx[fail], yy[fail], lw=0, c="r", s=5)
        plt.show()
    
    return keep, fail
