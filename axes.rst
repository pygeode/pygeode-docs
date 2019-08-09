*******************
Axis class overview
*******************

.. currentmodule:: pygeode

An Axis is a one-dimensional array of values, representing some kind of
coordinate.  For example, a ``Lat`` axis represents a set of latitudes over the
globe.  Axes are a subclass of :class:`Var`, and can be treated as such for many purposes
(such as arithmetic operations), though they have some specific behaviour, including
the fact that their values are always explicitly loaded into memory. 

In practice the :class:`Axis` class is rarely instantiated directly; one of its subclasses 
are typically used to represent a dimension of a particular type. 

Types of axes
-------------

The following is a (non-exhaustive) list of more commonly used axes built into PyGeode:

.. autosummary::
  :nosignatures:

  NamedAxis
  Lon
  Lat
  Height
  Pres
  Hybrid
  StandardTime
  ModelTime365
  ModelTime360
  Yearless
  NonCoordinateAxis

If PyGeode doesn't have a built-in representation of an axis that your input
data uses, it will default to a generic  :class:`NamedAxis` object, with no additional
context on what that axis represents.  To get around this, you can always
define your own :ref:`custom<axis.custom>` axis, and force your Var to use it
through :meth:`Var.replace_axes` or when importing from a data file.

In addition to the members listed below, :class:`Axis` objects inherit methods from
the :class:`Var` class; see :doc:`var` for this functionality.

.. class:: Axis

  Inherits from :class:`Var`

  .. rubric:: Generic attributes

  .. autosummary::

    Axis.auxarrays
    Axis.auxatts
    Axis.rtol

  .. rubric:: Generic Axis methods

  .. autosummary::

    Axis.__init__
    Axis.argsort
    Axis.auxasvar
    Axis.rename
    Axis.sorted
    Axis.str_as_val

  .. rubric:: Formatting and Plotting

  .. autosummary::

    Axis.formatstr
    Axis.formatter
    Axis.locator
    Axis.plotatts

  .. rubric:: Internal calls

  .. autosummary::

    Axis.__call__
    Axis._getitem_asvar
    Axis.class_has_alias
    Axis.isparentof
    Axis.map_to

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
  >>> print(sza)
  sza_axis <SZA_Axis>:  20.1 to 20.5 (5 values)

A more customized version:

  >>> class SZA_Axis (Axis):
  ...   name = "sza"
  ...   units = "degrees"
  ...
  >>> sza = SZA_Axis ([20.1, 20.2, 20.3, 20.4, 20.5])
  >>> print(sza)
  sza <SZA_Axis> :  20.1 degrees to 20.5 degrees (5 values)

If you think your axis will be useful to others, please let us know, and we may include it in future versions.

Aspects of customizing an axis:

  * Defining its name
  * Customize how values are formatted as strings
  * Customize how strings are parsed into values
  * Customize matplotlib formatting and tick positioning
  * Customize CF-metadata encoding and decoding

.. toctree::
  :hidden:

  axis
  namedaxis
  horizontalaxes
  verticalaxes
  timeaxes

