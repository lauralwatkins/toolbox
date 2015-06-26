#!/usr/bin/env python
# -----------------------------------------------------------------------------
# TOOLBOX.FMTTIME
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------


def fmttime(time):
    
    """
    Output time elapsed in seconds into a sensible format.
    
    INPUTS
      time : input time elapsed [seconds]
    """
    
    sc = time % 60.
    time = (time-sc)/60.
    result = "{:}s".format(sc)
    if not time: return result
    
    mn = int(time % 60.)
    time = (time-mn)/60.
    result = "{:}m {:}".format(mn, result)
    if not time: return result
    
    hr = int(time % 24.)
    time = (time-hr)/24.
    result = "{:}h {:}".format(hr, result)
    if not time: return result
    
    dy = int(time % 7.)
    time = (time-dy)/7.
    result = "{:}d {:}".format(dy, result)
    
    return result
