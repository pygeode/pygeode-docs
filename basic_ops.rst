Basic Variable Operations
=========================

.. currentmodule:: pygeode

Much of the functionality of PyGeode is found in the operations you can perform
on Var objects. We'll start with the basics of slicing variables, then move on
to more complicated operations. One important thing to keep in mind is that
these operations all delayed until the data is specifically requested. For
instance, one can compute an average over longitude as follows:

  >>> from pygeode.tutorial import t1
  >>> t_av = t1.Temp.mean('lon')
  >>> print t_av
  <Var 'Temp'>:
    Shape:  (lat)  (32)
    Axes:
      lat <Lat>      :  85 S to 85 N (32 values)
    Attributes:
      {}
    Type:  MeanVar (dtype="float64")

However, while the variable ``t_av`` now represents this average (and one
can carry out further operations with it), no actual averaging has been done.
This only happens when the data itself is requested:

  >>> print t_av[:]
  [ 1771.59115854  1223.57065946   891.29074384   686.0372979    556.28833859
     472.36640037   416.88604931   379.45966869   353.75681092   335.84596265
     323.2429993    314.35559351   308.15360203   303.97103724   301.38647664
     300.15173049   300.15173049   301.38647664   303.97103724   308.15360203
     314.35559351   323.2429993    335.84596265   353.75681092   379.45966869
     416.88604931   472.36640037   556.28833859   686.0372979    891.29074384
    1223.57065946  1771.59115854]

This should be kept in mind for the rest of the tutorial! We'll get a bit lazy:
what line 2 in the code above really does is return a new PyGeode variable
that represents the mean over the longitude axis of the source variable, without
actually calculating the mean, but we'll just say that we've computed the mean.
All of the operations in this section work this way - in fact, almost all of the
functions in PyGeode do, with a few exceptions that we'll mention explicitly
when we get there.

Selecting subsets
------------------

Documentation: :meth:`Var.__call__`

One of the most basic operations is to select a subset or subdomain of your
variable. For instance, to select a rectangular region of the same temperature
variable we just saw:

  >>> print t1.Temp(lat=(30, 50), lon=(100, 180))
  <Var 'Temp'>:
    Shape:  (lat,lon)  (4,15)
    Axes:
      lat <Lat>      :  30 N to 47 N (4 values)
      lon <Lon>      :  101 E to 180 E (15 values)
    Attributes:
      {}
    Type:  SlicedVar (dtype="float64")

PyGeode makes use of the calling syntax of Python to do slicing. While this is
arguably an abuse of the syntax, this operation is so common that it's a default
behaviour for PyGeode variables. The axes are specified as keyword arguments,
and ranges are given as a tuple in coordinate space (as opposed to the indices).

If the index is more convenient, you can specify this by prefixing the axis
name with ``i_``:

  >>> print t1.Temp(i_lat=5)
  <Var 'Temp'>:
    Shape:  (lat,lon)  (1,64)
    Axes:
      lat <Lat>      :  58 S
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {}
    Type:  SlicedVar (dtype="float64")

Note that not all axes need be specified; those axes are left alone. Also,
the returned variable will always have the same number of dimensions as the
source variable (in the same order, though not necessarily the same length),
even if some of them are of length 1. 

