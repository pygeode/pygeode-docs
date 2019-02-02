.. currentmodule:: pygeode

Arithmetic Operations on Variables
==================================

These methods are called implicitly when any arithmetic operation is applied to a :class:`Var`.
The result is a new Var object, which will apply the operation to any incoming data requests.
The following is a table of all built-in Python arithmetic operations that are supported:

===================  ===============  ========================================
Method:              Example of use:  Returns:
===================  ===============  ========================================
:func:`Var.__add__`  ``x + y``        Sum of ``x`` and ``y``
:func:`Var.__sub__`  ``x - y``        Difference between ``x`` and ``y``
:func:`Var.__mul__`  ``x * y``        Product of ``x`` and ``y``
:func:`Var.__div__`  ``x / y``        Quotient of ``x`` and ``y``
:func:`Var.__pow__`  ``x ** y``       ``x`` to the power of ``y``
:func:`Var.__abs__`  ``abs(x)``       Absolute value of ``x``
:func:`Var.__neg__`  ``-x``           Negative of ``x``
:func:`Var.__pos__`  ``+x``           Positive of ``x``
:func:`Var.__mod__`  ``x % t``        ``x`` modulo ``t``
:func:`Var.__lt__`   ``x < y``        Mask where ``x`` is less than ``y``
:func:`Var.__le__`   ``x <= y``       Mask where ``x`` is not more than ``y``
:func:`Var.__gt__`   ``x > y``        Mask where ``x`` is more than ``y``
:func:`Var.__ge__`   ``x >= y``       Mask where ``x`` is not less than ``y``
:func:`Var.__eq__`   ``x == y``       Mask where ``x`` is equal to than ``y``
:func:`Var.__ne__`   ``x != y``       Mask where ``x`` is not equal to ``y``
===================  ===============  ========================================

**Axis rules for arithmetic:**

  When you use one of the 2-argument operations above, PyGeode tries to match
  the two sets of input axes, independant of their respective orders. The
  output axes are determined from the inputs using following algorithm:

  1. If one of the Vars contains all the input axes, then the output axes are
     exactly those axes, in that order.  No further checking is done.

  2. Otherwise, the axes from the first Var are prepended to the list of
     output axes.

  3. The axes of the second Var are checked, in order.  If the output from
     step 2 does not already contain an identical axis, then it is
     appended to the end of the output axes.

  In the above algorithm, two axes are considered to be identical if 1) they
  are the same type of axis (e.g. ``Lat``), and 2) they contain the same
  values.  If either of these criteria fail, then the axes will be considered
  distinct, and the output variable will contain both axes.

  A special case is the ``Time`` axis.  The criteria for matching are loosened
  to allow for time axes with the same range, but different internal
  paritioning.  For example, a standard time axis with daily values from
  *January 1, 2000* to *December 31, 2005* can be matched with a monthly time
  axis from *January 2000* to *December 2005*.  Similarly, both can be matched
  to a monthly climatological time axis from *January* to *December*.  For this
  case, the axis with the most values (i.e., the finer level of partitioning)
  will be used in the output.

Arithmetic operations between Vars and scalar values are allowed.  The scalar
would be treated as an array of repeated values, with the same shape and axes
as the Var argument.

However, operations between Vars and numpy arrays are not well defined, since
numpy arrays are missing crucial information about their axes (e.g. coordinate
values).

**See Also:**

  :doc:`var`

  :doc:`ufunc` (higher-level math on PyGeode variables)

