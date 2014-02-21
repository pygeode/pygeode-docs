=========================
Variable input and output
=========================

Reading from files
------------------

One of the most common ways of in
Formats, specifying axes, name maps

multifile interpolation

Saving to files
---------------
naming considerations, attributes

Constructing variables in memory
--------------------------------

It is also often useful to create PyGeode variables directly in memory; for
instance, to evaluate analytical expressions on a given geophysical grid. A very
useful set of building blocks for creating variables in this way are axes
objects. If you already have a variable on the relevant grid (defined from a
file for instance), it's easy to simply use the existing axes, as has been done
in many cases in these tutorials. However, most axes objects have simple
constructors to create them directly.

.. ipython::

  In [0]: import pygeode as pyg, numpy as np

  # The simplest, default case
  In [1]: print pyg.NamedAxis(np.arange(15), 'myaxis')

  # Some simple examples
  In [1]: lon = pyg.Lon(180)
  
  In [1]: print lon

  In [2]: lat = pyg.Lat(92)

  In [2]: print lat

  In [3]: pres = pyg.Pres([1000, 900, 800, 700, 500, 300, 200, 100, 50, 30, 10])

  # Gaussian latitudes (with appropriate weights)
  In [2]: lat2 = pyg.gausslat(64)

  In [2]: print lat2

Time axes are somewhat more complicated, as you need to specify the calendar,
the reference date (``startdate``), offsets, and the native unit:

.. ipython::

  In [2]: time = pyg.ModelTime365(values=np.arange(3650), units='days', startdate=dict(year=2000, month=1))

Usually the easiest approach to creating variables in memory is to apply the
relevant mathematical operations to the axes themselves:

.. ipython::

  In [2]: pyg.sin(2*np.pi*time / 365) * pyg.exp(-(lat2 / 20.)**2) 

  In [2]: pyg.sin(2*np.pi*time / 365) * pyg.exp(-(lat2 / 20.)**2)

However, if you have a numpy array that you want to turn in to a PyGeode
variable, this can also be done.

.. ipython::

  In [2]: x = np.ones((64, 180), 'd')

  In [3]: print pyg.Var((lat2, lon), name = 'myvar', values=x)

