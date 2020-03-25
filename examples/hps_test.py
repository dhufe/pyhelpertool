#hps_test.py
import numpy as np
import scipy.signal as sigpy
import matplotlib.pyplot as plt

from pyhelpertool.HelpersSignal import PitchDetechtion

fs = 2e6
fn = 19e3
N = 4096
dt = 1/fs
df = fs/N

t = np.linspace ( 0, N * dt, N)
# Ampltude weights
w = np.array  ( [ .1, 1, 1, 1, 1, 1, 1] )
# Frequency multiplier
fr = np.array ( [ 1, 3, 5, 7, 9, 11, 13] )
f = np.arange ( 0, fs, df )

# Creating test signal by summing up different frequencies
y = np.zeros ( N )
for weight, freq in zip(w, fr ):
    y += weight * np.sin ( 2 * np.pi * freq * fn * t )

# Detect fundamental frequency using harmonic product spectrum
f2 = PitchDetechtion( y, fs )

# Get nearest value by minimal distance
fc = f[np.argmin( np.abs ( f - fn ) )]

print ( 'Fundamental frequency : %3.3f kHz' % (fn)  )
print ( 'Frequency domain resolution %2.3f Hz' % (df) )
print ( 'Nearest value  %2.3f Hz' % ( fc ) )
print ( 'Fundamental frequency detected : %3.3f kHz' % (f2*1e-3)  )
