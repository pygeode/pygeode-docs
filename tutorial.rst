==================
Tutorial
==================

PyGeode is a Python_ library intended to help with the management, analysis, and
visualization of geophysical datasets. It was originally developed with the
intent of dealing with the output of an atmospheric general circulation model
(specifically the Canadian Middle Atmosphere Model), but the library should be
general enough to apply to any gridded dataset. 

.. _Python: http://python.org/

PyGeode is based on a number of existing third party libraries which it uses to
perform the underlying computations and manipulations. Much of the underlying
computation and manipulation is done using numpy_, and PyGeode adopts many of
its conventions. Some use is also made of scipy_, and matplotlib_ is used for
plotting.

.. _numpy: http://numpy.scipy.org/
.. _scipy: http://numpy.scipy.org/
.. _matplotlib: http://matplotlib.sourceforge.net/

While there is no strict need to use the ipython_ interpreter, the plotting
features in combination with matplotlib are quite convenient and this tutorial
has been written assuming you are working with this combination. All the
commands given should still work in any other interpreter.

.. _ipython: http://ipython.scipy.org/

This tutorial is written in four parts. The first part gives a broad overview
and introduction to the library, including a brief description of some of the
most common tasks. The second part is a tutorial on how to perform
many typical operations on your data. The third part goes in to more detail on
how to read in and write out data, and on creating variables from scratch; this
includes an introduction to many of the types of axes recognized by PyGeode.
Finally, the fourth part introduces the plotting features of the library. 

.. toctree::
  :maxdepth: 1

  gettingstarted
  basic_ops
  adv_ops
  variableio
  plotting