Another useful prefix is ``l_``, which lets you select an arbitrary set of
points:

  >>> print t1.Temp(l_lat=(-25, 0, 60, 70))
  <Var 'Temp'>:
    Shape:  (lat,lon)  (4,64)
    Axes:
      lat <Lat>      :  24 S to 69 N (4 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {}
    Type:  SlicedVar (dtype="float64")

Here the closest grid points are selected to the requested latitudes; keep in
mind that the subsetted axis (``lat`` in this case) will always retain the order
of the source axis, regardless of what order you give the list. There are some
other useful shortcuts here, but we'll introduce them a bit later on. 

These examples all return a new PyGeode variable, as explained at the beginning
of the section. If you ever do just need the raw numerical data (in the form of
a numpy array), you can use standard slicing notation on a pygeode variable
(``t1.Temp[:]`` will return everything), though note that unlike numpy slicing,
degenerate axes are not automatically removed. That is, ``t1.Temp[0, 1].shape``
will return ``(1, 1)``.

Arithmetic operations 
---------------------

Documentation: :doc:`ufunc` and :doc:`var.arith`

Arithmetic and mathematical operations are also supported by PyGeode. The
simplest are unary operations, which are performed elementwise. Most standard
mathematical functions (powers, exponentials, trigonometric functions, etc.) are
supported, and can be found in the main ``pygeode`` module:

.. plot:: scripts/vop1.py
  :include-source:

There are some convenience functions included, for instance, most trig functions
have a version which takes arguments in degrees rather than radians:

.. plot:: scripts/vop2.py
  :include-source:

In most cases the underlying operation is performed by the numpy equivalent. 

All the standard arithmetic operations are also supported and work as one would
expect, if all the arguments are defined on the same grid. If the arguments are
not defined on the same grid, PyGeode follows a set of rules for automatically
broadcasting them so that the operations behave as one might typically
desire - it's important to be aware of these rules as you can end up with some
unexpected results.

When performing a binary operation, PyGeode will broadcast each variable along
the dimensions of the other which it does not itself possess. The order of the
axes in the resulting variable is given by the first variable's axes, followed
by those of the second which are not included in the first. The one exception to
this rule is that if either variable is defined on a subset of the other's axes,
the order of the latter is maintained. 

A couple of examples will clarify this:

mapping




Statistics (Means, Standard deviations)
---------------------------------------

Documentation: :doc:`reduce`

As we saw at the beginning of this section, you can compute averages over a variable with
:meth:`~Var.mean`. By default this computes an average over the whole domain, but you can specify
particular axes you want to average over. For example,

  >>> from pygeode.tutorial import t2, pygeode as pyg
  >>> print t2.Temp
  <Var 'Temp'>:
  Shape:  (time,pres,lat,lon)  (3650,20,32,64)
  Axes:
    time <ModelTime365>:  Jan 1, 2011 00:00:00 to Dec 31, 2020 00:00:00 (3650 values)
    pres <Pres>    :  1000  hPa to 50  hPa (20 values)
    lat <Lat>      :  85 S to 85 N (32 values)
    lon <Lon>      :  0 E to 354 E (64 values)
  Attributes:
    {}
  Type:  Mul_Var (dtype="float64")
  >>> print t2.Temp.mean('pres', 'lon')
  <Var 'Temp'>:
    Shape:  (time,lat)  (3650,32)
    Axes:
      time <ModelTime365>:  Jan 1, 2011 00:00:00 to Dec 31, 2020 00:00:00 (3650 values)
      lat <Lat>      :  85 S to 85 N (32 values)
    Attributes:
      {}
    Type:  MeanVar (dtype="float64")
  
This computes an average over the pressure and longitude axes. You can specify axes in three ways:

  * by name, e.g. ``t2.Temp.mean('lon')``
  * by class, e.g. ``t2.Temp.mean(pyg.Lon)``
  * or by (zero-based) index, e.g. ``t2.Temp.mean(3)``

These will all return the same average. These three ways of identifying axes are pretty general
across Pygeode routines. 

Often it's useful to compute an average over a subset of the domain. You could first select the
subdomain, then compute the mean (``t2.Temp(lat=(70, 90)).mean('lat')``), but it's such a common
operation that there is a short cut in the form of another selection prefix, ``m_``:

  >>> print t2.Temp(m_lat=(70, 90))
  <Var 'Temp'>:
    Shape:  (time,pres,lon)  (3650,20,64)
    Axes:
      time <ModelTime365>:  Jan 1, 2011 00:00:00 to Dec 31, 2020 00:00:00 (3650 values)
      pres <Pres>    :  1000  hPa to 50  hPa (20 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {}
    Type:  WeightedMeanVar (dtype="float64")

This selects all latitudes between 70 N and 90 N and performs an average.

You may notice this last operation returned a ``WeightedMeanVar``, rather than just a ``MeanVar``.
PyGeode, by default, will perform weighted averages over axes which have weights associated with
them. In this case, our latitude axis is weighted its cosine, to take in to account the smaller
surface area near the poles:

  >>> print t2.Temp.lat.weights
  [ 0.00701861  0.01627439  0.02539207  0.03427386  0.0428359   0.05099806
    0.05868409  0.06582222  0.07234579  0.0781939   0.08331192  0.08765209
    0.09117388  0.0938444   0.09563872  0.09654009  0.09654009  0.09563872
    0.0938444   0.09117388  0.08765209  0.08331192  0.0781939   0.07234579
    0.06582222  0.05868409  0.05099806  0.0428359   0.03427386  0.02539207
    0.01627439  0.00701861]

You can turn this off, if desired, by specifying ``weights=False`` as a keyword argument:

  >>> print t2.Temp.mean('lat', weights=False)
  <Var 'Temp'>:
    Shape:  (time,pres,lon)  (3650,20,64)
    Axes:
      time <ModelTime365>:  Jan 1, 2011 00:00:00 to Dec 31, 2020 00:00:00 (3650 values)
      pres <Pres>    :  1000  hPa to 50  hPa (20 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {}
    Type:  MeanVar (dtype="float64")

You can, alternatively, specify your own weights to use, in the form of a Pygeode variable with the
same axes as those you would like to weight:

  >>> print t2.Temp.mean('lat', weights=pyg.sind(t2.Temp.lat))
  <Var 'Temp'>:
    Shape:  (time,pres,lon)  (3650,20,64)
    Axes:
      time <ModelTime365>:  Jan 1, 2011 00:00:00 to Dec 31, 2020 00:00:00 (3650 values)
      pres <Pres>    :  1000  hPa to 50  hPa (20 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {}
    Type:  WeightedMeanVar (dtype="float64")

The weights do not need to be normalized; PyGeode will do that automatically. 

There are several other axes reductions that behave similarly: :func:`Var.stdev()`,
:func:`Var.var()`, :func:`Var.sum()`, :func:`Var.min()`, :func:`Var.max()`. Some differences exist
though:

  * :func:`Var.sum()` by default does *not* use the axes weights; you can use the
    default weights by specifying ``weights=True`` as a keyword argument. 

  * :func:`Var.max()` and  :func:`Var.min()` do not use weights; they return the maximum and
    minimum values (respectively) along the axes being reduced.

Finally, there are also equivalents for several of these methods which are ``NaN`` aware. 

Reshaping variables
-------------------
Finally, there are a whole set of basic manipulations you can perform on variables if you need to
rework their structure. Some of the most common are introduced here; for a complete list see
:doc:`varops`. Keep in mind that variables are thought of as immutable objects - that is, once
they're created, they don't change - as before, what the following operations actually do is return
a new variable with the desired changes that wraps the old one.

  * :func:`Var.transpose()` reorders the axes of a variable:

  >>> print t2.Temp.transpose('lon', 'lat', 'pres', 'time')
  <Var 'Temp'>:
    Shape:  (lon,lat,pres,time)  (64,32,20,3650)
    Axes:
      lon <Lon>      :  0 E to 354 E (64 values)
      lat <Lat>      :  85 S to 85 N (32 values)
      pres <Pres>    :  1000  hPa to 50  hPa (20 values)
      time <ModelTime365>:  Jan 1, 2011 00:00:00 to Dec 31, 2020 00:00:00 (3650 values)
    Attributes:
      {}
    Type:  TransposedVar (dtype="float64")

  * :func:`Var.replace_axes()` replaces any or all axes of a variable. The new axes must have the
    same length as those they are replacing:

  >>> print t2.Temp.replace_axes(pres=t2.pres.logPAxis(H=7000))
  <Var 'Temp'>:
    Shape:  (time,lev,lat,lon)  (3650,20,32,64)
    Axes:
      time <ModelTime365>:  Jan 1, 2011 00:00:00 to Dec 31, 2020 00:00:00 (3650 values)
      lev <ZAxis>    :    0 to 20970.1 (20 values)
      lat <Lat>      :  85 S to 85 N (32 values)
      lon <Lon>      :  0 E to 354 E (64 values)
    Attributes:
      {}
    Type:  Replace_axes (dtype="float64")

  * :func:`Var.concat()` concatenates:
  
  * :func:`Var.rename()` :


