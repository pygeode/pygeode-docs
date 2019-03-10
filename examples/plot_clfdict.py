
"""
Specify contour levels 
=======================
Use :func:`clfdict()` to create a set of contour levels and contour lines to plot. 

"""
import pygeode as pyg, numpy as np
lat = pyg.regularlat(60)
lon = pyg.regularlon(120)

z =pyg.sin(2*np.pi*lat/180.)**10 + pyg.cos(10 + (2*np.pi/180.)**2*lat*lon) * pyg.cos(2*np.pi*lat/180.)

ax = pyg.plot.AxesWrapper()

contour_dict = pyg.clfdict(min=-1.2, axes=ax, cdelt=0.4, ndiv=3, nf=2, nl=1, extend='both', cmap='RdGy')

ax.setp(title = 'Using helper function to set up contour levels')
pyg.showvar(z, **contour_dict)



############################################################################
# ``contour_dict`` contains a dictionary of the various plotting parameters
#

print(contour_dict)
