*******************
Axis class overview
*******************

.. currentmodule:: pygeode

An Axis is a one-dimensional array of values, representing some kind of
coordinate.  For example, a ``Lat`` axis represents a set of latitudes over the
globe.  Axes are a subclass of :class:`Var`, and can be used in the same
contexts (such as arithmetic operations).  See :doc:`var` for the functionality
inherited from the :class:`Var` class.

.. class:: Axis

  Inherits from :class:`Var`

.. rubric:: Generic Axis Methods

.. autosummary::

  Axis.__init__
  Axis.__call__
  Axis.sorted
  Axis.argsort

.. rubric:: Useful attributes

.. autosummary::

  Axis.rtol
  Axis.auxarrays
  Axis.auxatts

Types of axes
-------------

The following is a (non-exhaustive) list of more commonly used axes built into PyGeode:

  =====================     ================================================
  Axis subclass             Description
  =====================     ================================================
  :class:`NamedAxis`        A named (but otherwise arbitrary) dimension
  :class:`Lon`              Longitude
  :class:`Lat`              Latitude
  :class:`ZAxis`            A parent class for vertical axes
  :class:`Height`           Geometric height
  :class:`Pres`             Pressure height
  :class:`Hybrid`           Hybrid pressure height
  :class:`StandardTime`     Time axis, using a standard (Gregorian) calendar
  :class:`ModelTime365`     Time axis, using a 365-day calendar
  :class:`ModelTime360`     Time axis, using a 360-day calendar
  :class:`Yearless`         Time axis, without a calendar
  =====================     ================================================

If PyGeode doesn't have a built-in representation of an axis that your input
data uses, it will default to a generic ``Axis`` object, with no additional
context on what that axis represents.  To get around this, you can always
define your own :ref:`custom<axis.custom>` axis, and force your Var to use it
through :meth:`Var.replace_axes`.

.. class:: NamedAxis

  Inherits from :class:`Axis`

.. autosummary:: 

  NamedAxis.__init__
  
.. class:: XAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing horizontal coordinates, plotted by default on
  the horizontal axis in contour plots and line plots. No custom methods.

.. class:: YAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing horizontal coordinates, plotted by
  default on the horizontal axis in line plots, but on the vertical in contour
  plots. No custom methods.

.. class:: ZAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing vertical coordinates, plotted by default on
  the vertical axis in line plots and in contour plots. No custom methods.

.. class:: TAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing time coordinates. No custom methods.

.. rubric:: Horizontal coordinate axes

.. class:: Lon

  Inherits from :class:`YAxis`

  Represents longitude (in degrees)

.. autosummary:: 

  Lon.__init__
  Lon.formatvalue
  Lon.locator
  regularlon

.. class:: Lat

  Inherits from :class:`YAxis`

  Represents latitude (in degrees)

.. autosummary:: 

  Lat.__init__
  Lat.formatvalue
  Lat.locator
  regularlat
  gausslat

.. rubric:: Vertical coordinate axes

.. class:: Height

  Inherits from :class:`ZAxis`

  Represents a geometric height

.. class:: Pres

  Inherits from :class:`ZAxis`

  Represents a pressure vertical coordinate.

.. autosummary:: 

  Pres.logPAxis
  Pres.locator
  Pres.formatvalue

.. class:: Hybrid

  Inherits from :class:`ZAxis`

  Represents a hybridized pressure coordinate, of the form :math:`p(\eta) = A(\eta) p_0 + B(\eta) p_s`.

  Auxilliary arrays: ``A`` and ``B``

.. autosummary:: 

  Hybrid.__init__
  Hybrid.locator

.. currentmodule:: pygeode.timeaxis

.. class:: Time

  Inherits from :class:`~pygeode.TAxis`

  Parent class for axes representing times.

.. autosummary:: 

  Time.__init__
  Time.formatter
  Time.locator

.. class:: CalendarTime

  Inherits from :class:`Time`

  Parent class for time axes with an associated calendar.

.. autosummary:: 

  CalendarTime.__init__
  CalendarTime.days_in_month
  CalendarTime.formatvalue
  CalendarTime.str_as_val
  CalendarTime.val_as_date
  CalendarTime.date_as_val

.. currentmodule:: pygeode

.. class:: StandardTime

  Inherits from :class:`~timeaxis.CalendarTime`

  Time axis representing the standard calendar.

.. class:: ModelTime365

  Inherits from :class:`~timeaxis.CalendarTime`

  Time axis representing a calendar with a 365 day year.

.. class:: ModelTime360

  Inherits from :class:`~timeaxis.CalendarTime`

  Time axis representing a calendar with a 360 day year.

.. class:: Yearless

  Inherits from :class:`~timeaxis.CalendarTime`

  Time axis representing a calendar that marks days independent of years and months.

.. autosummary:: 

  Yearless.__init__
  Yearless.days_in_month

.. _axis.custom:

Defining a new type of axis
---------------------------

It's impossible (or at least improbable) for the standard PyGeode package to include every possible type of axis that people may want.  However, it's fairly straight-forward to define your own custom axis.  Simply define a new class, as a subclass of :class:`Axis`.

For example, suppose one of the dimensions of your data is solar zenith angle (SZA).  You can make a simple Axis representation as follows:
  >>> from pygeode import Axis
  >>> class SZA_Axis (Axis): pass
  ...

You can now use it like any other axis:
  >>> sza = SZA_Axis ([20.1, 20.2, 20.3, 20.4, 20.5])
  >>> print sza
  sza_axis <SZA_Axis>:  20.1 to 20.5 (5 values)

A more customized version:
  >>> class SZA_Axis (Axis):
  ...   name = "sza"
  ...   units = "degrees"
  ...
  >>> sza = SZA_Axis ([20.1, 20.2, 20.3, 20.4, 20.5])
  >>> print sza
  sza <SZA_Axis> :  20.1 degrees to 20.5 degrees (5 values)

If you think your axis will be useful to others, please let us know, and we may include it in future versions.

.. toctree::
  :hidden:

  axis
