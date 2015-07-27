===================================
Axis Reductions
===================================

These functions compute summary statistics over specified axes of a variable.
In general multiple axes can be reduced over at the same time. Many of them
wrap similar numpy functions, though they are also capable of performing these
operations on datasets too large to fit in memory. Most operations have two
versions, one which computes the reduction including every element without
checking for the presence of NaNs, and one which ignores any element which is a NaN, adjusting
the relevant normalization

.. currentmodule:: pygeode

.. automethod:: Var.mean
.. automethod:: Var.nanmean
.. automethod:: Var.sum
.. automethod:: Var.nansum
.. automethod:: Var.stdev
.. automethod:: Var.nanstdev
.. automethod:: Var.variance
.. automethod:: Var.nanvariance
.. automethod:: Var.min
.. automethod:: Var.nanmin
.. automethod:: Var.max
.. automethod:: Var.nanmax
.. automethod:: Var.argmin
.. automethod:: Var.argmax


**See Also:**
  :doc:`var`

  :ref:`arrays.ndarray.calculation`  (external Numpy documentation)
