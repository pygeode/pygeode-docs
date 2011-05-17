import pygeode as pyg
from pygeode.tutorial import t1

pyg.plotvar(t1.Temp - t1.Temp.mean('lon'))
