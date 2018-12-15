# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 17:10:26 2018

@author: QQ
"""

import numpy as np


dt = 1

fixation      = 10
stimulus_min  = 80
stimulus      = 20
stimulus_max  = 1500
decision      = 30
tmax          = fixation + stimulus_max + decision






durations = {
        'fixation':  (0, fixation),
        'stimulus':  (fixation, fixation + stimulus),
        'decision':  (fixation + stimulus, fixation + stimulus + decision),
        'tmax':      tmax
        }


#l = ('FIXATION', 'LEFT', 'RIGHT')
#for i, v in enumerate(l):
#    print i, v


def get_idx(t, (start, end)):
    return list(np.where((start <= t) & (t < end))[0])    
    
def get_epochs_idx(dt, epochs):
    t = np.linspace(0, epochs['tmax'], int(epochs['tmax']/dt)+1)

    return t, {k: get_idx(t, v) for k, v in epochs.items() if k != 'tmax'}

time, epochs = get_epochs_idx(dt, durations)
print epochs