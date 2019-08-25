******************
Var class overview
******************

.. currentmodule:: pygeode


.. commented out
  The Var class is at the centre of the PyGeode library. The Var module itself
  defines the core functionality of the var class, mostly having to do with the
  metadata of the grid structure and data type. Much of its useful functionality
  comes from extensions defined in other modules, these are added as hooks to
  avoid circular references when importing. A list of such hooks are included
  below, detailed references can be found by following the links.

In PyGeode, all gridded data is represented by Var objects.  They can be
thought of as :ref:`numpy <arrays.ndarray>` arrays, which have been further
abstracted in the following ways:

  * They can have a :attr:`name <Var.name>`, and :attr:`other <Var.atts>` useful metadata associated with them
  * Each array dimension has an associated :class:`~Axis` object (a special type of Var), containing the coordinate values.
  * The array values are not immediately loaded into memory.  Instead, the Var object knows where to find its values if it needs them, and will only bother to retrieve the values if something else is explicitly requesting them.
  * Similarly, operations on the data are not performed immediately.  Instead, a *new* Var object is constructed, encapsulating the input Vars and the operation.  If any of that data is ever requested, then the corresponding input data is retrieved, and *only then* is the operation performed.

.. class:: Var

  .. autosummary::

    Var.__init__

  .. rubric:: Useful attributes

  .. autosummary::

    Var.name
    Var.axes
    Var.naxes
    Var.shape
    Var.size
    Var.atts
    Var.dtype
    Var.units

  :doc:`var.get`

  .. autosummary::

    Var.get
    Var.__getitem__
    Var.load

  :doc:`varquery`

  .. autosummary::

    Var.hasaxis
    Var.whichaxis
    Var.getaxis
    Var.getweights

  .. _varops-list:

  :doc:`varops`

  .. autosummary::

    Var.__call__
    Var.slice
    Var._getitem_asvar
    Var.squeeze
    Var.extend
    Var.transpose
    Var.sorted
    Var.replace_axes
    Var.rename
    Var.rename_axes
    Var.fill
    Var.unfill
    Var.as_type

  .. _reduce-list:

  :doc:`reduce`

  .. autosummary::

    Var.mean
    Var.nanmean
    Var.sum
    Var.nansum
    Var.stdev
    Var.nanstdev
    Var.variance
    Var.nanvariance
    Var.min
    Var.nanmin
    Var.max
    Var.nanmax
    Var.argmin
    Var.argmax

  :doc:`var.arith`

    ==========  ===================      ===========================
    Operation   Method                   Description
    ==========  ===================      ===========================
    ``x + y``   :func:`Var.__add__`      Element-wise addition
    ``x - y``   :func:`Var.__sub__`      Element-wise subtraction
    ``x * y``   :func:`Var.__mul__`      Element-wise multiplication
    ``x / y``   :func:`Var.__div__`      Element-wise division
    ``x ** y``  :func:`Var.__pow__`      Exponentiation
    ``abs(x)``  :func:`Var.__abs__`      Absolute value
    ``-x``      :func:`Var.__neg__`      Negation 
    ``+x``      :func:`Var.__pos__`      Null operation
    ``x % t``   :func:`Var.__mod__`      Modulo
    ``x < y``   :func:`Var.__lt__`       ``True`` where ``x < y``
    ``x <= y``  :func:`Var.__le__`       ``True`` where ``x <= y``
    ``x > y``   :func:`Var.__gt__`       ``True`` where ``x > y``
    ``x >= y``  :func:`Var.__ge__`       ``True`` where ``x >= y``
    ``x == y``  :func:`Var.__eq__`       ``True`` where ``x == y``
    ``x != y``  :func:`Var.__ne__`       ``True`` where ``x != y``
    ==========  ===================      ===========================

  :doc:`ufunc`

  .. autosummary::

    Var.sign
    Var.exp
    Var.log
    Var.log10
    Var.cos
    Var.sin
    Var.tan
    Var.cosd
    Var.sind
    Var.tand
    Var.sinh
    Var.cosh
    Var.tanh
    Var.arcsin
    Var.arccos
    Var.arctan
    Var.arcsind
    Var.arccosd
    Var.arctand
    Var.arcsinh
    Var.arccosh
    Var.arctanh
    Var.sqrt
    Var.absolute
    Var.nan_to_num
    Var.real
    Var.imag
    Var.angle
    Var.conj
    Var.clip

  :doc:`var.other`

  .. autosummary::

    Var.diff
    Var.deriv
    Var.integrate
    Var.interpolate 
    Var.smooth
    Var.fft_smooth
    Var.composite
    Var.flatten
    Var.lag

  .. rubric:: Formatting and plotting operations

  .. autosummary::

    Var.plotatts
    Var.formatstr
    Var.formatvalue
    Var.formatter
    Var.locator

.. automethod:: Var.__init__

.. autoattribute:: Var.name
    :annotation: string

.. autoattribute:: Var.axes
    :annotation: tuple of Axis classes

.. autoattribute:: Var.naxes
    :annotation: integer

.. autoattribute:: Var.shape
    :annotation: tuple

.. autoattribute:: Var.size
    :annotation: integer

.. autoattribute:: Var.atts
    :annotation: dictionary

.. autoattribute:: Var.dtype
    :annotation: numpy dtype

.. autoattribute:: Var.units
    :annotation: string

.. autoattribute:: Var.plotatts
    :annotation: dictionary

.. autoattribute:: Var.formatstr
    :annotation: string

.. automethod:: Var.formatvalue

.. automethod:: Var.formatter

.. automethod:: Var.locator

.. toctree::
  :maxdepth: 2
  :hidden:

  varquery
  var.get
  var.arith
  ufunc
  reduce
  varops
  var.other

..
  intgr
  diff
  deriv
  smooth
  interpolate
  composite
