==============
Reference
==============

.. currentmodule:: pygeode

Fundamental PyGeode objects
-------------------------------------

:doc:`var`
  The fundamental class for representing a field on a geophysical grid, and
  many of the basic operations. 

:doc:`axes`
  The fundamental class :class:`Axis` for representing one dimension of the geophysical grid,
  and a description of all built-in types of :class:`Axis` objects. 

:doc:`dataset`
  A collection class to manage a set of :class:`Var` objects.

Plotting package
-------------------------------------
:doc:`plot`
  A module for plotting :class:`Var` objects.

Top-level analysis
-------------------------------------

:doc:`toplevel`
  File input and output routines. 

:doc:`timeutils`
  A module of routines for working with time axes

:doc:`climat`
  A module of routines for computing climatological means and variances.

:doc:`eof` 
  A module of routines for computing empirical orthogonal functions, singular
  value decompositions, and related variance decompositions.

:doc:`stats` 
  A module of routines for computing correlations, regressions, and computing statistical tests.

Under the hood
-------------------------------------

:doc:`view`
  A helper class for mapping subsets of variables 

.. toctree::
  :hidden:

  var
  axes
  dataset
  plot
  toplevel
  timeutils
  climat
  stats
  eof
  view
