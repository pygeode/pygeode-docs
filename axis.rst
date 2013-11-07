*******************
Axis class overview
*******************

.. currentmodule:: pygeode

.. class:: Axis

An Axis is a one-dimensional array of values, representing some kind of coordinate.  For example, a ``Lat`` axis represents a set of latitudes over the globe.  Axes are a subclass of :class:`Var`, and can be used in the same contexts (such as arithmetic operations).  See :doc:`var` for the functionality inherited from the Var class.

Types of axes
-------------

The following is a (non-exhaustive) list of axes that are built into PyGeode:

  ================     ================================================
  Axis subclass        Description
  ================     ================================================
  ``Lat``              Latitude (degrees)
  ``Lon``              Longitude (degrees)
  ``Pres``             Pressure level (mbar)
  ``ZAxis``            Generic vertical coordinate
  ``StandardTime``     Time axis, using a standard (Gregorian) calendar
  ``ModelTime365``     Time axis, using a 365-day calendar
  ``ModelTime360``     Time axis, using a 360-day calendar
  ``Yearless``         Time axis, without a calendar
  ================     ================================================

  If PyGeode doesn't have a built-in representation of an axis that your input data uses, it will default to a generic ``Axis`` object, with no additional context on what that axis represents.  To get around this, you can always define your own :ref:`custom<axis.custom>` axis, and force your Var to use it through :meth:`Var.replace_axes`.

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

Useful attributes
-----------------

In addition to the :attr:`~Var.atts` inherited from the :class:`Var` class, axes have a few extra attributes listed below:

.. attribute:: Axis.formatstr

  The format to apply to the axis values when displaying on the screen.  See the Python documentation on `String Formatting <http://docs.python.org/library/stdtypes.html#string-formatting>`_ for the options available.

  If the axis needs a more complicated format (that changes depending on the value), it may also define a :meth:`~Axis.formatvalue` method to explicitly convert each value to a string.  For example, the ``Lat`` axis uses a *formatvalue* method to append an 'N' or 'S' to the latitudes, depending on the sign of the value.

.. attribute:: Axis.plottitle

  A string to display on plot axes.  Usually more verbose than the axis's :attr:`~Var.name` attribute.

.. attribute:: Axis.plotscale

  ``'linear'`` for a linear plot scale, ``'log'`` for a logarithmic plot scale.

.. attribute:: Axis.plotorder

  The order of the values when plotting.  ``1`` = increasing from left to right, ``-1`` = decreasing.

**Note:** Due to current limitations in PyGeode, modifications to these attributes may be lost if you do further work on the axis (e.g. slicing, concatenation, etc.).  It will revert back to the default class values.  For example:
  >>> from pygeode import Lat
  >>> x = Lat([10,20,30])
  >>> print x
  lat <Lat>      :  10 N to 30 N (3 values)
  >>> x.formatstr = '%d deg'
  >>> print x
  lat <Lat>      :  10 deg N to 30 deg N (3 values)
  >>> #               ^^^ yay!
  >>> print x(lat=(10,20))
  lat <Lat>      :  10 N to 20 N (2 values)
  >>> #               ^^^ wtf?!

To get around this, make your changes to the class itself.  As an added benefit, *all* axes of this class will have your changes applied consistently:
  >>> from pygeode import Lat
  >>> x = Lat([10,20,30])
  >>> print x
  lat <Lat>      :  10 N to 30 N (3 values)
  >>> #  change this ^^^  on all latitude axes:
  >>> Lat.formatstr = '%d deg'
  >>> print x
  lat <Lat>      :  10 deg N to 30 deg N (3 values)
  >>> print x(lat=(10,20))    # check if the changes 'stick'
  lat <Lat>      :  10 deg N to 20 deg N (2 values)
  >>> y = Lat([40,50,60])     # will work on all Lat axes now.
  >>> print y
  lat <Lat>      :  40 deg N to 60 deg N (3 values)

Useful methods
--------------

.. automethod:: Axis.sorted

.. automethod:: Axis.argsort

Axis Classes
------------

.. autoclass:: Lon

.. autoclass:: Lat

.. autoclass:: StandardTime

.. autoclass:: ModelTime365

.. autoclass:: ModelTime360

.. autoclass:: Yearless
