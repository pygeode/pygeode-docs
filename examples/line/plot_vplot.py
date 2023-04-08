"""
Overplot lines with vplot
==========================

.. currentmodule:: pygeode

Overplots two lines using lower level plotting routine :func:`vplot()`
"""

import pygeode as pyg, numpy as np
import pylab as pyl 

# Create a 400-element time axis starting Jan 1 year 2000 with a time step of 6 hours
t = pyg.modeltime365n('2000-01-01', 400, step=0.25, units = 'days')

y1 = pyg.exp(-t / 30.) * pyg.cos(2*np.pi * t / 20.)
y2 = pyg.exp(-t / 30.) * pyg.sin(2*np.pi * t / 20.)

y1 = y1.rename('y1')
y2 = y2.rename('y2')

pyl.ioff()

# Create an axis wrapper object to hold the plot
ax = pyg.plot.AxesWrapper()

# Add the two lines
pyg.vplot(y1, label='y1', c='r', lw=2, axes=ax)
pyg.vplot(y2, label='y2', c='b', lw=2, axes=ax)

ax.setp(title = 'Two lines', ylabel='')


ax.legend(loc='lower right', frameon=False)

pyl.ion()
ax.render()

# %%
# The default tick locator/formatter used by pygeode for time axes is
# somewhat aware of the time range being displayed and adjusts the 
# format and spacing of ticks appropriately

pyl.ioff()
ax.setp(xlim = (0, 20))

pyl.ion()
ax.render()

# %%
# You can chose the tick spacing and format explicitly; in this case with major
# ticks every month and minor ticks every 5 days.
pyl.ioff()

# For 
ax.setp(xlim = (0, 100))
ax.setp_xaxis(major_formatter=pyg.timeticker.TimeFormatter(t, '$b'), \
              major_locator = pyg.timeticker.MonthLocator(t, 1), \
              minor_locator = pyg.timeticker.DayOfMonthLocator(t, 5))
pyl.ion()
ax.render()
