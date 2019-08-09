======================
Working with Datasets
======================

.. currentmodule:: pygeode

PyGeode :class:`Var` objects can be grouped together into :class:`Dataset`
objects. This is convenient for dealing with, for instance, the contents of 
a large NetCDF file which defines multiple variables, but datasets can be used
to perform a number of bulk operations on all (or some) of the variables they
contain, which can also be quite powerful. 

As a simple example, let's return to the second dataset in the tutorial module, 
and select a single timestep:

.. ipython::

  In [0]: import pygeode as pyg, numpy as np

  In [0]: from pygeode.tutorial import t2

  In [2]: print(t2(time='1 Sep 2010'))

As you can see this returns a new dataset with the appropriate selection from
each variable contained in the dataset. Many operations defined for single 
variables have equivalent versions that act on whole datasets:

.. ipython::

  In [0]: import pygeode as pyg

  In [0]: from pygeode.tutorial import t2

  In [2]: print(t2.mean('time'))

  In [2]: print(t2.transpose('time', 'lon', 'lat', 'pres'))

  In [2]: print(t2.extend(0, pyg.NamedAxis(name = 'member', values=np.arange(5))))

If you have a custom operation you need to perform, or perhaps a more
complicated set of operations, this can also be done. Write a function that
takes as its first argument a variable from the dataset, and returns a new,
modified variable, then carry out this operation using :meth:`Dataset.map`.
As a simple example, consider the following

.. ipython::

  In [2]: def sel(v, lat=0):
     ...:   return v(s_lat=lat).rename(v.name + '_' + v.lat.formatvalue(lat, '%dN'))

  In [5]: t_eq = t2.map(sel); print(t_eq)

  # You can also pass additional arguments, either by keyword
  In [5]: t_5s = t2.map(sel, lat=-5); print(t_5s)

  # or as a positional argument
  In [5]: t_5n = t2.map(sel, 5); print(t_5n)

In more complicated datasets, this can be very useful for operating only on a
subset of the variables (for instance, only those)

One can then combine these datasets

.. ipython::

  In [6]: print(t_5s + t_5n)

  In [7]: print(t_5n.rename_vars(Temp_5N = 'T_5n'))

