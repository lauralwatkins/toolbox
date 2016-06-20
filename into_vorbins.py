#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.INTO_VORBINS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import table
import voronoi


def into_vorbins(data_pix, pix, targetSN, x="x", y="y", id="id", n="N",
    sn="SN", npix="Npix", quiet=False, vquiet=True):
    
    """
    Put pixels into Voronoi bins. This is a wrapper for voronoi.bin2d (see 
    https://github.com/lauralwatkins/voronoi) that does a lot of the tedious 
    housekeeping. There are two outputs:
    1) an astropy QTable for the bins with the bin ID number, x-centre, 
       y-centre, number of objects, signal-to-noise, and number of pixels;
    2) an array containing the bin ID number of all datapoints.
    The code also adds to columns to the input pixel table (pix): "bin" 
    records the bin ID number of the pixels, and "Nbin" records the number of 
    stars in the bin to which the pixel belongs.
    
    
    INPUTS
      data_pix : pixel number of each datapoint
      pix : pixel grid for the data
      targetSN : target signal-to-noise required for binning
    
    OPTIONS
      x : name for x-coordinate column of output table [default "x"]
      y : name for y-coordinate column of output table [default "y"]
      id : name for pixel ID column of output table [default "id"]
      n : name for number of datapoints column of output table [default "N"]
      sn : name for signal-to-noise column of output table [default "SN"]
      npix : name for number of pixels column of output table [default "Npix"]
      quiet : suppress text outputs for this code? [default False]
      vquiet : suppress text outputs for Voronoi call? [default True]
    """
    
    # fail if there are no columns called n, x or y
    for key in (n, x, y):
        if key not in pix.colnames:
            print "ERROR: Could not find column '{:}' in pixel table."\
                .format(key)
            return
    
    # settings for Voronoi binning
    good = pix[n]>0
    signal = pix[good][n]
    noise = np.sqrt(pix[good][n])
    
    # need to have pixels on same scale for Voronoi
    xp = (pix[x] - pix[x].min())/pix.meta["xscale"]
    yp = (pix[y] - pix[y].min())/pix.meta["yscale"]
    
    # do the Voronoi binning
    bin = table.QTable()
    pix["bin"] = -np.ones(len(pix), dtype="int")
    pix["bin"][good], bin[x], bin[y], bin[sn], bin[npix], vscale \
        = voronoi.bin2d(xp[good], yp[good], signal, noise, targetSN,
        graphs=False, quiet=vquiet)
    bin["id"] = range(len(bin))
    
    # adjust bins back to real scale
    bin[x] *= pix.meta["xscale"]
    bin[y] *= pix.meta["yscale"]
    try: bin["x"].unit = pix.meta["xscale"].unit
    except: pass
    try: bin["y"].unit = pix.meta["yscale"].unit
    except: pass
    
    # bin number for each datapoint
    data_bin = pix["bin"][data_pix]
    
    # number of stars in each bin
    bin[n] = np.array([sum(data_bin==i) for i in range(len(bin))])
    
    # number of stars in bin to which pixel belongs
    pix["Nbin"] = -np.ones(len(pix), dtype="int")
    pix["Nbin"][good] = bin[pix[good]["bin"]][n]
    
    # reorder columns
    bin = bin[id,x,y,n,sn,npix]
    
    if not quiet:
        print "\nVoronoi binning of pixels\n"
        print "  bins: {:}".format(len(bin))
        print "  min stars per bin: {:}".format(bin[n].min())
        print "  max stars per bin: {:}".format(bin[n].max())
        print "  avg stars per bin: {:}".format(int(np.round(bin[n].mean())))
    
    return bin, data_bin
