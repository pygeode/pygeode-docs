Advanced Variable Operations
============================

.. currentmodule:: pygeode

Time Axis Operations
--------------------

PyGeode recognizes many types of geophysical dimensions, some of which we've
already seen in these tutorials. By far the most complicated of these are those
axes representing the time dimension. PyGeode has a reasonably sophisticated
time axis, which is aware of four main types of Calandars - the standard Julian
calendar, a 365-day calendar, a 360-day calendar, and a yearless calendar,
which might better be described as a time axis with no calendar at all. 

These will often be created automatically from datasets with CF-compliant
metadata (of which PyGeode is aware, see ??); but they can also be created
manually (see ??). 

-select by year, month, day
-Split/Join

Internally these are represented using offsets from a reference date - the
refer
  
Climatological statistics
-------------------------

climatology? others?

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

