#!/usr/bin/env python

import numpy as np
from units as u

def PercentileErrors(values):
    
    try:
        unit = values.unit
    except:
        unit = 1
    
    v_m1, v, v_p1 = np.percentile(values, (15.9, 50, 84.1))*unit
    ep_v = v_p1 - v
    em_v = v - v_m1
    
    return v, ep_v, em_v
