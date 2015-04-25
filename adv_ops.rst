Advanced Variable Operations
============================

.. currentmodule:: pygeode

.. _timeaxisops:

Time Axis Operations
--------------------

PyGeode recognizes many types of geophysical dimensions, some of which we've
already seen in these tutorials. By far the most complicated of these are those
axes representing the time dimension. PyGeode has a reasonably sophisticated
time axis, which is aware of four main types of Calandars - the standard Julian
calendar (:class:`StandardTime`), a 365-day calendar (:class:`ModelTime365`), a
360-day calendar (:class:`ModelTime360`), and a yearless calendar
(:class:`Yearless`) with no temporal organization at scales longer than days. 

Creating Time Axes
..................

Time axes will often be created automatically from datasets with CF-compliant
metadata (of which PyGeode is aware); but they can also be created manually.
There are two broad ways to create a time axis: 1) in terms of an offset from a
reference date and 2) by directly specifying dates and times.

The first requires specifying a reference date (``startdate``), a list of
values representing offsets from this date, and the units in which these
offsets are specified (``seconds``, ``minutes``, ``hours``, or ``days``); this
is usually the more convenient way to construct an axis.

.. ipython::

  In [1]: import pygeode as pyg, numpy as np

  # A time axis representing the (leap) year 2008 at 6 h increments
  In [2]: print pyg.StandardTime(values=np.arange(0, 24*366, 6), units = 'hours', startdate=dict(year=2008, month=1, day=1))

  # 2000 to 2010 in 360-day years
  In [3]: print pyg.ModelTime360(values=np.arange(10*360), units = 'days', startdate=dict(year=2000, month=1, day=1))

The second involves providing an explicit list of the dates and times of each element of the 
axis. PyGeode recognizes the auxiliary arrays ``year``, ``month``, ``day``,
``hour``, ``minute`` and ``second``, though not all need to be explicitly
provided:

.. ipython::

  # A time axis representing the months of 1890
  In [4]: print pyg.ModelTime365(year=12*[1890], month=range(1, 13), units='days')

Combining Time Axes
...................

Internally the axis values (used for mapping two axes, selecting subranges, and
plotting) are represented as offsets from the reference ``startdate``. PyGeode
will map between the two if a valid map exists (:ref:`broadcasting`), though
note that which reference frame the result will be returned in can depend on the
order of operations:
  
.. ipython::

  # A time axis representing the year 2005 at 6 h increments
  In [5]: t1 = pyg.ModelTime365(values=np.arange(0, 24*365, 6), units = 'hours', startdate=dict(year=2005, month=1, day=1))

  # Another time axis representing the same dates but with a different reference
  In [5]: t2 = pyg.ModelTime365(values=365. + np.arange(0, 365, 0.25), units = 'days', startdate=dict(year=2004, month=1, day=1))

  # Sum these in two different ways
  In [5]: ts12 = t1 + t2

  # Since either axis can be mapped to each other, these will differ
  In [5]: ts21 = t2 + t1 

  # Both of these work and refer to the same time period...
  In [6]: print ts12.time.units

  # ...but are defined in different reference frames.
  In [6]: print ts21.time.units

  # Accessing absolute times will work the same in each case
  In [6]: print ts12(time='15 Jan 2005').time, ts21(time='15 Jan 2005').time

  # But relative times will differ
  In [6]: print ts12(time=400).time, ts21(time=400).time

Accessing any results by an absolute date will therefore yield the same result,
but accessing by value will not. Moreover since PyGeode used the ``values``
array for plotting, this can affect details of plots. At present this ambiguity
only exists if the mapping can be done both ways; if one is a strict subset of
the other the result will always be in the reference frame of the smaller axis.

Climatological statistics
.........................

A variety of time averaging operations are possible. In addition to computing
climatologies, one can compute monthly means, daily means, diurnal means, and
trends. These should generally work as expected; however, PyGeode also
implements special mapping rules for time axes so that anomalies from these time
averages can be easily defined. In general these are based on the 

oOne common operation is to
compute climatologies. As described in the first of these tutorials this is
simply performed as follows

.. ipython::

  In [10]: from pygeode.tutorial import t2

  In [10]: Tc = pyg.climatology(t2.Temp)    # Compute the climatology

  In [10]: 


Time axis utilities
...................

There are a number of other useful utility functions for working with time axes
in the timeutils module. For instance, it is sometimes convenient to convert
data on a a standardtime axis 


EOFs, correlation and regression analysis
-----------------------------------------

include lag correlation

Integration and Differentiation
-------------------------------

Interpolation
-------------

Composites
----------

Smoothing
---------

