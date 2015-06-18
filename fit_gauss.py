#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.FIT_GAUSS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import *
from matplotlib.pyplot import *
from scipy import optimize, stats


def fit_gauss(data, bins=100, showplot=False, label=None):
    
    """
    Fit a gaussian profile to a given distribution.
    
    INPUTS:
      data : input quantity
    
    OPTIONS:
      bins : number of bins in histogram [default 100]
      showplot : show plot of histogram and fit? [default False]
      label : label for plot axes. [default None]
    """
    
    # normalised histogram of data
    yh, lims = histogram(data, bins=bins, normed=True)
    xh = (lims[1:] + lims[:-1])/2.
    
    # fit gaussian to distribution
    p0 = array([ data.mean(), data.std() ])
    p, cov = optimize.curve_fit(stats.norm.pdf, xh, yh, p0)
    p[1:] = abs(p[1:])
    
    if showplot:
        
        # set up plotting
        rc('font', family='serif')
        rc('text', usetex=True)
        rc('xtick', labelsize='8')
        rc('ytick', labelsize='8')
        rc('axes', labelsize='10')
        rc('legend', fontsize='9')
        
        # set up figure
        fig = figure(figsize=(4,3))
        fig.subplots_adjust(left=0.15, bottom=0.13, top=0.97, right=0.97)
        
        # plot histogram
        hist(data, bins=bins, histtype="stepfilled", alpha=0.3, color="grey",
            normed=True)
        plot(xh, yh, "ko", alpha=0.2)
        
        # array for plotting
        xx = linspace(data.min(), data.max(), 201)
        
        # fitted double gaussian
        yy = stats.norm.pdf(xx, *p)
        plot( xx, yy, c="r", alpha=0.8, lw=2, label="fit" )
        
        if label:
            xlabel(label)
            ylabel(r"$f($" + label + r"$)$")
        
        legend(frameon=False)
        
        show()
    
    
    return p, cov
