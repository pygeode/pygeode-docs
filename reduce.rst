===================================
Axis Reductions
===================================

These functions compute summary statistics over subdomains of a variable. Many of them wrap similar
numpy functions, though they are also capable of performing these operations on datasets too large
to fit in memory.

.. currentmodule:: pygeode

.. automethod:: Var.mean
.. automethod:: Var.sum
.. automethod:: Var.stdev
.. automethod:: Var.variance
.. automethod:: Var.nanmean
.. automethod:: Var.nansum
.. automethod:: Var.nanstdev
.. automethod:: Var.nanvariance
.. automethod:: Var.min
.. automethod:: Var.max
.. automethod:: Var.argmin
.. automethod:: Var.argmax


**See Also:**
  :doc:`var`

  :ref:`arrays.ndarray.calculation`  (external Numpy documentation)
