"""
Overplot multiple fields
=========================
"""
import pygeode as pyg, numpy as np
import pylab as pyl

ds = pyg.open('../pygeode-data/era5_202001_pl_uvt.nc', dimtypes = dict(level = pyg.Pres))

print(ds)

ds = ds(i_time = 0).mean('lon')

ws = pyg.sqrt(ds.u**2 + ds.v**2)

ax = pyg.plot.AxesWrapper()
pyg.vcontour(ds.t, axes=ax, cmap = pyl.cm.RdBu)
pyg.vcontour(ws, clines = np.linspace(0, 50, 5), axes=ax)

ax.setp(title = 'Filled contours and contour lines')

pyl.ion()

ax.render(1)
