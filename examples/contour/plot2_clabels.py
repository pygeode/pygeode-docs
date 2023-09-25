"""
Contour map with vcontour()
====================================

.. currentmodule:: pygeode

Create a contour map with lines, filled contours, hatching, and contour
labels using the lower level :func:`vcontour()`

"""
import pylab as pyl

import pygeode as pyg
import numpy as np
from pygeode.tutorial import t1

ax = pyg.plot.AxesWrapper()

# Plot contour lines, use 5 divisions
pyg.vcontour(t1.Temp, clines=5, clevs=None, colors='k', axes=ax)

# Add labels
ax.clabel(ax.plots[0], colors='k', fmt='%d', fontsize=14)

# Add filled contour lines, use 10 divisions
pyg.vcontour(t1.Temp, clines = None, clevs = 10, cmap='BuGn', axes=ax)

# Add stippling between 200 and 280 K
pyg.vcontour(t1.Temp, clevs=[200,280], hatches=['..'], alpha=0, axes=ax)

ax.setp(title = 'Plot specific contours and hatching')

pyl.ion()
ax.render(1)
