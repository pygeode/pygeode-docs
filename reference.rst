==============
Reference
==============

.. currentmodule:: pygeode

The vast majority of the functionality provided by PyGeode is available within
the top level namespace of the module :mod:`pygeode`, along with the
fundamental classes :class:`Var`, :class:`Axis`, and :class:`Dataset`.  The
contents of this top level namespace is summarized here. Several submodules
with further functionality are also included.

.. container:: module

  .. rubric:: pygeode

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
    NonCoordinateAxis

  .. rubric:: Axis helper functions
  
  .. autosummary::
    regularlon
    rotatelon
    regularlat
    gausslat
    standardtimerange
    standardtimen
    modeltime365range
    modeltime365n
    modeltime360range
    modeltime360n
    yearlessn

  :doc:`genops`

  .. autosummary::
    asdataset
    concatenate
    ensemble
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
    conj
    clip

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

  :doc:`timeutils`

  .. autosummary::

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
    paired_difference
    isnonzero

  :doc:`eof` 

  .. autosummary::

    EOF
    SVD

  :doc:`plot`

  .. autosummary::

    showvar
    showgrid
    showlines
    vcontour
    vplot
    vscatter
    vquiver
    vstreamplot
    vsigmask
    vhist
    clfdict
    cldict
    log1sdict
    log2sdict

  :doc:`external`

  .. autosummary::

    ext_xarray.to_xarray
    ext_xarray.from_xarray

Under the hood
-------------------------------------

:doc:`view`

  A helper class for mapping subsets of variables 

.. toctree::
  :hidden:

  var
  axes
  dataset
  genops
  plot
  fileio
  timeutils
  climat
  stats
  eof
  view
  custom
  external
