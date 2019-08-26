*********************
Axis class reference
*********************

.. currentmodule:: pygeode

.. attribute:: Axis.rtol 
  :annotation: float

  Relative tolerance for identifying two values for this axis as the same point. Set automatically
  in Axis::__init__ but if this is too large for a given application this can be the source
  of unexpected errors. Setting this parameter to a new value on the Axis objects in question may 
  resolve these issues.

.. attribute:: Axis.formatstr
  :annotation: string

  The format to apply to the axis values when displaying on the screen.  See
  the Python documentation on `String Formatting
  <http://docs.python.org/library/stdtypes.html#string-formatting>`_ for the
  options available.

  If the axis needs a more complicated format (that changes depending on the
  value), it may also define a :meth:`~Axis.formatvalue` method to explicitly
  convert each value to a string.  For example, the ``Lat`` axis uses a
  *formatvalue* method to append an 'N' or 'S' to the latitudes, depending on
  the sign of the value.

.. autoattribute:: Axis.auxatts
  :annotation: dictionary

.. attribute:: Axis.auxarrays
  :annotation: dictionary

  A dictionary of 1D numpy arrays with the same length as the axis that carry auxiliary
  data associated with each element of the axis. These data need not be unique; for instance, 
  the values of time axes (e.g. :class:`StandardTime`) are given as offsets from a reference
  date, while they have auxarrays for the year, month, day, etc. Many elements of the time axis
  might have same value in the corresponding 'month' auxiliary array. These can be used
  to select by keyword. 

  See Also
  ========
  auxasvar
  Var.__call__

.. autoattribute:: Axis.plotatts
  :annotation: dictionary

**Note:** Due to current limitations in PyGeode, modifications to these
attributes may be lost if you do further work on the axis (e.g. slicing,
concatenation, etc.).  It will revert back to the default class values.  For
example:

  >>> import pygeode as pyg
  >>> x = pyg.Lat([10,20,30])
  >>> print(x)
  lat <Lat>      :  10 N to 30 N (3 values)
  >>> x.formatstr = '%d deg N'
  >>> print(x)
  lat <Lat>      :  10 deg N to 30 deg N (3 values)
  >>> #               ^^^ yay!
  >>> print(x(lat=(10,20))) 
  lat <Lat>      :  10 N to 20 N (2 values)
  >>> #               ^^^ wtf?!

At the moment there isn't a great way to address this beyond
changing the configuration file ``pygrc``.

.. automethod:: Axis.__init__

.. automethod:: Axis.argsort

.. automethod:: Axis.auxasvar

.. automethod:: Axis.formatter

.. automethod:: Axis.locator

.. automethod:: Axis.rename

.. automethod:: Axis.sorted

.. automethod:: Axis.str_as_val

.. automethod:: Axis.__call__

.. automethod:: Axis._getitem_asvar

.. automethod:: Axis.class_has_alias

.. automethod:: Axis.isparentof

.. automethod:: Axis.map_to
