"""
Create a line plot
=====================

.. currentmodule:: pygeode

Plots a simple line plot using :func:`showvar()`
"""

import pygeode as pyg
import numpy as np
import pylab as pyl

N = 100
p = 0.9

# Create some normally distributed random numbers
rng = np.random.default_rng(seed = 1)
eps = rng.standard_normal(N)

# Generate an AR1 time series
ar1 = np.empty(N)
ar1[0] = eps[0]
for i in range(1, N):
  ar1[i] = p * ar1[i-1] + eps[i]

# Create an N-element time axis with no calendar
t = pyg.yearlessn(N)

# Create a pygeode variable from the numpy array
AR1 = pyg.Var((t,), values = ar1, name = 'AR1')

# Plot AR1 
ax = pyg.showvar(AR1)

pyl.ion()
ax.render()

# %%
# We can use the formatting options from the underlying :func:`matplotlib.pyplot.plot()`
# command to further customize the plot

pyl.ioff()
ax = pyg.showvar(AR1, color = 'g', marker = 'o', linewidth = 1, linestyle = '--', markersize = 4)

# We can also customize the axis labels and locators
ax.setp(ylim = (-3.5, 3.5), ylabel = '')
#ax.setp_xaxis(major_locator = pyg.timeticker.DayLocator(t, [15]))

pyl.ion()
ax.render()
