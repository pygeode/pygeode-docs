==================
Tutorial
==================

PyGeode is a Python_ library intended to help with the management, analysis, and
visualization of geophysical datasets. It was originally developed with the
intent of dealing with the output of an atmospheric general circulation model
(specifically the Canadian Middle Atmosphere Model), but the library has
been applied to many gridded dataset. 

.. _Python: http://python.org/

PyGeode is based on a number of existing third party libraries which it uses to
perform the underlying computations and manipulations. Much of the underlying
computation and manipulation is done using numpy_, and PyGeode adopts many of
its conventions. Some use is also made of scipy_, and matplotlib_ is used for
plotting. At present a small number of routines from the GSL are also used for
interpolation; this may change in the future to remove this dependency.

.. _numpy: http://numpy.org/
.. _scipy: http://scipy.org/
.. _matplotlib: http://matplotlib.org/

While there is no strict need to use the ipython_ interpreter, the plotting
features in combination with matplotlib are quite convenient and this tutorial
has been written assuming you are working with this combination. It can also be
run within a jupyter notebook. All the commands given should still work in any
other interpreter.

.. _ipython: http://ipython.scipy.org/

The tutorial is split up into a series of parts, beginning with a brief
overview the main features of the library and then proceeding through the
different features in greater detail.

.. toctree::
  :maxdepth: 2

  tut_gettingstarted
  tut_basics
  tut_io
  tut_plot
  tut_axes
  tut_datasets
  tut_adv

