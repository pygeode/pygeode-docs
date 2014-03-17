===================================
Element-wise math
===================================

.. currentmodule:: pygeode

See Also:

  :doc:`var.arith` (simple arithmetic on PyGeode variables)

  :ref:`ufuncs`  (external Numpy documentation)

The majority of these functions are wrappers to the corresponding Numpy
functions. They are augmented to handle PyGeode variables, and, in the case of
functions that take a single argument, are available in two forms, as functions
in the top-level PyGeode namespace, or as members of the :class:`Var` class.

.. autosummary:: 

  sign
  exp
  log
  log10
  cos
  sin
  tan
  cosd
  sind
  tand
  sinh
  cosh
  tanh
  arcsin
  arccos
  arctan
  arctan2
  arcsind
  arccosd
  arctand
  arctand2
  arcsinh
  arccosh
  arctanh
  sqrt
  absolute
  nan_to_num
  real
  imag
  angle

.. autofunction:: sign

.. automethod:: Var.sign

.. autofunction:: exp

.. automethod:: Var.exp

.. autofunction:: log

.. automethod:: Var.log

.. autofunction:: log10

.. automethod:: Var.log10

.. autofunction:: cos

.. automethod:: Var.cos

.. autofunction:: sin

.. automethod:: Var.sin

.. autofunction:: tan

.. automethod:: Var.tan

.. autofunction:: cosd

.. automethod:: Var.cosd

.. autofunction:: sind

.. automethod:: Var.sind

.. autofunction:: tand

.. automethod:: Var.tand

.. autofunction:: sinh

.. automethod:: Var.sinh

.. autofunction:: cosh

.. automethod:: Var.cosh

.. autofunction:: tanh

.. automethod:: Var.tanh

.. autofunction:: arcsin

.. automethod:: Var.arcsin

.. autofunction:: arccos

.. automethod:: Var.arccos

.. autofunction:: arctan

.. automethod:: Var.arctan

.. autofunction:: arctan2

.. autofunction:: arcsind

.. automethod:: Var.arcsind

.. autofunction:: arccosd

.. automethod:: Var.arccosd

.. autofunction:: arctand

.. automethod:: Var.arctand

.. autofunction:: arctand2

.. autofunction:: arcsinh

.. automethod:: Var.arcsinh

.. autofunction:: arccosh

.. automethod:: Var.arccosh

.. autofunction:: arctanh

.. automethod:: Var.arctanh

.. autofunction:: sqrt

.. automethod:: Var.sqrt

.. autofunction:: absolute

.. automethod:: Var.absolute

.. autofunction:: nan_to_num

.. automethod:: Var.nan_to_num

.. autofunction:: real

.. automethod:: Var.real

.. autofunction:: imag

.. automethod:: Var.imag

.. autofunction:: angle

.. automethod:: Var.angle

