******************
Var class overview
******************

.. currentmodule:: pygeode

.. class:: Var

.. commented out
  The Var class is at the centre of the PyGeode library. The Var module itself
  defines the core functionality of the var class, mostly having to do with the
  metadata of the grid structure and data type. Much of its useful functionality
  comes from extensions defined in other modules, these are added as hooks to
  avoid circular references when importing. A list of such hooks are included
  below, detailed references can be found by following the links.

In PyGeode, all gridded data is represented by Var objects.  They can be thought of as :ref:`numpy <arrays.ndarray>` arrays, which have been further abstracted in the following ways:
  * They can have a :attr:`name <Var.name>`, and :attr:`other <Var.atts>` useful metadata associated with them
  * Each array dimension has an associated :class:`~Axis` object (a special type of Var), containing the coordinate values.
  * The array values are not immediately loaded into memory.  Instead, the Var object knows where to find its values if it needs them, and will only bother to retrieve the values if something else is explicitly requesting them.
  * Similarly, operations on the data are not performed immediately.  Instead, a *new* Var object is constructed, encapsulating the input Vars and the operation.  If any of that data is ever requested, then the corresponding input data is retrieved, and *only then* is the operation performed.

Useful attributes
-----------------

.. attribute:: Var.name

  A description of the variable (may not be set).  Usually determined at the data source (e.g. input file), and may be used to identify the variable when saving to an output file.

.. attribute:: Var.axes

  The axes of the variable, as a ``tuple``. See :doc:`axis`

.. attribute:: Var.atts

    A ``dict`` of metadata associated with the variable (if applicable).

.. attribute:: Var.dtype

    The type of numeric data that the Var represents.


Retrieving values
-----------------
:func:`Var.get`

Main article: :doc:`var.get`


Variable querying routines
--------------------------
:func:`Var.hasaxis`, :func:`Var.whichaxis`, :func:`Var.getaxis`, etc.

Main article: :doc:`varquery`


Array manipulation routines
---------------------------
:func:`Var.__call__`, :func:`Var.squeeze`, :func:`Var.extend`, :func:`Var.transpose`,
:func:`Var.sorted`, :func:`Var.replace_axes`,
:func:`Var.rename`, :func:`Var.rename_axes`, :func:`Var.fill`, :func:`Var.unfill`,
:func:`Var.as_type`

Main article: :doc:`varops`


Axis reduction routines
-----------------------
:func:`Var.mean`, :func:`Var.nanmean`, :func:`Var.sum`, :func:`Var.nansum`

Main article: :doc:`reduce`


Arithmetic (and boolean) operations
-----------------------------------
``+``, ``-``, ``*``, ``/``, ``**``, ``%``, ``<``, ``<=``, ``>``, ``>=``, ``==``, ``!=``

Main Article: :doc:`var.arith`


Unary functions
---------------
:func:`~Var.sign`, :func:`~Var.exp`, :func:`~Var.log`, :func:`~Var.log10`, :func:`~Var.cos`, 
:func:`~Var.sin`, :func:`~Var.tan`, :func:`~Var.cosd`, :func:`~Var.sind`, :func:`~Var.tand`,
:func:`~Var.cosh`, :func:`~Var.sinh`, :func:`~Var.tanh`, :func:`~Var.arccos`,
:func:`~Var.arcsin`, :func:`~Var.arctan`,
:func:`~Var.arccosd`, :func:`~Var.arcsind`, :func:`~Var.arctand`, :func:`~Var.arccosh`,
:func:`~Var.arcsinh`, :func:`~Var.arctanh`,
:func:`~Var.sqrt`, :func:`~Var.abs`, :func:`~Var.nan_to_num`, :func:`~Var.real`,
:func:`~Var.imag`, :func:`~Var.angle`

These are simple wrappers which apply the unary function to the current PyGeode variable.

See Also: :doc:`ufunc` for the static version of these methods.


..
  (commented out)
  .. toctree::
  :maxdepth: 2
  :hidden:

  varquery
  var.get
  ufunc
  reduce
  varops
  intgr
  deriv
  smooth
  interpolate
  composite
