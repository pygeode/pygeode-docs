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

  .. rubric:: Useful attributes

  .. autosummary::

    Var.name
    Var.axes
    Var.atts
    Var.dtype

  :doc:`var.get`

  .. autosummary::

    Var.get
    Var.__getitem__

  :doc:`varquery`

  .. autosummary::

    Var.hasaxis
    Var.whichaxis
    Var.getaxis

  :doc:`varops`

  .. autosummary::

    Var.__call__
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

  :doc:`reduce`

  .. autosummary::

    Var.mean
    Var.sum
    Var.stdev
    Var.variance
    Var.nanmean
    Var.nansum
    Var.nanstdev
    Var.nanvariance
    Var.min
    Var.max
    Var.argmin
    Var.argmax

  :doc:`var.arith`

    ==========  ===================      ======================
    Operation   Method                   Description
    ==========  ===================      ======================
    ``x + y``   :func:`Var.__add__`      Binary addition      
    ``x - y``   :func:`Var.__sub__`      Binary subtraction
    ``x * y``   :func:`Var.__mul__`      Binary multiplication
    ``x / y``   :func:`Var.__div__`      Binary division
    ``x ** y``  :func:`Var.__pow__`      Exponentiation
    ``abs(x)``  :func:`Var.__abs__`      Absolute value
    ``-x``      :func:`Var.__neg__`      Negation 
    ``+x``      :func:`Var.__pos__`      Null operation
    ``x % t``   :func:`Var.__mod__`      Modulo
    ``x < y``   :func:`Var.__lt__`
    ``x <= y``  :func:`Var.__le__`
    ``x > y``   :func:`Var.__gt__`
    ``x >= y``  :func:`Var.__ge__`
    ``x == y``  :func:`Var.__eq__`
    ``x != y``  :func:`Var.__ne__`
    ==========  ===================      ======================

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

  :doc:`var.other`

  .. autosummary::

    Var.deriv
    Var.integrate
    Var.interpolate 
    Var.smooth

  .. rubric:: Formatting and plotting operations

  .. autosummary::

    Var.formatstr
    Var.formatvalue
    Var.formatter
    Var.locator

.. attribute:: Var.name

    A description of the variable (may not be set).  Usually determined at the
    data source (e.g. input file), and may be used to identify the variable
    when saving to an output file.

.. attribute:: Var.axes

    The axes of the variable, as a ``tuple``. See :doc:`axes`.

.. attribute:: Var.atts

    A ``dict`` of metadata associated with the variable (if applicable).

.. attribute:: Var.dtype

    The type of numeric data that the Var represents.

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
  deriv
  smooth
  interpolate
  composite
