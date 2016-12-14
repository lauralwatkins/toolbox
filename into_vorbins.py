#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.INTO_VORBINS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import table, units as u
import voronoi


def into_vorbins(data_pix, pix, targetSN, x="x", y="y", id="id", n="N",
    npix="Npix", sn="SN", signal=None, noise=None, quiet=False, vquiet=True):
    
    """
    Put pixels into Voronoi bins. This is a wrapper for voronoi.bin2d (see 
    https://github.com/lauralwatkins/voronoi) that does a lot of the tedious 
    housekeeping. There are two outputs:
    1) an astropy QTable for the bins with the bin ID number, x-centre, 
       y-centre, number of objects, number of pixels, signal-to-noise, signal 
       and noise;
    2) an array containing the bin ID number of all datapoints.
    The code also adds to columns to the input pixel table (pix): "bin" 
    records the bin ID number of the pixels, and "Nbin" records the number of 
    stars in the bin to which the pixel belongs.
    
    INPUTS
      data_pix : pixel number of each datapoint
      pix : pixel grid for the data
      targetSN : target signal-to-noise required for binning
    
    OPTIONS
      x : name for x-coordinate column of input/output table [default "x"]
      y : name for y-coordinate column of input/output table [default "y"]
      id : name for bin ID column of output table [default "id"]
      n : name for number of datapoints column of inout/output table
        [default "N"]
      npix : name for number of pixels column of output table [default "Npix"]
      sn : name for signal-to-noise column of output table [default "SN"]
      signal : name for signal column of input/output table [default None](*)
      noise : name for noise column of input/output table [default None](**)
      quiet : suppress text outputs for this code? [default False]
      vquiet : suppress text outputs for Voronoi call? [default True]
    
    (*) The code uses the number of objects in the pixel for the "signal" in
    the pixel, unless a column name is passed for the signal data.
    (**) The code also assumes that the noise in the pixel is the square-root
    of the signal in the pixel (useful if the signal is the number of objects
    in the pixel), unless a column name is passed for the noise data.
    """
    
    # fail if there are no columns called n, x or y
    for key in (n, x, y):
        if key not in pix.colnames:
            print "ERROR: Could not find column '{:}' in pixel table."\
                .format(key)
            return
    
    # settings for Voronoi binning
    good = pix[n]>0
    if not signal: signal = n
    pix_signal = pix[good][signal]
    if not noise: pix_noise = np.sqrt(pix[good][signal])
    else: pix_noise = pix[good][noise]
    
    # need to have pixels on same scale for Voronoi
    xp = ((pix[x]-pix[x].min())/pix.meta["xscale"]/u.Unit(pix.meta["xunit"]))[good]
    yp = ((pix[y]-pix[y].min())/pix.meta["yscale"]/u.Unit(pix.meta["yunit"]))[good]
    
    # do the Voronoi binning
    bin = table.QTable()
    pix["bin"] = -np.ones(len(pix), dtype="int")
    pix["bin"][good], bin[x], bin[y], bin[sn], bin[npix], vscale \
        = voronoi.bin2d(xp, yp, pix_signal, pix_noise, targetSN, graphs=False,
        quiet=vquiet)
    bin["id"] = range(len(bin))
    
    # adjust bins back to real scale
    bin[x] = bin[x]*pix.meta["xscale"]*u.Unit(pix.meta["xunit"]) + pix[x].min()
    bin[y] = bin[y]*pix.meta["yscale"]*u.Unit(pix.meta["yunit"]) + pix[y].min()
    try: bin["x"].unit = pix.meta["xunit"]
    except: pass
    try: bin["y"].unit = pix.meta["yunit"]
    except: pass
    
    # bin number for each datapoint
    data_bin = pix["bin"][data_pix]
    
    # number of datapoints in each bin
    bin[n] = np.array([sum(data_bin==i) for i in range(len(bin))])
    
    # reorder columns
    bin = bin[id,x,y,n,npix,sn]
    
    # make columns to record the signal and noise in each bin
    if signal==n: signal = "signal"
    if not noise: noise = "noise"
    bin[signal] = [sum(pix_signal[pix[good]["bin"]==b["id"]]) for b in bin]
    bin[noise] = [np.sqrt(sum(pix_noise[pix[good]["bin"]==b["id"]]**2)) \
        for b in bin]
    
    # number of datapoints in bin to which pixel belongs
    pix["Nbin"] = -np.ones(len(pix), dtype="int")
    pix["Nbin"][good] = bin[pix[good]["bin"]][n]
    
    # signal and noise in bin to which pixel belongs
    pix[signal+"_bin"] = [np.nan]*len(pix)
    pix[noise+"_bin"] = [np.nan]*len(pix)
    pix[signal+"_bin"][good] = bin[pix[good]["bin"]][signal]
    pix[noise+"_bin"][good] = bin[pix[good]["bin"]][noise]
    
    if not quiet:
        print "\nVoronoi binning of pixels\n"
        print "  bins: {:}".format(len(bin))
        print "  min S/N per bin: {:}".format(bin[sn].min())
        print "  max S/N per bin: {:}".format(bin[sn].max())
        print "  avg S/N per bin: {:}".format(bin[sn].mean())
    
    return bin, data_bin
