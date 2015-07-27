==============
Reference
==============

.. currentmodule:: pygeode

The vast majority of the functionality provided by PyGeode is available within
the top level namespace of the module :mod:`pygeode`. The contents of this
top level namespace is summarized here. Note that there are also several
submodules with further functionality referenced in the summary as well. 

.. container:: module

  .. module:: pygeode

  The top level pygeode namespace

  :doc:`fileio`

  .. autosummary::

    open
    openall
    open_multi
    save

  .. rubric:: Fundamental Classes

  .. autosummary::

    Var
    Axis
    Dataset

  .. rubric:: Axis Types

  .. autosummary::

    NamedAxis
    Lon
    Lat
    Height
    Pres
    Hybrid
    StandardTime
    ModelTime365
    ModelTime360
    Yearless

  .. rubric:: Axis creation helper functions
  
  .. autosummary::
    regularlon
    regularlat
    gausslat

  .. rubric:: General operations

  .. autosummary::
    concat
    ensemble
    composite
    lag
    vprod
    vsum

  :doc:`ufunc`

  .. autosummary:: 

    sign
    exp
    log
    log10
    cos
    sin
    tan
    cosd
    sind
    tand
    sinh
    cosh
    tanh
    arcsin
    arccos
    arctan
    arctan2
    arcsind
    arccosd
    arctand
    arctand2
    arcsinh
    arccosh
    arctanh
    sqrt
    absolute
    nan_to_num
    minimum
    maximum
    real
    imag
    angle

  :doc:`climat`

  .. autosummary::

    dailymean
    monthlymean
    seasonalmean
    yearlymean
    diurnalmean
    climatology
    climtrend
    from_trend
    climat

  :doc:`timeutils`

  .. autosummary::

    timeutils
    timeutils.conform_values
    timeutils.date_diff
    timeutils.delta
    timeutils.jointimeaxes
    timeutils.modify
    timeutils.reltime
    timeutils.removeleapyears
    timeutils.splittimeaxis
    timeutils.wrapdate

  :doc:`stats`

  .. autosummary::
  
    correlate
    regress
    multiple_regress
    difference
    isnonzero

  :doc:`eof` 

  .. autosummary::

    EOF
    SVD
    eof

  :doc:`plot`

  .. autosummary::

    showvar
    showcol
    showgrid
    showlines
    vcontour
    vplot
    vscatter
    vquiver
    vstreamplot
    vsigmask
    plot

Under the hood
-------------------------------------

:doc:`view`

  A helper class for mapping subsets of variables 

.. toctree::
  :hidden:

  var
  axes
  dataset
  plot
  fileio
  timeutils
  climat
  stats
  eof
  view
