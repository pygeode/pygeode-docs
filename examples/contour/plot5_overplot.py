"""
Add a colorbar manually
===========================================
"""
import pygeode as pyg, numpy as np
import pylab as pyl

ds = pyg.open('../pygeode-data/era5_202001_pl_uvt.nc', dimtypes = dict(level = pyg.Pres))

print(ds)

# Compute time average over the first 20 timesteps and zonal mean
ds = ds(mi_time = (0, 20)).mean('lon')

pyl.ioff()

ax = pyg.plot.AxesWrapper()
pyg.vcontour(ds.t, axes=ax, cmap = pyl.cm.RdBu)
pyg.vcontour(ds.u, clines = np.linspace(0, 50, 5), colors = 'k', axes=ax)

# Add colorbar. pos = 'b' puts the colorbar at the bottom of the plot
# rb (and rt, rr, rl) allow you to tweak the location of the colorbar
axg = pyg.plot.colorbar(ax, ax.plots[0], pos = 'b', format = "%d K", rb = 0.6)

ax.setp(title = 'Zonal mean temperature and winds')

pyl.ion()

axg.render(1)
