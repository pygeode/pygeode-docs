********************************
Horizonal axis objects reference
********************************

.. currentmodule:: pygeode

.. class:: XAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing horizontal coordinates, plotted by default on
  the horizontal axis in contour plots and line plots. No new or overridden methods.

.. class:: YAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing horizontal coordinates, plotted by
  default on the horizontal axis in line plots, but on the vertical in contour
  plots. No new or overridden methods.

.. class:: Lon

  Inherits from :class:`YAxis`

  Represents longitude (in degrees East by default). Regular longitude grids
  can be created with the helper method :func:`regularlon`.

  .. rubric:: New and overridden methods

  .. autosummary:: 

    Lon.__init__
    Lon.formatvalue
    Lon.locator

.. class:: Lat

  Inherits from :class:`YAxis`

  Represents latitude (in degrees North by default). Evenly spaced and gaussian
  latitude grids can be created with the helper functions
  :func:`regularlat` and :func:`gausslat`.

  .. rubric:: New and overridden methods

  .. autosummary:: 

    Lat.__init__
    Lat.formatvalue
    Lat.locator

.. rubric:: Utility functions

.. autosummary:: 

  regularlon
  rotatelon
  regularlat
  gausslat

.. automethod:: Lon.__init__

.. automethod:: Lon.formatvalue

.. automethod:: Lon.locator

.. autofunction:: regularlon

.. autofunction:: rotatelon

.. automethod:: Lat.__init__

.. automethod:: Lat.formatvalue

.. automethod:: Lat.locator

.. autofunction:: regularlat

.. autofunction:: gausslat
