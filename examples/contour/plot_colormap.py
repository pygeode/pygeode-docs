
"""
Basics of contour plots
=================================

.. currentmodule:: pygeode

Create a simple contour map using :func:`showvar()` and choose contour levels and the color map explicitly.


"""
import pygeode as pyg, numpy as np
import pylab as pyl

# Create a 2-dimensional variable to contour
time = pyg.yearlessn(180)
lon = pyg.regularlon(120)

z = 0.5*pyg.sin(2*np.pi*time/180.)**10 + pyg.cos(10 + (2*np.pi/180.)**2*time*lon) * pyg.cos(2*np.pi*time/180.)
z = z.rename('sample')

# We'll start with the default color map and contour levels:
pyl.ion()
pyg.showvar(z)

# %%
# The default color map has high dynamic range, but is also very dense for a field like this with fine scale structures
#
# We can choose any standard color map instead

pyg.showvar(z, cmap = pyl.cm.RdBu_r)

# %%
# We can also set explicitly the contour levels and contour lines

pyg.showvar(z, cmap = pyl.cm.RdBu_r, clevs = np.arange(-1.5, 1.6, 0.3), clines = np.arange(-1.5, 1.6, 0.5))
