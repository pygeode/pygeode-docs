import pygeode as pyg
from pygeode.tutorial import t1

sinLat = pyg.sind(t1.lat)  # sind() takes an argument in degrees
pyg.plotvar(sinLat)

