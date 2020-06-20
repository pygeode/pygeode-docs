"""
Cartopy: Quiver plot on a regional projection
=============================================
"""
import pygeode as pyg, numpy as np, pylab as pyl
from cartopy import crs as ccrs
import cartopy

# Construct dummy data for quivers
lat = pyg.gausslat(40)
lon = pyg.regularlon(80, origin=-180)

x = pyg.sin(2*np.pi * lon / 180.) * pyg.exp(-(lat - 30)**2 / (2*10**2))
y = pyg.cos(4*np.pi * lon / 180.) * pyg.exp(-(lat - 40)**2 / (4*10**2))

pyl.ioff()

# Build CartopyAxis for a Lambert Conformal projection
prj = dict(central_longitude=-90., central_latitude = 39.)
ax = pyg.plot.CartopyAxes(projection = 'LambertConformal', prj_args = prj)
ax.size = [6., 5.1]

# Add ocean
ax.add_feature(cartopy.feature.OCEAN)

# Add quiver plot
pyg.vquiver(x, y, axes=ax, width = 0.005)

# Set plot title
ax.setp(title = 'Lambert Conformal')

# Set lat/lon grid
ax.gridlines(xlocs = range(0, 361, 20), ylocs = range(-80, 81, 20))

# Set map extent to region over North America
ax.set_extent([-140, -50, 10, 75], crs = ccrs.PlateCarree())

pyl.ion()
ax.render(2)
