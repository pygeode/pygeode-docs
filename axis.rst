*********************
Axis class reference
*********************

.. currentmodule:: pygeode

.. class:: Axis
  :noindex:

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

.. automethod:: Axis.sorted

.. automethod:: Axis.argsort

.. class:: NamedAxis
  :noindex:

.. automethod:: NamedAxis.__init__
  
.. class:: Lon
  :noindex:

.. automethod:: Lon.__init__

.. automethod:: Lon.formatvalue

.. automethod:: Lon.locator

.. autofunction:: regularlon

.. class:: Lat
  :noindex:

.. automethod:: Lat.__init__

.. automethod:: Lat.formatvalue

.. automethod:: Lat.locator

.. autofunction:: regularlat

.. autofunction:: gausslat

.. class:: Pres
  :noindex:

.. automethod:: Pres.logPAxis

.. automethod:: Pres.formatvalue

.. automethod:: Pres.locator

.. class:: Hybrid
  :noindex:

.. automethod:: Hybrid.__init__

.. automethod:: Hybrid.locator

.. currentmodule:: pygeode.timeaxis

.. class:: Time
  :noindex:

.. automethod:: Time.__init__

.. automethod:: Time.formatter

.. automethod:: Time.locator

.. class:: CalendarTime
  :noindex:

.. automethod:: CalendarTime.__init__

.. automethod:: CalendarTime.days_in_month

.. automethod:: CalendarTime.formatvalue

.. automethod:: CalendarTime.str_as_val

.. automethod:: CalendarTime.val_as_date

.. automethod:: CalendarTime.date_as_val

.. currentmodule:: pygeode

.. class:: Yearless
  :noindex:

.. automethod:: Yearless.__init__

.. automethod:: Yearless.days_in_month

