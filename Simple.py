#!/usr/bin/env python
import ncarglow as glow
from datetime import datetime
time = datetime(2015, 12, 13, 10, 0, 0)
glat = 65.1
glon = -147.5
Ap = 4
# %% solar radio flux [10-22 W m-2]
f107 = 100
f107a = 100
f107p = 100
# %% flux [erg cm-2 s-1 == mW m-2 s-1]
Q = 1
# %% characteristic energy [eV]
Echar = 100e3
# %% Number of energy bins
Nbins = 250

iono = glow.simple(time, glat, glon, f107a, f107, f107p, Ap, Q, Echar, Nbins)

for k, v in iono.items():
    print(k)
    print(v)
