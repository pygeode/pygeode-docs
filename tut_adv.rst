Advanced Variable Operations
============================

.. currentmodule:: pygeode

Climatological statistics
.........................

A variety of time averaging operations are possible. In addition to computing
climatologies, one can compute monthly means, daily means, diurnal means, and
trends. These should generally work as expected; however, PyGeode also
implements special mapping rules for time axes so that anomalies from these time
averages can be easily defined. In general these are based on the 

A common operation is to
compute climatologies. As described in the first of these tutorials this is
simply performed as follows

.. ipython::
  
  @suppress
  In [0]: import pygeode as pyg

  In [10]: from pygeode.tutorial import t2

  In [10]: Tc = pyg.climatology(t2.Temp)    # Compute the climatology

Time averaging
..............

Other Operations
----------------

EOFs, correlation, and regression analysis
..........................................

include lag correlation

Integration, Differentiation, Interpolation and Smoothing
.........................................................

Composites
..........
