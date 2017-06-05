**************************
NamedAxis object reference
**************************

.. currentmodule:: pygeode

.. class:: NamedAxis

  Inherits from :class:`Axis`

  Generic axis identified by the instances name. Unlike other axes classes,
  NamedAxis objects must have the same name in order for two axes to be mapped 
  to one another. 

  .. rubric:: New or Overridden Methods

  .. autosummary:: 

    NamedAxis.__init__
    NamedAxis.map_to

.. automethod:: NamedAxis.__init__

.. automethod:: NamedAxis.map_to
  
.. class:: NonCoordinateAxis

  Inherits from :class:`Axis`

  An axis for non-coordinate dimensions (e.g. categorical data such as stations, etc.). 

  .. rubric:: New or Overridden Methods

  .. autosummary:: 

    NonCoordinateAxis.__init__
    NonCoordinateAxis.map_to
    NonCoordinateAxis.str_as_val
    NonCoordinateAxis.formatvalue
    NonCoordinateAxis.__eq__

.. automethod:: NonCoordinateAxis.__init__

.. automethod:: NonCoordinateAxis.map_to

.. automethod:: NonCoordinateAxis.str_as_val

.. automethod:: NonCoordinateAxis.formatvalue

.. automethod:: NonCoordinateAxis.__eq__
