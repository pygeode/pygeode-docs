******************************
Vertical axes object reference
******************************

.. currentmodule:: pygeode

.. class:: ZAxis

  Inherits from :class:`Axis`

  Generic parent class for axes representing vertical coordinates, plotted by default on
  the vertical axis in line plots and in contour plots. No new or overridden methods.

.. class:: Height

  Inherits from :class:`ZAxis`

  Represents a geometric height. No new or overridden methods.

.. class:: Pres

  Inherits from :class:`ZAxis`

  Represents a pressure vertical coordinate.

.. rubric:: New and overridden methods

.. autosummary:: 

  Pres.logPAxis
  Pres.locator
  Pres.formatvalue

.. class:: Hybrid

  Inherits from :class:`ZAxis`

  Represents a hybridized pressure coordinate, of the form :math:`p(\eta) = A(\eta) p_0 + B(\eta) p_s`.

  Auxilliary arrays: ``A`` and ``B``

.. rubric:: New and overridden methods

.. autosummary:: 

  Hybrid.__init__
  Hybrid.locator

.. automethod:: Pres.logPAxis

.. automethod:: Pres.formatvalue

.. automethod:: Pres.locator

.. automethod:: Hybrid.__init__

.. automethod:: Hybrid.locator
