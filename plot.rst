Plot module
===================================

.. currentmodule:: pygeode

.. container:: module

  pygeode.plot

  Module containing most plotting-related commands for PyGeode. 

  .. rubric:: Top-level routines

  .. autosummary::

    showvar
    showgrid
    showlines

  .. rubric:: Second-level routines

  .. autosummary::

    vplot
    vcontour
    vscatter
    vhist
    vsigmask
    vstreamplot
    vquiver

  .. rubric:: Contouring helper functions

  .. autosummary::

    clfdict
    cldict
    log1sdict
    log2sdict

  .. rubric:: Matplotlib wrappers
    
  PyGeode uses a thin set of wrapper classes around matplotlib. The central
  object is the AxesWrapper class which provides an object that can produce a
  matplotlib plot. It was intended to make it possible to pickle and unpickle
  plots, though this often doesn't work. Most of the higher-level plotting
  functions return an AxesWrapper instance.

  The routines (most accessible as equivalent member functions of
  AxesWrapper) permit modifying and adding to plots much as one would with
  standard matplotlib figures. AxesWrappers can also be combined using 
  into compound plots using :func:`plot.grid`. 

  .. autosummary::

    plot.AxesWrapper
    plot.plot
    plot.fill_between
    plot.scatter
    plot.hist
    plot.axhline
    plot.axvline
    plot.legend
    plot.text
    plot.colorbar
    plot.contour
    plot.contourf
    plot.quiver
    plot.quiverkey
    plot.grid

.. autofunction:: showvar

.. autofunction:: showgrid

.. autofunction:: showlines

.. autofunction:: vplot

.. autofunction:: vcontour

.. autofunction:: vscatter

.. autofunction:: vhist

.. autofunction:: vsigmask

.. autofunction:: vstreamplot

.. autofunction:: vquiver

.. autofunction:: clfdict

.. autofunction:: cldict

.. autofunction:: log1sdict

.. autofunction:: log2sdict

.. currentmodule:: pygeode.plot

.. module:: pygeode.plot

.. class:: AxesWrapper

   A PyGeode wrapper class for a matplotlib figure or subplot

.. autofunction:: grid
