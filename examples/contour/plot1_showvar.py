"""
Contour map with showvar()
======================================

.. currentmodule:: pygeode

An example of creating a simple contour plot with :func:`showvar()`.
"""
import pygeode as pyg, numpy as np
import pylab as pyl

# Use some sample data from ERA5 to create a plot
ds = pyg.open('../pygeode-data/era5_202001_pl_uvt.nc', dimtypes = dict(level = pyg.Pres))

# Compute the zonal mean temperature on 1 Jan 2020
t = ds.t(time = '2020-01-01').mean('lon')

pyl.ioff()

# Create plot using default options
ax = pyg.showvar(t)

# Set plot title 
ax.axes[0].setp(title = 'Temperature 1 Jan 2020')

# Add units caption to the colorbar
ax.axes[1].setp(title = 'K')

pyl.ion()

ax.render(1)

