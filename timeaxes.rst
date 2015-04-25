***************************
Time axes objects reference
***************************

.. currentmodule:: pygeode

.. class:: TAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing time coordinates, plotted by default on
  the horizontal axis in line plots and in contour plots. No new or overridden methods.

.. currentmodule:: pygeode.timeaxis

.. class:: Time

  Inherits from :class:`TAxis`

  Parent class for axes representing times.

.. rubric:: New and overridden methods

.. autosummary:: 

  Time.__init__
  Time.formatter
  Time.locator
  Time.map_to

.. class:: CalendarTime

  Inherits from :class:`Time`

  Parent class for time axes with an associated calendar.

.. rubric:: New and overridden methods

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

  .. rubric:: New and overridden methods

  .. autosummary:: 

    Yearless.__init__
    Yearless.days_in_month

.. currentmodule:: pygeode.timeaxis

.. automethod:: Time.__init__

.. automethod:: Time.formatter

.. automethod:: Time.locator

.. automethod:: Time.map_to

.. automethod:: CalendarTime.__init__

.. automethod:: CalendarTime.days_in_month

.. automethod:: CalendarTime.formatvalue

.. automethod:: CalendarTime.str_as_val

.. automethod:: CalendarTime.val_as_date

.. automethod:: CalendarTime.date_as_val

.. currentmodule:: pygeode

.. automethod:: Yearless.__init__

.. automethod:: Yearless.days_in_month

