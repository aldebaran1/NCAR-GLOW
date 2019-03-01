#!/usr/bin/env python
import ncarglow as glow
from datetime import datetime
import matplotlib.pyplot as plt

time = datetime(2017, 8, 22, 4, 0, 0)
glat = 42
glon = -100
Ap = 4
# %% solar radio flux [10-22 W m-2]
f107 = 70
f107a = 65
f107p = 65
# %% flux [erg cm-2 s-1 == mW m-2 s-1]
Q = 0
# %% characteristic energy [eV]
Echar = 0
# %% Number of energy bins
Nbins = 0

iono = glow.simple(time, glat, glon, f107a, f107, f107p, Ap, Q, Echar, Nbins)

bins = iono['Ebin_centers']
Eflux = iono['Eflux']

plt.figure(figsize=(6,8))
plt.plot(bins, Eflux, lw=2)
plt.show()

plt.figure(figsize=(6,8))
plt.title('LON: {}, LAT: {}, \n time UT: {}'.format(glat,glon,time))
plt.plot(iono['ver'][:,4], iono['ver'][:,0], 'g', lw=2, label='5577')
plt.plot(iono['ver'][:,5], iono['ver'][:,0], 'r', lw=2, label='6300')
plt.ylim([60, 500])
plt.legend()
plt.show()
