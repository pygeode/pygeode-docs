===================================
Axis Reductions
===================================

These functions compute summary statistics over subdomains of a variable. Many of them wrap similar
numpy functions, though they are also capable of performing these operations on datasets too large
to fit in memory.

See Also:
  :ref:`arrays.ndarray.calculation`  (external Numpy documentation)

.. currentmodule:: pygeode

.. automethod:: Var.mean
.. automethod:: Var.nanmean
.. automethod:: Var.sum
.. automethod:: Var.nansum

**See Also:**
  :doc:`var`