Example
-------
Start with some 2D data:
  >>> from pygeode.tutorial import t1
  >>> print(t1.Temp)
  <Var 'Temp'>:
    Shape:  (lat,lon)  (32,64)
    Axes:
      lat <Lat>      :  85 S to 85 N (32 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {'units': 'K'}
    Type:  Var (dtype="float64")

Generate a time axis (say, every 6 hours starting at January 1, 2000)
  >>> import numpy as np
  >>> hour_values = np.arange(124) * 6
  >>> print(hour_values)
  [  0   6  12  18  24  30  36  42  48  54  60  66  72  78  84  90  96 102
   108 114 120 126 132 138 144 150 156 162 168 174 180 186 192 198 204 210
   216 222 228 234 240 246 252 258 264 270 276 282 288 294 300 306 312 318
   324 330 336 342 348 354 360 366 372 378 384 390 396 402 408 414 420 426
   432 438 444 450 456 462 468 474 480 486 492 498 504 510 516 522 528 534
   540 546 552 558 564 570 576 582 588 594 600 606 612 618 624 630 636 642
   648 654 660 666 672 678 684 690 696 702 708 714 720 726 732 738]
  >>> start_date = dict(year=2000,month=1,day=1,hour=0)
  >>> from pygeode import StandardTime
  >>> taxis = StandardTime(values=hour_values, units='hours', startdate=start_date)
  >>> print(taxis)
  time <StandardTime>:  Jan 1, 2000 00:00:00 to Jan 31, 2000 18:00:00 (124 values)

**1) Operation between a Var and a scalar**

Create a small linear temperature trend along the time axis.  Since our time axis is stored in units of 'hours', let's make a trend of 0.01 degrees per hour.
  >>> t_trend = taxis * 0.01
  >>> print(t_trend)
  <Var '(time*0.01)'>:
    Shape:  (time)  (124)
    Axes:
      time <StandardTime>:  Jan 1, 2000 00:00:00 to Jan 31, 2000 18:00:00 (124 values)
    Attributes:
      {}
    Type:  Mul_Var (dtype="float64")
  >>> print(t_trend.get())
  [ 0.    0.06  0.12  0.18  0.24  0.3   0.36  0.42  0.48  0.54  0.6   0.66
    0.72  0.78  0.84  0.9   0.96  1.02  1.08  1.14  1.2   1.26  1.32  1.38
    1.44  1.5   1.56  1.62  1.68  1.74  1.8   1.86  1.92  1.98  2.04  2.1
    2.16  2.22  2.28  2.34  2.4   2.46  2.52  2.58  2.64  2.7   2.76  2.82
    2.88  2.94  3.    3.06  3.12  3.18  3.24  3.3   3.36  3.42  3.48  3.54
    3.6   3.66  3.72  3.78  3.84  3.9   3.96  4.02  4.08  4.14  4.2   4.26
    4.32  4.38  4.44  4.5   4.56  4.62  4.68  4.74  4.8   4.86  4.92  4.98
    5.04  5.1   5.16  5.22  5.28  5.34  5.4   5.46  5.52  5.58  5.64  5.7
    5.76  5.82  5.88  5.94  6.    6.06  6.12  6.18  6.24  6.3   6.36  6.42
    6.48  6.54  6.6   6.66  6.72  6.78  6.84  6.9   6.96  7.02  7.08  7.14
    7.2   7.26  7.32  7.38]


**2) Operation between two Vars**

Add this to our 2D data, to get a 3D field.  Use the time-dependant data as the left argument of the addition, so that the time axis is our first (leftmost) axis for the output.
  >>> mydata = t_trend + t1.Temp
  >>> print(mydata)
  <Var '((time*0.01)+Temp)'>:
    Shape:  (time,lat,lon)  (124,32,64)
    Axes:
      time <StandardTime>:  Jan 1, 2000 00:00:00 to Jan 31, 2000 18:00:00 (124 values)
      lat <Lat>      :  85 S to 85 N (32 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {}
    Type:  Add_Var (dtype="float64")

Give this variable a better name (so it's more easily identifiable if we save it to a file):
  >>> mydata = mydata.rename('Temp')
  >>> print(mydata)
  <Var 'Temp'>:
    Shape:  (time,lat,lon)  (124,32,64)
    Axes:
      time <StandardTime>:  Jan 1, 2000 00:00:00 to Jan 31, 2000 18:00:00 (124 values)
      lat <Lat>      :  85 S to 85 N (32 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {'units': 'K'}
    Type:  RenamedVar (dtype="float64")


