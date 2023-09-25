
"""
Use clfdict() to customize color map
=========================================

.. currentmodule:: pygeode

Illustrates the use of :func:`clfdict()` to customize contour levels.


"""
import pygeode as pyg, numpy as np
import pylab as pyl

# Create a 2-dimensional variable to contour
time = pyg.yearlessn(180)
lon = pyg.regularlon(120)

z = 0.5*pyg.sin(2*np.pi*time/180.)**10 + pyg.cos(10 + (2*np.pi/180.)**2*time*lon) * pyg.cos(2*np.pi*time/180.)
z = z.rename('sample')

# The default color map has high dynamic range, but is also very dense for a
# field like this with fine scale structures One can control the color map and
# contour levels using a higher level set of options.  The code below creates a
# divergent color map with one division (ndiv = 1) above and below zero; these
# divisions are a unit wide (cdelt = 1) and include 5 filled contours (nf = 5)
# and one contour line (nl = 1)
pyl.ion()
pyg.showvar(z, cdelt = 1., ndiv = 1, nf = 5, nl = 1)

# %%
# These arguments are a short form for calling :func:`clfdict()` to create 
# color map arguments. One can do this directly as well; here we'll use 2 divisions
# of 0.6:

cf = pyg.clfdict(cdelt = 0.6, ndiv = 2, nf = 6, nl = 1, extend = 'both')

import pprint
pprint.pprint(cf)

pyg.showvar(z, **cf)

# %%
# As a final example we can also create a sequential color map starting from -1:

cf = pyg.clfdict(cdelt = 1, min = -1.5, style = 'seq', ndiv = 3, nf = 4, nl = 2, extend = 'both')

pprint.pprint(cf)

pyg.showvar(z, **cf)
